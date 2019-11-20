import rebuildIndex
import random
import string

from .forms import *
from .helpers import change_username, send_email, write_categories_table
from .models import userInfo, Category, Program, resetPWURLs
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth import \
    authenticate, \
    login as auth_login, \
    logout, \
    update_session_auth_hash
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User as UserAccount
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, reverse
from django.template.loader import render_to_string
from haystack.generic_views import SearchView
from haystack.forms import SearchForm
from smtplib import SMTPRecipientsRefused




def aboutContact(request):
    return render(request, 'about.html', context={
        "config": settings.CONFIG,
    })


def admin(request):
        if request.user.is_authenticated and request.user.userinfo.isAdmin and request.user.userinfo.isPending == False:
                pendingUserList = userInfo.objects.filter(isPending=True)
                pendingEventList = Program.objects.filter(isPending=True).filter(editOf=0)
                pendingEditList = Program.objects.filter(isPending=True).exclude(editOf=0)
                context = {'pendingUserList' : pendingUserList, 'pendingEventList' : pendingEventList, 'pendingEditList' : pendingEditList}
                if request.method == "POST":
                        # This line checks whether the changeemail field (which is the input field on the html page containing the new email address of
                        # the admin user [name=changeemail in the html]), exists. If so, perform change_username.
                        # It takes the current username, the new username (changeemail), and the request (the logged in user object),
                        # and changes the current username to the new username. See functions.py for that function.
                        if request.POST.get('changeemail') and (request.user.username != request.POST['changeemail']):
                            if UserAccount.objects.filter(username=request.POST['changeemail']).exists():
                                context = {'pendingUserList': pendingUserList, 'pendingEventList': pendingEventList,
                                           'pendingEditList': pendingEditList, 'user_exists' : True}
                            else:
                                change_username(request.user.username, request.POST['changeemail'] , request)
                        # The way we have the page coded, when a POST submit occurs,
                        # either the above situation happens in order to change the username,
                        # or this bottom situation, where the user has filled out the password modal, occurs.
                        # current is the current password field in the modal. new is the new password field. confirm is the confirm new password field.
                        # This checks whether the current password exists (that should be enough to determine if the modal has been filled out).
                        # It also checks whether new = confirm (in other words, do the new password fields match).
                        # If so, it writes the old password and new password to variables as seen below:
                        if request.POST.get('current') and (request.POST.get('new') == request.POST.get('confirm')):
                            current = request.POST['current']
                            new = request.POST['new']
                            # Checks if the password is actually right (check_password)
                            if request.user.check_password(current):
                                # If it is, set the password to new, and save the user.
                                request.user.set_password(new)
                                request.user.save()
                                update_session_auth_hash(request, request.user)
                            else:
                                context = {'pendingUserList' : pendingUserList, 'pendingEventList' : pendingEventList, 'pendingEditList' : pendingEditList, 'incorrect_password' : True}
                                return render(request, 'admin.html', context)
                        if request.POST.get('deny_user_reason'):
                            context = {'pendingUserList': pendingUserList, 'pendingEventList': pendingEventList,
                                       'pendingEditList': pendingEditList}
                            denyUser(request, request.POST.get('userid'), request.POST.get('deny_user_reason'))
                        if request.POST.get('deny_event_reason'):
                            context = {'pendingUserList': pendingUserList, 'pendingEventList': pendingEventList, 'pendingEditList': pendingEditList}
                            denyEvent(request, request.POST.get('eventid'), request.POST.get('deny_event_reason'))
                        if request.POST.get('edit_event_reason'):
                            print(request.POST.get('edit_event_reason'))
                            context = {'pendingUserList': pendingUserList, 'pendingEventList': pendingEventList,
                                       'pendingEditList': pendingEditList}
                            denyEdit(request, request.POST.get('editeventid'), request.POST.get('edit_event_reason'))
                        return render(request, 'admin.html', context)
                return render(request, 'admin.html', context)
        if request.user.is_authenticated and request.user.userinfo.isAdmin is False:
                return HttpResponseRedirect(reverse('provider_page'))
        else:
                return HttpResponseRedirect(reverse('login_page'))
        return render(request, 'admin.html')


def initial_setup(request):
    config = settings.CONFIG
    userList = userInfo.objects.filter(isAdmin=True)
    if (not userList):
        newUser = UserAccount.objects.create_superuser(config['admin_email'], config['admin_email'], "Password1")
        newUser.isStaff = True
        newUser.is_admin = True
        newUser.save()
        uInfo = userInfo(user=newUser, org_name="Administrator", isAdmin=True, isPending=False)
        uInfo.save()
    categoryList = Category.objects.all()
    if (not categoryList):
        write_categories_table()
    return HttpResponseRedirect(reverse('search'))
    

def allUsers(request):
    if request.user.is_authenticated and request.user.userinfo.isAdmin and not request.user.userinfo.isPending:
        userList = userInfo.objects.filter(isPending=False).filter(isAdmin=False)
        context = {'userList': userList}
        if request.method == 'POST':
                if request.POST.get('emailAddr'):
                    try:
                        # TODO: Change to hostname config value in email later...
                        send_email(
                            [request.POST.get('emailAddr')],
                            render_to_string("messaging/invite_provider_subject.txt"),
                            render_to_string(
                                "messaging/invite_provider_mail.txt",
                                context={"config": settings.CONFIG, })
                        )
                        context = {'userList': userList, 'sent_invite': True}
                    except SMTPRecipientsRefused:
                        context = {'userList': userList, 'invite_failure': True}
                if request.POST.get('delete'):
                    deleteUser(request, request.POST.get('delete'))
        return render(request, 'allUsers.html', context)
    return HttpResponseRedirect(reverse('search'))


def allAdmins(request):
    if request.user.is_authenticated and request.user.userinfo.isAdmin and not request.user.userinfo.isPending:
        userList = userInfo.objects.filter(isAdmin=True)
        if request.method == 'POST':
            if request.POST.get('current') or request.POST.get('confirm'):
                if (request.POST.get('current') == request.POST.get('confirm')):
                    #Check for Duplicate Email Entry (Email Already in Database)
                    emailAddr = request.POST['emailAddr']
                    checkInfo = UserAccount.objects.filter(email=emailAddr)
                    if(checkInfo.count() >= 1):
                        context = {'userList': userList, 'emailTaken' : True}
                        return render(request, 'allAdmins.html', context)
                    else:
                        current = request.POST['current']
                        newUser = UserAccount.objects.create_superuser(emailAddr, emailAddr, current)
                        uInfo = userInfo(user=newUser, org_name="Administrator", isAdmin=True, isPending=False)
                        uInfo.save()
                        try:
                            send_email(
                                [emailAddr],
                                render_to_string("messaging/invite_admin_subject.txt"),
                                render_to_string("messaging/invite_admin_mail.txt"))
                        except SMTPRecipientsRefused:
                            context = {'invalidEmail': True, 'userList': userList}
                            return render(request, 'allAdmins.html', context)
                        context = {'userList': userList, 'emailTaken' : False}
                        return render(request, 'allAdmins.html', context)
            if request.POST.get('delete'):
                deleteUser(request, request.POST.get('delete'))
                context = {'userList': userList}
                return render(request, 'allAdmins.html', context)
        else:
                context = {'userList': userList, 'emailTaken' : False}
                return render(request, 'allAdmins.html', context)
    return HttpResponseRedirect(reverse('search'))


def allEvents(request):
    if request.user.is_authenticated and request.user.userinfo.isAdmin and not request.user.userinfo.isPending:
        programList = Program.objects.filter(isPending=False)
        context = {'programList': programList}
        if request.method == 'POST':
            if request.POST.get('delete'):
                deleteEvent(request, request.POST.get('delete'))
        return render(request, 'allEvents.html', context)
    return HttpResponseRedirect(reverse('search'))


def changepw(request):
        if request.user.is_authenticated:
            if request.method == 'POST':
                    current = request.POST['current']
                    new = request.POST['new']
                    if request.user.check_password(current):
                            request.user.set_password(new)
                            request.user.save()
                    else:
                            return
        else:
            return HttpResponseRedirect(reverse('search'))
        return render(request, 'changePW.html')


def createevent(request):
        context = {"config": settings.CONFIG, }
        if request.method == 'POST':
                g = (str(request.user.userinfo.id))
                #Only change was to set fees to fees=float(request.POST['fees']) so that the value gets stored in DB as float
                program = Program(user_id_id = g, title=request.POST['title'], content=request.POST['content'], address=request.POST['address'], website=request.POST['website'], fees=float(request.POST['fees']), contact_name=request.POST['contact_name'], contact_email=request.POST['contact_email'], contact_phone=request.POST['contact_phone'], lat=request.POST['lat'], lng=request.POST['lng'])
                program.save()
                i = 0
                for tag in request.POST.getlist('activity'):
                        var = Category.objects.get(description=str(request.POST.getlist('activity')[i]))
                        var.save()
                        program.categories.add(var)
                        i= i + 1
                i = 0
                for tag in request.POST.getlist('transportation'):
                    if str(request.POST.getlist('transportation')[i]) != "Not-Provided":
                        var = Category.objects.get(description=str(request.POST.getlist('transportation')[i]))
                        var.save()
                        program.categories.add(var)
                        i = i + 1
                i = 0
                for tag in request.POST.getlist('grades'):
                        var = Category.objects.get(description=str(request.POST.getlist('grades')[i]))
                        var.save()
                        program.categories.add(var)
                        i = i + 1
                i = 0
                for tag in request.POST.getlist('gender'):
                    if str(request.POST.getlist('gender')[i]) != "Non-Specific":
                        var = Category.objects.get(description=str(request.POST.getlist('gender')[i]))
                        var.save()
                        program.categories.add(var)
                        i = i + 1
                i = 0
                for tag in request.POST.getlist('timing'):
                        var = Category.objects.get(description=str(request.POST.getlist('timing')[i]))
                        var.save()
                        program.categories.add(var)
                        i = i + 1
                return HttpResponseRedirect(reverse('provider_page'))
        else:
                return render(request, 'createEvent.html', context)
        return render(request, 'createEvent.html', context)


def getEventInfo(eventID):
        event = Program.objects.get(pk=eventID)
        grades_list_pub = ""
        timing_list_pub = ""
        gender_list_pub = ""
        transportation_list_pub = ""
        topic_list = event.categories.filter(id__lte=18)
        grades_list = event.categories.filter(id__gte=20)
        grades_list = grades_list.filter(id__lte=24)
        for g in grades_list:
                grades_list_pub = grades_list_pub + str(g) + ", "
        grades_list_pub = grades_list_pub[:-2]

        timing_list = event.categories.filter(id__gte=27)
        timing_list = timing_list.filter(id__lte=32)
        for t in timing_list:
                timing_list_pub = timing_list_pub + str(t) + ", "
        timing_list_pub = timing_list_pub[:-2]

        gender_list = event.categories.filter(id__gte=25)
        gender_list = gender_list.filter(id__lte=26)
        for g in gender_list:
                gender_list_pub = gender_list_pub + str(g) + ", "
        gender_list_pub = gender_list_pub[:-2]
        if gender_list.count() == 0:
                gender_list_pub = "Any Gender"

        transportation_list = event.categories.filter(id__gte=19)
        transportation_list = transportation_list.filter(id__lte=19)
        for t in transportation_list:
                transportation_list_pub = transportation_list_pub + str(t)
        if transportation_list.count() == 0:
                transportation_list_pub = "Not Provided"

        context = {'event' : event, 'topic_list' : topic_list, 'grades_list_pub' : grades_list_pub, 'timing_list_pub' : timing_list_pub, 'gender_list_pub' : gender_list_pub, 'transportation_list_pub' : transportation_list_pub, 'fees' : "{:0.2f}".format(event.fees)}

        address = context['event'].address.split('+')
        context['address'] = address

        return context


def event(request, eventID):
        context = getEventInfo(eventID)
        return render(request, 'event.html', context)


def getEventInfo(eventID):
        event = Program.objects.get(pk=eventID)
        grades_list_pub = ""
        timing_list_pub = ""
        gender_list_pub = ""
        transportation_list_pub = ""
        grades_list = event.categories.filter(id__gte=20)
        grades_list = grades_list.filter(id__lte=24)
        for g in grades_list:
                grades_list_pub = grades_list_pub + str(g) + ", "
        grades_list_pub = grades_list_pub[:-2]

        timing_list = event.categories.filter(id__gte=27)
        timing_list = timing_list.filter(id__lte=32)
        for t in timing_list:
                timing_list_pub = timing_list_pub + str(t) + ", "
        timing_list_pub = timing_list_pub[:-2]

        gender_list = event.categories.filter(id__gte=25)
        gender_list = gender_list.filter(id__lte=26)
        for g in gender_list:
                gender_list_pub = gender_list_pub + str(g) + ", "
        gender_list_pub = gender_list_pub[:-2]
        if gender_list.count() == 0:
                gender_list_pub = "Any Gender"

        transportation_list = event.categories.filter(id__gte=19)
        transportation_list = transportation_list.filter(id__lte=19)
        for t in transportation_list:
                transportation_list_pub = transportation_list_pub + str(t)
        if transportation_list.count() == 0:
                transportation_list_pub = "Not Provided"

        context = {
            'config': settings.CONFIG,
            'event': event,
            'fees': "{:0.2f}".format(event.fees),
            'gender_list_pub': gender_list_pub,
            'grades_list_pub': grades_list_pub,
            'timing_list_pub': timing_list_pub,
            'topic_list': event.categories.filter(id__lte=18),
            'transportation_list_pub': transportation_list_pub,
        }

        tempAddress = context['event'].address.split('+')
        address = []
        for i in range(0,len(tempAddress)):
                address.append(tempAddress[i].strip())

        context['address'] = address

        return context


def event(request, eventID):
        context = getEventInfo(eventID)
        return render(request, 'event.html', context)


def editEvent(request, eventID):
        event = Program.objects.get(pk=eventID)
        if request.user.is_authenticated and request.user.userinfo.isPending == False and (request.user.userinfo.isAdmin or request.user.userinfo.id == event.user_id.id):
            if request.method == 'POST':
                g = (str(request.user.userinfo.id))
                #Only change was to set fees to fees=float(request.POST['fees']) so that the value gets stored in DB as float
                program = Program(user_id_id = g, title=request.POST['title'], content=request.POST['content'], address=request.POST['address'], website=request.POST['website'], fees=float(request.POST['fees']), contact_name=request.POST['contact_name'], contact_email=request.POST['contact_email'], contact_phone=request.POST['contact_phone'], lat=request.POST['lat'], lng=request.POST['lng'], editOf=eventID)
                program.save()
                i = 0
                for tag in request.POST.getlist('activity'):
                        var = Category.objects.get(description=str(request.POST.getlist('activity')[i]))
                        var.save()
                        program.categories.add(var)
                        i= i + 1
                i = 0
                for tag in request.POST.getlist('transportation'):
                    if str(request.POST.getlist('transportation')[i]) != "Not-Provided":
                        var = Category.objects.get(description=str(request.POST.getlist('transportation')[i]))
                        var.save()
                        program.categories.add(var)
                        i = i + 1
                i = 0
                for tag in request.POST.getlist('grades'):
                        var = Category.objects.get(description=str(request.POST.getlist('grades')[i]))
                        var.save()
                        program.categories.add(var)
                        i = i + 1
                i = 0
                for tag in request.POST.getlist('gender'):
                    if str(request.POST.getlist('gender')[i]) != "Non-Specific":
                        var = Category.objects.get(description=str(request.POST.getlist('gender')[i]))
                        var.save()
                        program.categories.add(var)
                        i = i + 1
                i = 0
                for tag in request.POST.getlist('timing'):
                        var = Category.objects.get(description=str(request.POST.getlist('timing')[i]))
                        var.save()
                        program.categories.add(var)
                        i = i + 1
                return redirect("provider_page")

            elif request.method == 'GET':
                context = getEventInfo(eventID)
                activities = []
                for activity in context['topic_list']:
                        activities.append(str(activity))
                context['topic_list'] = activities

                timing1 = context['timing_list_pub'].split(',')
                timing2 = []

                for time in timing1:
                        timing2.append(time.strip())
                context['timing_list_pub'] = timing2

                grades1 = context['grades_list_pub'].split(',')
                grades2 = []

                for grade in grades1:
                        grades2.append(grade.strip())
                context['grades_list_pub'] = grades2

                return render(request, 'editEvent.html', context)
        else:
            return redirect('login_page')


        timing_list = event.categories.filter(id__gte=27)
        timing_list = timing_list.filter(id__lte=32)
        for t in timing_list:
                timing_list_pub = timing_list_pub + str(t) + ", "
        timing_list_pub = timing_list_pub[:-2]

        gender_list = event.categories.filter(id__gte=25)
        gender_list = gender_list.filter(id__lte=26)
        for g in gender_list:
                gender_list_pub = gender_list_pub + str(g) + ", "
        gender_list_pub = gender_list_pub[:-2]
        if gender_list.count() == 0:
                gender_list_pub = "Any Gender"

        transportation_list = event.categories.filter(id__gte=19)
        transportation_list = transportation_list.filter(id__lte=19)
        for t in transportation_list:
                transportation_list_pub = transportation_list_pub + str(t)
        if transportation_list.count() == 0:
                transportation_list_pub = "Not Provided"

        context = {'event' : event, 'timing_list_pub' : timing_list_pub, 'gender_list_pub' : gender_list_pub, 'transportation_list_pub' : transportation_list_pub, 'fees' : "{:0.2f}".format(event.fees)}
        return render(request, 'event.html', context)


def login(request):
        if request.user.is_authenticated:
                return HttpResponseRedirect(reverse('search'))
        if request.method == 'POST':
                        email = request.POST['email']
                        password = request.POST['password']
                        user = authenticate(request, username=email, password=password)
                        #This will check that the user is approved, if not
                        #(say and un-approved account) it will not let them
                        #log in. Same if no email/password match a row in the
                        #database, but will log them in and cause .is_authenticated
                        #to return true otherwise.
                        if user is not None and user.userinfo.isPending:
                            #Logic to see if the user is pending or doesn't exist
                            context = {'pendingUser' : True, 'wrongCredentials' : False}
                            return render(request, 'login.html', context)
                        if user is not None and not user.userinfo.isPending:
                                auth_login(request, user)
                                if request.user.userinfo.isAdmin:
                                        return HttpResponseRedirect(reverse('admin_page'))
                                else:
                                        return HttpResponseRedirect(reverse('provider_page'))
                        else:
                                context = {
                                        'pendingUser' : False,
                                        'wrongCredentials' : True
                                }
                                return render(request, 'login.html', context)
        else:
                context = {'pendingUser' : False, 'wrongCredentials' : False}
                return render(request, 'login.html', context)
        return render(request, 'login.html', context)


def logout_view(request):
        logout(request)
        return HttpResponseRedirect(reverse('search'))


def index(request):
        return redirect('search')


def provider(request):
        currentUser = userInfo.objects.filter(user=(request.user.userinfo.id - 1))
        myEventList = Program.objects.filter(user_id=request.user.userinfo.id)
        if request.method == 'POST':
            if request.POST.get('changeemail') and (request.user.username != request.POST['changeemail']):
                if UserAccount.objects.filter(username=request.POST['changeemail']).exists():
                    context = {
                        'config': settings.CONFIG,
                        'currentUser': currentUser,
                        'myEventList': myEventList,
                        'user_exists': True
                    }
                    return render(request, 'provider.html', context)
                else:
                    change_username(request.user.username, request.POST.get('changeemail'), request)
            if request.POST.get('changename'):
                    u = userInfo.objects.get(pk=request.user.id)
                    u.org_name = request.POST['changename']
                    u.save()
                    rebuildIndex.rebuildWhooshIndex()
            if request.POST.get('current') and (request.POST.get('new') == request.POST.get('confirm')):
                current = request.POST['current']
                new = request.POST['new']
                if request.user.check_password(current):
                    request.user.set_password(new)
                    request.user.save()
                    currentUser = userInfo.objects.filter(user=(request.user.userinfo.id - 1))
                    myEventList = Program.objects.filter(user_id=request.user.userinfo.id)
                    update_session_auth_hash(request, request.user)
                else:
                    currentUser = userInfo.objects.filter(user=(request.user.userinfo.id - 1))
                    myEventList = Program.objects.filter(user_id=request.user.userinfo.id)
                    context = {
                        'config': settings.CONFIG,
                        'currentUser': currentUser,
                        'myEventList': myEventList,
                        'incorrect_password': True,
                    }
                    return render(request, 'provider.html', context)
            if request.POST.get('delete'):
                deleteEvent(request, request.POST.get('delete'))
        if request.user.is_authenticated and not request.user.userinfo.isAdmin and not request.user.userinfo.isPending:
                currentUser = userInfo.objects.filter(user=(request.user.userinfo.id - 1))
                myEventList = Program.objects.filter(user_id = request.user.userinfo.id)
                context = {
                    'config': settings.CONFIG,
                    'currentUser': currentUser,
                    'myEventList': myEventList,
                }
                return render(request, 'provider.html', context)
        if request.user.is_authenticated and request.user.userinfo.isAdmin and not request.user.userinfo.isPending:
                return HttpResponseRedirect(reverse('admin_page'))
        else:
                return HttpResponseRedirect(reverse('login_page'))


def register(request):
        if request.method == 'POST' and request.POST['current'] == request.POST['confirm'] :
                emailAddr = request.POST['emailAddr']
                orgName = request.POST['orgName']
                current = request.POST['current']
                contact_name = request.POST['contact_name']
                contact_email = request.POST['contact_email']
                contact_phone = request.POST['contact_phone']
                #Check for Duplicate Email Entry (Email Already in Database)
                checkInfo = UserAccount.objects.filter(email=emailAddr)
                if(checkInfo.count() >= 1):
                    context = {
                        'config': settings.CONFIG,
                        'emailTaken': True,
                    }
                    return render(request, 'register.html', context)
                else:
                    newUser = UserAccount.objects.create_user(emailAddr, emailAddr, current)
                    uInfo = userInfo(user = newUser, org_name = orgName, contact_name = contact_name, contact_email = contact_email, contact_phone = contact_phone)
                    uInfo.save()
                    return redirect('login_page')
        else:
                context = {
                    'config': settings.CONFIG,
                    'emailTaken': False,
                }
                return render(request, 'register.html', context)
        context = {
            'config': settings.CONFIG,
            'emailTaken': False,
        }
        return render(request, 'register.html', context)


def resetpw(request):
        i = 0
        if request.method == 'POST':
                if UserAccount.objects.filter(username=request.POST['emailAddr']).exists():
                        try:
                            # This line attempts to delete any existing entry in the reset URL table for the user so the user cannot generate multiple reset links.
                            resetPWURLs.objects.get(user_ID = request.POST['emailAddr']).delete()
                        except resetPWURLs.DoesNotExist:
                            pass
                        reset_link = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(15)])
                        resetPWURL = resetPWURLs(user_ID = request.POST['emailAddr'], reset_string= reset_link, expiry_time= (datetime.now() + timedelta(minutes = 60)))
                        resetPWURL.save()
                        email_context = {
                            "config": settings.CONFIG,
                            "reset_link": reset_link,
                        }
                        send_email(
                            [request.POST['emailAddr']],
                            render_to_string("messaging/reset_password_subject.txt"),
                            render_to_string(
                                "messaging/reset_password_mail.txt",
                                context=email_context)
                        )
                return render(request, 'resetPW.html', context={
                    'email_submitted': True
                })
        else:
            return render(request, 'resetPW.html')


def resetPWForm(request, reset_string):
        try:
            #Check if the current time is greater than the timestamp in the table (which is 60 minutes after submission)
            if datetime.now() > datetime.strptime(resetPWURLs.objects.get(reset_string=reset_string).expiry_time, '%Y-%m-%d %H:%M:%S.%f'):
                #If so, show the expired message, hide the form.
                context = {'expired': True, "valid_string" : False}
                # Then delete the associated table entry that's out of date.
                resetPWURLs.objects.get(reset_string = reset_string).delete()
                return render(request, 'resetPWForm.html', context)
            # This is the most typical situation, where the form has a reset_string with a valid time.
            else:
                # The form should be showing if valid
                context = {"valid_string" : True}
                # If a post went through (check for the time again!), and the input was valid, change the password.
                if request.method == 'POST':
                    if request.POST.get('new') == request.POST.get('confirm'):
                        print(reset_string)
                        username = resetPWURLs.objects.get(reset_string=reset_string)
                        user = UserAccount.objects.get(username=username.user_ID)
                        user.set_password(request.POST['new'])
                        user.save()
                        resetPWURLs.objects.get(reset_string=reset_string).delete()
                        return redirect("login_page")
                    else:
                        # If the inputted passwords do not match, bring up the "confirm match" message, and continue to show the form.
                        context = {'pwdmatch' : True, 'valid_string' : True}
                        return render(request, 'resetPWForm.html', context)
                return render(request, 'resetPWForm.html', context)
        except resetPWURLs.DoesNotExist:
            # If the entry is not found, hide the resetPW form and show the "link expired message".
            context = {'expired': True, "valid_string" : False}
            return render(request, 'resetPWForm.html', context)
            #This is only triggered when no reset string is present. Note that this situation cannot happen without editing the URL file.
        return render(request, 'resetPWForm.html')


# Functional views, post only, need to be logged in admin, self defining names
def approveUser(request, userID):
        if request.user.is_authenticated and request.user.userinfo.isAdmin and not request.user.userinfo.isPending:
                u = userInfo.objects.get(pk=userID)
                u.isPending = False
                u.save()
                email_context = {
                    "config": settings.CONFIG,
                    "user": u,
                }
                send_email(
                    [str(u.user)],
                    render_to_string("messaging/provider_account_approval_subject.txt"),
                    render_to_string(
                        "messaging/provider_account_approval_mail.txt",
                        context=email_context)
                )
                send_email(
                    [str(u.contact_email)],
                    render_to_string("messaging/alternate_contact_confirm_subject.txt"),
                    render_to_string(
                        "messaging/alternate_contact_confirm_mail.txt",
                        context=email_context)
                )
                return redirect("admin_page")
        else:
                return redirect("login_page")


def denyUser(request, userID, deny_user_reason):
        if request.user.is_authenticated and request.user.userinfo.isAdmin and not request.user.userinfo.isPending:
                u = userInfo.objects.get(pk=userID)
                v = UserAccount.objects.get(id=userID)
                send_email(
                    [str(u.user)],
                    render_to_string("messaging/provider_account_denied_subject.txt"),
                    render_to_string(
                        "messaging/provider_account_denied_mail.txt",
                        context={
                            "config": settings.CONFIG,
                            "denied_reason": deny_user_reason,
                            "user": u,
                        })
                )
                u.delete()
                v.delete()
                rebuildIndex.rebuildWhooshIndex()
                return redirect("admin_page")
        else:
                return redirect("login_page")


def deleteUser(request, userID):
    if request.user.is_authenticated and request.user.userinfo.isAdmin and not request.user.userinfo.isPending:
        u = userInfo.objects.get(pk=userID)
        v = UserAccount.objects.get(id=userID)
        u.delete()
        v.delete()
        rebuildIndex.rebuildWhooshIndex()
        return redirect("admin_page")
    else:
        return redirect("login_page")


def approveEvent(request, eventID):
        if request.user.is_authenticated and request.user.userinfo.isAdmin and not request.user.userinfo.isPending:
                p = Program.objects.get(pk=eventID)
                p.isPending = False
                p.save()
                rebuildIndex.rebuildWhooshIndex()

                email_context = {
                    "config": settings.CONFIG,
                    "event_id": eventID,
                    "program": p,
                }
                send_email(
                    [str(UserAccount.objects.get(pk=p.user_id.user_id))],
                    render_to_string(
                        "messaging/event_approved_confirm_subject.txt",
                        context=email_context),
                    render_to_string(
                        "messaging/event_approved_confirm_mail.txt",
                        context=email_context)
                )
                return redirect("admin_page")
        else:
                return redirect("login_page")


def deleteEvent(request, eventID):
    p = Program.objects.get(pk=eventID)
    p.delete()
    rebuildIndex.rebuildWhooshIndex()

def denyEvent(request, eventID, deny_event_reason):
    p = Program.objects.get(pk=eventID)
    if request.user.is_authenticated and request.user.userinfo.isPending is False and (request.user.userinfo.isAdmin or request.user.userinfo.id is p.user_id.id):
        email_context = {
            "config": settings.CONFIG,
            "denied_reason": deny_event_reason,
            "program": p,
        }
        send_email(
            [str(UserAccount.objects.get(pk=p.user_id.user_id))],
            render_to_string(
                "messaging/event_denied_confirm_subject.txt",
                context=email_context),
            render_to_string(
                "messaging/event_denied_confirm_mail.txt",
                context=email_context)
        )
        p.delete()
        rebuildIndex.rebuildWhooshIndex()
        return redirect("admin_page")
    else:
        return redirect("login_page")

def approveEdit(request, editID):
        if request.user.is_authenticated and request.user.userinfo.isAdmin and not request.user.userinfo.isPending:
                p = Program.objects.get(pk=editID)
                # Check if oldP still exists (may have been deleted)
                oldP = Program.objects.filter(pk=p.editOf)
                if(oldP.count() >= 1):
                    oldP = Program.objects.get(pk=p.editOf)
                    oldP.title = p.title
                    oldP.content = p.content
                    oldP.address = p.address
                    oldP.lat = p.lat
                    oldP.lng = p.lng
                    oldP.website = p.website
                    oldP.fees = p.fees
                    oldP.contact_name = p.contact_name
                    oldP.contact_email = p.contact_email
                    oldP.contact_phone = p.contact_phone
                    for category in oldP.categories.all():
                        oldP.categories.remove(category)
                    for category2 in p.categories.all():
                        oldP.categories.add(category2)
                    oldP.save()
                    p.delete()
                    send_email(
                        [str(UserAccount.objects.get(pk=oldP.user_id.user_id))],
                        render_to_string(
                            "messaging/edit_approved_confirm_subject.txt",
                            context={"program": oldP}),
                        render_to_string(
                            "messaging/edit_approved_confirm_mail.txt",
                            context={
                                "event_id": str(oldP.id),
                                "program": oldP,
                            })
                    )
                else:
                    # It didn't exist, so make edit its own new event
                    p.isPending = False
                    p.editOf = 0
                    p.save()
                    send_email(
                        [str(UserAccount.objects.get(pk=p.user_id.user_id))],
                        render_to_string(
                            "messaging/edit_approved_confirm_subject.txt",
                            context={"program": p}),
                        render_to_string(
                            "messaging/edit_approved_confirm_mail.txt",
                            context={
                                "config": settings.CONFIG,
                                "event_id": str(p.id),
                                "program": p,
                            })
                    )
                rebuildIndex.rebuildWhooshIndex()
                return redirect("admin_page")
        else:
                return redirect("login_page")


def denyEdit(request, editID, deny_edit_reason):
        if request.user.is_authenticated and request.user.userinfo.isAdmin and not request.user.userinfo.isPending:
                p = Program.objects.get(pk=editID)
                email_context = {
                    "config": settings.CONFIG,
                    "program": p,
                    "denied_reason" : deny_edit_reason
                }
                send_email(
                    [str(UserAccount.objects.get(pk=p.user_id.user_id))],
                    render_to_string(
                        "messaging/edit_denied_confirm_subject.txt",
                        context=email_context),
                    render_to_string(
                        "messaging/edit_denied_confirm_mail.txt",
                        context=email_context)
                )
                p.delete()
                return redirect("admin_page")
        else:
                return redirect("login_page")


class programSearchView(SearchView):
    template_name = 'search/search.html'
    form_class = grasaSearchForm
