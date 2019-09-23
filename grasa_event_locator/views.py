from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import logout

def admin(request):
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
        if request.method == 'POST':
                login_form_var = LoginForm(request.POST)
                if login_form_var.is_valid():
                        username = request.POST['username']
                        password = request.POST['password']
                        user = authenticate(request, username=username, password=password)
                        if user is not None:
                                auth_login(request, user)
                                print("Logged In!")
                                print(user.is_authenticated)
                                return(render(request,'provider.php'))
                        else:
                                return render(request,'login.php', {'login_form_var': login_form_var}, user)
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
        return render(request, 'register.php')

def resetpw(request):
        return render(request, 'resetPW.php')
