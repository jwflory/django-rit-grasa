from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('admin.php', views.admin, name='admin_page'),
    path('changePW.php', views.changepw),
    path('createEvent.php', views.createevent),
    path('event.php', views.event),
    path('index.php', views.index),
    path('login.php', views.login, name='login_page'),
    path('provider.php', views.provider, name='provider_page'),
    path('register.php', views.register),
    path('resetPW.php', views.resetpw),
    path('logout', views.logout_view),
    path('admin/', admin.site.urls),
    path('approve_user/<userID>', views.approveUser, name='approve_user'),
    path('deny_user/<userID>', views.denyUser, name='deny_user'),
]

