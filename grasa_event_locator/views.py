from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from .functions import *
from .models import *
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import logout
from django.contrib.auth.models import User as UserAccount
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect
from django.db import connection
from haystack.generic_views import SearchView
from haystack.forms import SearchForm
import time
from django.db import *
import rebuildIndex
import random
import string
import time
from datetime import datetime
from django.shortcuts import reverse
from smtplib import *

def aboutContact(request):
        return render(request, 'aboutContact.php')

def admin(request):
        if request.user.is_authenticated and request.user.userinfo.isAdmin and request.user.userinfo.isPending == False:
                pendingUserList = userInfo.objects.filter(isPending=True)
                pendingEventList = Program.objects.filter(isPending=True).filter(editOf=0)
                pendingEditList = Program.objects.filter(isPending=True).exclude(editOf=0)
                context = {'pendingUserList' : pendingUserList, 'pendingEventList' : pendingEventList, 'pendingEditList' : pendingEditList}
                if request.method == "POST":
                        change_username(request.user.username, request.POST['changeemail'] , request)
                return render(request, "admin.php", context)
        if request.user.is_authenticated and request.user.userinfo.isAdmin == False:
                return HttpResponseRedirect('provider.php')
        else:
                return HttpResponseRedirect("login.php")
        return render(request, 'admin.php')

def admin_user(request):
        newUser = UserAccount.objects.create_superuser("grasatest@yahoo.com", "grasatest@yahoo.com", "Password1")
        newUser.save()
        newUser.isStaff = True
        newUser.save()
        newUser.is_admin = True
        newUser.save()
        uInfo = userInfo(user=newUser, org_name="Administrator", isAdmin=True, isPending=False)
        uInfo.save()
        return HttpResponseRedirect("index.php")

def create_database(request):
        write_categories_table()
        return HttpResponseRedirect("index.php")

def allUsers(request):
    if request.user.is_authenticated and request.user.userinfo.isAdmin and not request.user.userinfo.isPending:
        userList = userInfo.objects.filter(isPending=False).filter(isAdmin=False)
        context = {'userList': userList}

        if request.method == 'POST':
                print(send_email([request.POST.get('emailAddr')], "GRASA - Event Locator Registration", "You've been invited to sign up for the GRASA Event Locator! Register at http://grasa.larrimore.de/register.php"))
        return render(request, 'allUsers.php', context)
    return HttpResponseRedirect("index.php")

def allAdmins(request):
    if request.user.is_authenticated and request.user.userinfo.isAdmin and not request.user.userinfo.isPending:
        userList = userInfo.objects.filter(isAdmin=True)
        if request.method == 'POST' and request.POST['current'] == request.POST['confirm']:
            #Check for Duplicate Email Entry (Email Already in Database)
            emailAddr = request.POST['emailAddr']
            checkInfo = UserAccount.objects.filter(email=emailAddr)
            if(checkInfo.count() >= 1):
                context = {'userList': userList, 'emailTaken' : True}
                return render(request, 'allAdmins.php', context)
            else:
                current = request.POST['current']
                newUser = UserAccount.objects.create_superuser(emailAddr, emailAddr, current)
                uInfo = userInfo(user=newUser, org_name="Administrator", isAdmin=True, isPending=False)
                uInfo.save()
                try:
                    print(send_email([emailAddr], "GRASA - Administrator Account Created", "You've now been designated an Administrator at the GRASA Event Locator! Please consult GRASA for login information, if you have not already received it."))
                except SMTPRecipientsRefused:
                    print("Email not sent due to a formatting error.")
                    context = {'invalidEmail': True, 'userList': userList}
                    return render(request, 'allAdmins.php', context)
                context = {'userList': userList, 'emailTaken' : False}
                return render(request, 'allAdmins.php', context)
        else:
                context = {'userList': userList, 'emailTaken' : False}
                return render(request, 'allAdmins.php', context)
        return render(request, 'allAdmins.php', context)
    return HttpResponseRedirect("index.php")

def allEvents(request):
    if request.user.is_authenticated and request.user.userinfo.isAdmin and not request.user.userinfo.isPending:
        programList = Program.objects.filter(isPending=False)
        context = {'programList': programList}
        return render(request, 'allEvents.php', context)
    return HttpResponseRedirect("index.php")

def changepw(request):
        if request.user.is_authenticated:
            if request.method == 'POST':
                    current = request.POST['current']
                    new = request.POST['new']
                    if request.user.check_password(current):
                            request.user.set_password(new)
                            request.user.save()
                    else:
                            print("No")
        else:
            return HttpResponseRedirect("index.php")
        return render(request, 'changePW.php')

def createevent(request):
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
                return HttpResponseRedirect("provider.php")
        else:
                print("No")
                return render(request, 'createEvent.php')
        return render(request, 'createEvent.php')

def editEvent(request, eventID):
        event = Program.objects.get(pk=eventID)

        if request.user.is_authenticated and request.user.userinfo.isPending == False and (request.user.userinfo.isAdmin or request.user.userinfo.id == event.user_id.id):
            context = {'event': event}
            return render(request, 'editEvent.php', context)
        else:
            return redirect("login_page")

def event(request, eventID):
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
        return render(request, 'event.php', context)

def login(request):
        if request.user.is_authenticated:
                return HttpResponseRedirect(reverse('haystack_search'))
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
                            return render(request,'login.php', context)
                        if user is not None and not user.userinfo.isPending:
                                auth_login(request, user)
                                u = userInfo.objects.get(pk=request.user.id)
                                u.last_login = str(datetime.now())[:-7]
                                u.save()
                                if request.user.userinfo.isAdmin:
                                        return HttpResponseRedirect("admin.php")
                                else:
                                        return HttpResponseRedirect("provider.php")
                        else:
                                context = {'pendingUser' : False, 'wrongCredentials' : True}
                                return render(request,'login.php', context)
        else:
                context = {'pendingUser' : False, 'wrongCredentials' : False}
                return render(request, 'login.php', context)
        context = {'pendingUser' : False, 'wrongCredentials' : False}
        return render(request, 'login.php', context)

def logout_view(request):
        logout(request)
        return HttpResponseRedirect("index.php")

def index(request):
        return redirect("haystack_search")

def provider(request):
        if request.method == 'POST':
                if request.POST.get('changeemail'):
                        change_username(request.user.username, request.POST['changeemail'] , request)
                if request.POST.get('changename'):
                        u = userInfo.objects.get(pk=request.user.id)
                        u.org_name = request.POST['changename']
                        u.save()
                        rebuildIndex.rebuildWhooshIndex()
        if request.user.is_authenticated and not request.user.userinfo.isAdmin and not request.user.userinfo.isPending:
                currentUser = userInfo.objects.filter(user=(request.user.userinfo.id - 1))
                myEventList = Program.objects.filter(user_id = request.user.userinfo.id)
                context = {'myEventList' : myEventList, 'currentUser' : currentUser}
                return render(request, "provider.php", context)
        if request.user.is_authenticated and request.user.userinfo.isAdmin and not request.user.userinfo.isPending:
                return HttpResponseRedirect('admin.php')
        else:
                return HttpResponseRedirect("login.php")


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
                    context = {'emailTaken' : True}
                    return render(request, 'register.php', context)
                else:
                    newUser = UserAccount.objects.create_user(emailAddr, emailAddr, current)
                    uInfo = userInfo(user = newUser, org_name = orgName, contact_name = contact_name, contact_email = contact_email, contact_phone = contact_phone)
                    uInfo.save()
                    return redirect("login_page")
        else:
                context = {'emailTaken' : False}
                return render(request, 'register.php', context)
        context = {'emailTaken' : False}
        return render(request, 'register.php', context)

def resetpw(request):
        i = 0
        if request.method == 'POST':
                if User.objects.filter(username=request.POST['emailAddr']).exists():
                        with connection.cursor() as cursor:
                                cursor.execute("DELETE FROM `grasa_event_locator_resetpwurls` WHERE `user_ID` = '" + request.POST['emailAddr'] + "';")
                        resetlink = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(15)])
                        resetPWURL = resetPWURLs(user_ID = request.POST['emailAddr'], reset_string= resetlink)
                        resetPWURL.save()
                        # Make sure to pull the hostname from config file.
                        print(send_email([request.POST['emailAddr']], "GRASA - Reset Password", "You've requested a password reset at the GRASA Event Locator. Please visit this linnk: http://grasa.larrimore.de/changePWLogout/" + resetlink))

        return render(request, 'resetPW.php')

def changePWLogout(request, reset_string):
        if request.method == 'POST' and request.POST['new'] == request.POST['confirm']:
                print(reset_string)
                username = resetPWURLs.objects.get(reset_string=reset_string)
                print(username)
                user = User.objects.get(username=username.user_ID)
                print(user)
                user.set_password(request.POST['new'])
                user.save()
                with connection.cursor() as cursor:
                        cursor.execute(
                                "DELETE FROM `grasa_event_locator_resetpwurls` WHERE `user_ID` = '" + username.user_ID + "';")
                return redirect("login_page")
        else:
                return render(request, 'changePWLogout.php')

#Functional views, post only, need to be logged in admin, self defining names

def approveUser(request, userID):
        if request.user.is_authenticated and request.user.userinfo.isAdmin and not request.user.userinfo.isPending:
                u = userInfo.objects.get(pk=userID)
                u.isPending = False
                u.save()
                print(send_email([u.contact_email], "GRASA - Alternate Contact", "You are the alternative contact for " + u.org_name + " in the GRASA Event Locator. Please contact them for further details."))
                return redirect("admin_page")
        else:
                return redirect("login_page")

def denyUser(request, userID):
        if request.user.is_authenticated and request.user.userinfo.isAdmin and not request.user.userinfo.isPending:
                u = userInfo.objects.get(pk=userID)
                v = User.objects.get(id = userID)
                #for program in u.program_set.all():
                #    program.delete()
                #^^^^^works but breaks page unless rebuild_index run
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
                print(send_email([str(User.objects.get(pk=p.user_id.user_id))], "GRASA - Event Approved!", "Your event has been approved! See it at http://grasa.larrimore.de/event/" + str(p.id)))
                return redirect("admin_page")
        else:
                return redirect("login_page")

def denyEvent(request, eventID):
        p = Program.objects.get(pk=eventID)
        if request.user.is_authenticated and request.user.userinfo.isPending == False and (request.user.userinfo.isAdmin or request.user.userinfo.id == p.user_id.id):
                print(send_email([str(User.objects.get(pk=p.user_id.user_id))], "GRASA - Event Denied/Deleted", "Your event -"+ str(p.title) +"- has been denied or deleted. Contact GRASA for details."))
                p.delete()
                rebuildIndex.rebuildWhooshIndex()
                return redirect("admin_page")
        else:
                return redirect("login_page")

def approveEdit(request, editID):
        if request.user.is_authenticated and request.user.userinfo.isAdmin and not request.user.userinfo.isPending:
                p = Program.objects.get(pk=editID)
                oldP = Program.objects.get(pk=p.editOf)
                #Strange issue here, I get no errors but editOf won't switch to 0 and oldP wont delete
                oldP.delete()
                p.editOf = 0
                p.isPending = False
                p.save()
                print(send_email([str(User.objects.get(pk=p.user_id.user_id))], "GRASA - Event Edit Approved!", "Your edited event has been approved! See it at http://grasa.larrimore.de/event/" + str(p.id)))
                return redirect("admin_page")
        else:
                return redirect("login_page")

def denyEdit(request, editID):
        if request.user.is_authenticated and request.user.userinfo.isAdmin and not request.user.userinfo.isPending:
                p = Program.objects.get(pk=editID)
                p.delete()
                print(send_email([str(User.objects.get(pk=p.user_id.user_id))], "GRASA - Event Edit Denied", "Your edited event has been denied. Contact GRASA for details."))
                return redirect("admin_page")
        else:
                return redirect("login_page")

class programSearchView(SearchView):
        template_name = 'search/search.html'
        form_class = grasaSearchForm
