from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import logout
from .models import *
from django.contrib.auth.models import User as UserAccount 
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect
from django.db import connection

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

def allUsers(request):
        userList = userInfo.objects.filter(isPending=False)
        context = {'userList' : userList}
        return render(request, 'allUsers.php', context)

def changepw(request):
        return render(request, 'changePW.php')

def database(request):
        with connection.cursor() as cursor:
                cursor.execute("delete from grasa_event_locator_category")
                cursor.execute("ALTER TABLE grasa_event_locator_category AUTO_INCREMENT = 1")
        table = Category(description = "Academic Support")
        table.save()
        table = Category(description = "Arts & Culture")
        table.save()
        table = Category(description = "Career or College Readiness")
        table.save()
        table = Category(description = "Civic Engagement")
        table.save()
        table = Category(description = "Community Service / Service Learning")
        table.save()
        table = Category(description = "Financial Literacy")
        table.save()
        table = Category(description = "Health & Wellness")
        table.save()
        table = Category(description = "Media Technology")
        table.save()
        table = Category(description = "Mentoring")
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
        table = Category(description="Not Provided")
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
        table = Category(description="Not Specific")
        table.save()
        table = Category(description="Female")
        table.save()
        table = Category(description="Male")
        table.save()
        table = Category(description="Before School")
        table.save()
        table = Category(description="After School")
        table.save()
        table = Category(description="Evenings")
        table.save()
        table = Category(description="Weekends")
        table.save()
        table = Category(description="Summer")
        table.save()
        table = Category(description="Other")
        table.save()
        return HttpResponseRedirect("admin.php")

def createevent(request):
        if request.method == 'POST':
                print(request.POST['activity'])
                g = (str(request.user.userinfo.id))
                # program = Program(user_id_id = g, title=request.POST['title'], content=request.POST['content'], address=request.POST['address'], website=request.POST['website'], fees=request.POST['fees'], contact_name=request.POST['contact_name'], contact_email=request.POST['contact_email'], contact_phone=request.POST['contact_phone'])
                # program.save()
        else:
                return render(request, 'createEvent.php')
        return render(request, 'createEvent.php')

def editEvent(request):
        return render(request, 'editEvent.php')

def event(request, eventID):
        event = Program.objects.get(pk=eventID)

        context = {'event' : event}

        return render(request, 'event.php', context)

def index(request):
        allEventList = Program.objects.filter(isPending=False)
        context = {'allEventList': allEventList,}
        return render(request, 'index.php', context)

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
                        if user is not None and user.userinfo.isActive: 
                                auth_login(request, user)
                                if request.user.userinfo.isAdmin:
                                        return HttpResponseRedirect("admin.php")
                                else:
                                        return HttpResponseRedirect("provider.php")

                        else:
                                return render(request,'login.php',)
                                #Will need to put some logic here to state invalid credentials
        else:
                return render(request, 'login.php')
        return render(request, 'login.php')

def logout_view(request):
        logout(request)
        return HttpResponseRedirect("index.php")

def provider(request):
        if request.user.is_authenticated and not request.user.userinfo.isAdmin and request.user.userinfo.isActive:
                currentUser = userInfo.objects.filter(user=(request.user.userinfo.id - 1))
                myEventList = Program.objects.filter(user_id = request.user.userinfo.id)
                context = {'myEventList' : myEventList, 'currentUser' : currentUser}
                return render(request, "provider.php", context)
        if request.user.is_authenticated and request.user.userinfo.isAdmin and request.user.userinfo.isActive:
                return render(request, 'index.php', )
        else:
                return HttpResponseRedirect("login.php")

#         if request.method == 'POST':
#                 form = SubmitEvent(request.POST)
#
#                if form.is_valid():
#                        new_event = Events(event_title=request.POST['event_title'], event_extsite=request.POST['event_extsite'], event_address=request.POST['event_address'])
#                        new_event.save()
#        else:
#                form = SubmitEvent()
#
#        context = {'form' : form}


def register(request):
        if request.method == 'POST' and request.POST['current'] == request.POST['confirm'] :
                emailAddr = request.POST['emailAddr']
                orgName = request.POST['orgName']
                current = request.POST['current']
                newUser = UserAccount.objects.create_user(emailAddr, emailAddr, current)
                uInfo = userInfo(user = newUser, org_name = orgName)
                uInfo.save()
                return redirect("login_page")
                #return render(request, 'login.php')
        else:
                return render(request, 'register.php', )
        return render(request, 'register.php', )

def resetpw(request):
        return render(request, 'resetPW.php')

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

