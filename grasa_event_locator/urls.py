from . import views
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("about.html", views.aboutContact, name="about_contact"),
    path("admin.html", views.admin, name="admin_page"),
    path("allUsers.html", views.allUsers, name="all_users"),
    path("allAdmins.html", views.allAdmins, name="all_admins"),
    path("allEvents.html", views.allEvents, name="all_events"),
    path("createEvent.html", views.createevent, name="create_event"),
    path("initial_setup", views.initial_setup),
    path("editEvent/<eventID>", views.editEvent, name="edit_event"),
    path("event/<eventID>", views.event, name="event_page"),
    path("", views.index),
    path("login.html", views.login, name="login_page"),
    path("provider.html", views.provider, name="provider_page"),
    path("register.html", views.register, name="register"),
    path("resetPW.html", views.resetpw, name="resetpw_page"),
    path("logout", views.logout_view),
    path("admin/", admin.site.urls),
    path("approve_user/<userID>", views.approveUser, name="approve_user"),
    path("deny_user/<userID>", views.denyUser, name="deny_user"),
    path("approve_event/<eventID>", views.approveEvent, name="approve_event"),
    path("deny_event/<eventID>", views.denyEvent, name="deny_event"),
    path("approve_edit/<editID>", views.approveEdit, name="approve_edit"),
    path("deny_edit/<editID>", views.denyEdit, name="deny_edit"),
    path("resetPWForm/<reset_string>", views.resetPWForm, name="resetpw_form"),
    url(r"^search//?$", views.programSearchView.as_view(), name="search"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
