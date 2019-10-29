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

def aboutContact(request):
        return render(request, 'aboutContact.php')

def admin(request):

        if request.user.is_authenticated and request.user.userinfo.isAdmin and request.user.userinfo.isActive:
                pendingUserList = userInfo.objects.filter(isPending=True)
                pendingEventList = Program.objects.filter(isPending=True).filter(editOf=0)
                pendingEditList = Program.objects.filter(isPending=True).exclude(editOf=0)

                context = {'pendingUserList' : pendingUserList, 'pendingEventList' : pendingEventList, 'pendingEditList' : pendingEditList}

                return render(request, "admin.php", context)
        else:
                return HttpResponseRedirect("login.php")
        return render(request, 'admin.php')

def admin_activate(request):
        with connection.cursor() as cursor:
                cursor.execute("UPDATE `grasa_event_locator_userinfo` SET `isActive` = '1' WHERE `grasa_event_locator_userinfo`.`org_name` = 'Administrator';")
        return HttpResponseRedirect("login.php")

def admin_user(request):
        newUser = UserAccount.objects.create_user("grasatest@yahoo.com", "grasatest@yahoo.com", "Password1")
        uInfo = userInfo(user=newUser, org_name="Administrator")
        uInfo.save()
        with connection.cursor() as cursor:
                cursor.execute("UPDATE `grasa_event_locator_userinfo` SET `isAdmin` = '1' WHERE `grasa_event_locator_userinfo`.`org_name` = 'Administrator';")
                cursor.execute("UPDATE `grasa_event_locator_userinfo` SET `isPending` = '0' WHERE `grasa_event_locator_userinfo`.`org_name` = 'Administrator';")
                cursor.execute("UPDATE `grasa_event_locator_userinfo` SET `isActive` = '1' WHERE `grasa_event_locator_userinfo`.`org_name` = 'Administrator';")
        return HttpResponseRedirect("index.php")

def create_database(request):
        with connection.cursor() as cursor:
                cursor.execute("delete from grasa_event_locator_program_categories")
                cursor.execute("delete from grasa_event_locator_program")
                cursor.execute("delete from grasa_event_locator_category")
                cursor.execute("ALTER TABLE grasa_event_locator_category AUTO_INCREMENT = 1")
        table = Category(description="Academic Support")
        table.save()
        table = Category(description="Arts and Culture")
        table.save()
        table = Category(description="Career or College Readiness")
        table.save()
        table = Category(description="Civic Engagement")
        table.save()
        table = Category(description="Community Service / Service Learning")
        table.save()
        table = Category(description="Entrepreneurship / Leadership")
        table.save()
        table = Category(description="Financial Literacy")
        table.save()
        table = Category(description="Health & Wellness")
        table.save()
        table = Category(description="Media Technology")
        table.save()
        table = Category(description="Mentoring")
        table.save()
        table = Category(description="Nature & the Environment")
        table.save()
        table = Category(description="Play")
        table.save()
        table = Category(description="Public Speaking")
        table.save()
        table = Category(description="Social and Emotional Learning (SEL)")
        table.save()
        table = Category(description="Sports and Recreation")
        table.save()
        table = Category(description="STEM")
        table.save()
        table = Category(description="Tutoring")
        table.save()
        table = Category(description="Other")
        table.save()
        #Refactored to match header and forms as well as fix duplicate search bug
        table = Category(description="Not-Provided")
        table.save()
        table = Category(description="Provided")
        table.save()
        table = Category(description="K-3rd")
        table.save()
        table = Category(description="K-5th")
        table.save()
        table = Category(description="3rd-5th")
        table.save()
        table = Category(description="6th-8th")
        table.save()
        table = Category(description="9th-12th")
        table.save()
        #Refactored to match header and forms
        table = Category(description="Non-Specific")
        table.save()
        #Refactored to match header and forms as well as fix duplicate search bug
        table = Category(description="Female-Only")
        table.save()
        #Refactored to match header and forms as well as fix duplicate search bug
        table = Category(description="Male-Only")
        table.save()
        #Refactored to match header and forms as well as fix duplicate search bug
        table = Category(description="Before-School")
        table.save()
        #Refactored to match header and forms as well as fix duplicate search bug
        table = Category(description="After-School")
        table.save()
        table = Category(description="Evenings")
        table.save()
        table = Category(description="Weekends")
        table.save()
        table = Category(description="Summer")
        table.save()
        #Refactored to "Other Time" to avoid conflicts with activities "Other" as well as fix duplicate search bug
        table = Category(description="Other-Time")
        table.save()
        return HttpResponseRedirect("index.php")

def allUsers(request):
        userList = userInfo.objects.filter(isActive=True).filter(isAdmin=False)
        context = {'userList': userList}
        return render(request, 'allUsers.php', context)

def allAdmins(request):
        userList = userInfo.objects.filter(isAdmin=True)
        context = {'userList': userList}

        if request.method == 'POST' and request.POST['confirm'] == request.POST['confirm']:
                print(request.POST['emailAddr'])
                print(request.POST['current'])
                print(request.POST['confirm'])
                emailAddr = request.POST['emailAddr']
                current = request.POST['current']
                newUser = UserAccount.objects.create_user(emailAddr, emailAddr, current)
                uInfo = userInfo(user=newUser, org_name="Administrator")
                uInfo.save()
                with connection.cursor() as cursor:
                        cursor.execute("UPDATE `grasa_event_locator_userinfo` SET `isAdmin` = '1' WHERE `grasa_event_locator_userinfo`.`org_name` = 'Administrator';")
                        cursor.execute("UPDATE `grasa_event_locator_userinfo` SET `isPending` = '0' WHERE `grasa_event_locator_userinfo`.`org_name` = 'Administrator';")
                        cursor.execute("UPDATE `grasa_event_locator_userinfo` SET `isActive` = '1' WHERE `grasa_event_locator_userinfo`.`org_name` = 'Administrator';")
                return redirect("allAdmins.php")
                #return render(request, 'login.php')
        else:
                return render(request, 'allAdmins.php', context)
        return render(request, 'allAdmins.php', context)

def allEvents(request):
        userList = userInfo.objects.filter(isActive=True)
        context = {'userList': userList}
        return render(request, 'allEvents.php', context)

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
        context = {'event': event}
        return render(request, 'editEvent.php', context)

def event(request, eventID):
        event = Program.objects.get(pk=eventID)
        grades_list_pub = ""
        timing_list_pub = ""
        gender_list_pub = ""
        transportation_list_pub = ""
        topic_list = event.categories.filter(id__lte=18)
        grades_list = event.categories.filter(id__gte=21)
        grades_list = grades_list.filter(id__lte=25)
        for g in grades_list:
                grades_list_pub = grades_list_pub + str(g) + ", "
        grades_list_pub = grades_list_pub[:-2]

        timing_list = event.categories.filter(id__gte=29)
        timing_list = timing_list.filter(id__lte=34)
        for t in timing_list:
                timing_list_pub = timing_list_pub + str(t) + ", "
        timing_list_pub = timing_list_pub[:-2]

        gender_list = event.categories.filter(id__gte=26)
        gender_list = gender_list.filter(id__lte=28)
        for g in gender_list:
                gender_list_pub = gender_list_pub + str(g) + ", "
        gender_list_pub = gender_list_pub[:-2]

        transportation_list = event.categories.filter(id__gte=19)
        transportation_list = transportation_list.filter(id__lte=20)
        for t in transportation_list:
                transportation_list_pub = transportation_list_pub + str(t)

        context = {'event' : event, 'topic_list' : topic_list, 'grades_list_pub' : grades_list_pub, 'timing_list_pub' : timing_list_pub, 'gender_list_pub' : gender_list_pub, 'transportation_list_pub' : transportation_list_pub}
        return render(request, 'event.php', context)

def login(request):
        if request.user.is_authenticated:
                return HttpResponseRedirect("index.php")
        if request.method == 'POST':
                        email = request.POST['email']
                        password = request.POST['password']
                        user = authenticate(request, username=email, password=password)
                        #This will check that the user is active, if not
                        #(say and un-approved account) it will not let them
                        #log in. Same if no email/password match a row in the
                        #database, but will log them in and cause .is_authenticated
                        #to return true otherwise.
                        if user is not None and not user.userinfo.isActive:
                            #Logic to see if the user is pending or doesn't exist
                            context = {'pendingUser' : True, 'wrongCredentials' : False}
                            return render(request,'login.php', context)
                        if user is not None and user.userinfo.isActive:
                                auth_login(request, user)
                                print(send_email([request.POST['email']], "GRASA - Successful Login", "You Logged In!"))
                                u = userInfo.objects.get(pk=request.user.id)
                                u.last_login = str(datetime.now())[:-7]
                                u.save()
                                print(u.last_login)
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
                 with connection.cursor() as cursor:
                        cursor.execute("UPDATE `grasa_event_locator_userinfo` SET `org_name` = '" + request.POST['changename'] + "' WHERE `org_name` = '" + request.user.userinfo.org_name + "';")
                 return render(request, 'provider.php', )
        if request.user.is_authenticated and not request.user.userinfo.isAdmin and request.user.userinfo.isActive:
                currentUser = userInfo.objects.filter(user=(request.user.userinfo.id - 1))
                myEventList = Program.objects.filter(user_id = request.user.userinfo.id)
                context = {'myEventList' : myEventList, 'currentUser' : currentUser}
                return render(request, "provider.php", context)
        if request.user.is_authenticated and request.user.userinfo.isAdmin and request.user.userinfo.isActive:
                return render(request, 'index.php', )
        else:
                return HttpResponseRedirect("login.php")


def register(request):
        if request.method == 'POST' and request.POST['current'] == request.POST['confirm'] :
                print("POST OK")
                emailAddr = request.POST['emailAddr']
                orgName = request.POST['orgName']
                current = request.POST['current']
                contact_name = request.POST['contact_name']
                contact_email = request.POST['contact_email']
                contact_phone = request.POST['contact_phone']
                newUser = UserAccount.objects.create_user(emailAddr, emailAddr, current)
                uInfo = userInfo(user = newUser, org_name = orgName, contact_name = contact_name, contact_email = contact_email, contact_phone = contact_phone)
                uInfo.save()
                return redirect("login_page")
                #return render(request, 'login.php')
        else:
                return render(request, 'register.php', )
        return render(request, 'register.php', )

def resetpw(request):
        i = 0
        if request.method == 'POST':
                if User.objects.filter(username=request.POST['emailAddr']).exists():
                        with connection.cursor() as cursor:
                                cursor.execute("DELETE FROM `grasa_event_locator_resetpwurls` WHERE `user_ID` = '" + request.POST['emailAddr'] + "';")
                        resetlink = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(15)])
                        resetPWURL = resetPWURLs(user_ID = request.POST['emailAddr'], reset_string= resetlink)
                        resetPWURL.save()
                        print(send_email([request.POST['emailAddr']], "GRASA - Reset Password", "Link at http://hleong.ddns.net:8001/changePWLogout/" + resetlink))

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
        if request.user.is_authenticated and request.user.userinfo.isAdmin and request.user.userinfo.isActive:
                u = userInfo.objects.get(pk=userID)
                u.isPending = False
                u.isActive = True
                u.save()
                return redirect("admin_page")
        else:
                return redirect("login_page")

def denyUser(request, userID):
        if request.user.is_authenticated and request.user.userinfo.isAdmin and request.user.userinfo.isActive:
                u = userInfo.objects.get(pk=userID)
                #for program in u.program_set.all():
                #    program.delete()
                #^^^^^works but breaks page unless rebuild_index run
                u.isPending = False
                u.isActive = False
                u.save()
                return redirect("admin_page")
        else:
                return redirect("login_page")

                
def approveEvent(request, eventID):
        if request.user.is_authenticated and request.user.userinfo.isAdmin and request.user.userinfo.isActive:
                p = Program.objects.get(pk=eventID)
                p.isPending = False
                p.save()

                rebuildIndex.rebuildWhooshIndex()
                
                return redirect("admin_page")
        else:
                return redirect("login_page")

def denyEvent(request, eventID):
        if request.user.is_authenticated and request.user.userinfo.isAdmin and request.user.userinfo.isActive:
                p = Program.objects.get(pk=eventID)
                p.delete()
                return redirect("admin_page")
        else:
                return redirect("login_page")

def approveEdit(request, editID):
        if request.user.is_authenticated and request.user.userinfo.isAdmin and request.user.userinfo.isActive:
                p = Program.objects.get(pk=editID)
                oldP = Program.objects.get(pk=p.editOf)
                #Strange issue here, I get no errors but editOf won't switch to 0 and oldP wont delete
                oldP.delete()
                p.editOf = 0
                p.isPending = False
                p.save()
                return redirect("admin_page")
        else:
                return redirect("login_page")

def denyEdit(request, editID):
        if request.user.is_authenticated and request.user.userinfo.isAdmin and request.user.userinfo.isActive:
                p = Program.objects.get(pk=editID)
                p.delete()
                return redirect("admin_page")
        else:
                return redirect("login_page")

class programSearchView(SearchView):
        template_name = 'search/search.html'
        form_class = grasaSearchForm
        #Harrison's map work for Index
        # e_id = []
        # title = []
        # address = []
        # coord = []
        # coord2 = []
        # lat = []
        # lng = []
        # html_string = []
        # i = 1
        # zip_table = ""
        # try:
        #         allEventList = Program.objects.filter(isPending=False)
        #         for event in allEventList:
        #                 e_id.append(event.id)
        #                 title.append(event.title)
        #                 address.append(event.address)
        #                 coord.append(event.lat + ', ' + event.lng)
        #                 html_string= []
        #                 html_string_to_write = ""
        #                 i = 0

        #         zip_table = sorted(zip(coord, e_id, title, address))
        #         zip_table.sort()
        #         coord, e_id, title, address = zip(*zip_table)
        #         # Separate coordinates into lat and lng lists
        #         # for value in coord:
        #         #        lat2, lng2 = value.split(', ')
        #         #        lat.append(lat2)
        #         #        lng.append(lng2)
        #         for value in coord:
        #                 if i == 0:
        #                         html_string_to_write = html_string_to_write + "<b>" + str(title[i]) + "</b><br>" + str(address[i]) + "<br><a href='/event/" + str(e_id[i]) + "'>Details</a><hr>"
        #                 else:
        #                         if str(coord[i]) == str(coord[i - 1]):
        #                                 html_string_to_write = html_string_to_write + "<b>" + str(title[i]) + "</b><br>" + str(address[i]) + "<br><a href='/event/" + str(e_id[i]) + "'>Details</a><hr>"
        #                         else:
        #                                 # print(html_string_to_write)
        #                                 html_string.append(html_string_to_write)
        #                                 html_string_to_write = ""
        #                                 html_string_to_write = html_string_to_write + "<b>" + str(title[i]) + "</b><br>" + str(address[i]) + "<br><a href='/event/" + str(e_id[i]) + "'>Details</a><hr>"
        #                 coord2.append(coord[i])
        #                 i = i + 1
        #                 gotdata = 'null'
        #         html_string.append(html_string_to_write)
        #         coord2 = list(dict.fromkeys(coord2))
        #         for value in coord2:
        #                 lat2, lng2 = value.split(', ')
        #                 lat.append(lat2)
        #                 lng.append(lng2)
        #         # Remove horizontal line from map marker with only one location:
        #         for i in range(0, len(html_string) - 1):
        #              if html_string[i].count("<hr>") == 1:
        #                      html_string[i]= html_string[i].replace("<hr>","")
        #         zip_table = zip(lat, lng, html_string)
        # except (IndexError, ValueError, ProgrammingError):
        #         gotdata = 'null'
        # #Next two lines modified for search
        # #context = {'allEventList': allEventList, 'zip_table': zip_table}
        # #return render(request, 'index.php', context)


        # extra_context={ 'allEventList': allEventList, 'zip_table': zip_table }
        #form_class = SearchForm
        #searchqueryset = sqs

