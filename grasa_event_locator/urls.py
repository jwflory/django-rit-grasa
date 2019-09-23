from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('admin.php', views.admin),
    path('changePW.php', views.changepw),
    path('createEvent.php', views.createevent),
    path('event.php', views.event),
    path('index.php', views.index),
    path('login.php', views.login),
    path('provider.php', views.provider),
    path('register.php', views.register),
    path('resetPW.php', views.resetpw),
    path('logout', views.logout_view),
]

