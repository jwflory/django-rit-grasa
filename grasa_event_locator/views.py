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


def admin(request):
        if request.user.is_staff:
                return render(request, "admin.php")
        else:
                return HttpResponseRedirect("login.php")
        return render(request, 'admin.php')

def changepw(request):
        return render(request, 'changePW.php')

def createevent(request):
        return render(request, 'createEvent.php')

def event(request):
        return render(request, 'event.php')

def index(request):
        return render(request, 'index.php')

def login(request):
        if request.user.is_authenticated:
                return HttpResponseRedirect("index.php")
        if request.method == 'POST':
                        email = request.POST['email']
                        password = request.POST['password']
                        user = authenticate(request, username=email, password=password)
                        if user is not None:
                                auth_login(request, user)
                                return(render(request,'provider.php'))
                        else:
                                return render(request,'login.php',)
        else:
                login_form_var = LoginForm()
        return render(request, 'login.php', {'login_form_var': login_form_var})

def logout_view(request):
        logout(request)
        return HttpResponseRedirect("index.php")

def provider(request):
        if request.user.is_authenticated:
                return render(request, 'provider.php', )
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
                submission = User(email = emailAddr, password = current, org_name = orgName)
                submission.save()
                user = UserAccount.objects.create_user(emailAddr, emailAddr, current)
                return render(request, 'login.php')
        else:
                return render(request, 'register.php', )
        return render(request, 'register.php', )

def resetpw(request):
        return render(request, 'resetPW.php')
