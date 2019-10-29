from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from . import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('aboutContact.php', views.aboutContact),
    path('admin.php', views.admin, name='admin_page'),
    path('admin_activate', views.admin_activate),
    path('create_database', views.create_database),
    path('allUsers.php', views.allUsers),
    path('allAdmins.php', views.allAdmins),
    path('allEvents.php', views.allEvents),
    path('changePW.php', views.changepw),
    path('createEvent.php', views.createevent),
    path("admin_user", views.admin_user),
    path('editEvent/<eventID>', views.editEvent, name='edit_page'),
    path('event/<eventID>', views.event, name='event_page'),
    path('index.php', views.index),
    path('', views.index),
    path('login.php', views.login, name='login_page'),
    path('provider.php', views.provider, name='provider_page'),
    path('register.php', views.register),
    path('resetPW.php', views.resetpw),
    path('logout', views.logout_view),
    path('admin/', admin.site.urls),
    path('approve_user/<userID>', views.approveUser, name='approve_user'),
    path('deny_user/<userID>', views.denyUser, name='deny_user'),
    path('approve_event/<eventID>', views.approveEvent, name='approve_event'),
    path('deny_event/<eventID>', views.denyEvent, name='deny_event'),
    path('approve_edit/<editID>', views.approveEdit, name='approve_edit'),
    path('deny_edit/<editID>', views.denyEdit, name='deny_edit'),
    path('changePWLogout/<reset_string>', views.changePWLogout, name='changePW_logout'),
    #path('search/', include('haystack.urls')),
    url(r'^search//?$', views.programSearchView.as_view(), name='haystack_search'),
    #path('search/', views.programSearchView.as_view(), name='haystack_search'),
]

