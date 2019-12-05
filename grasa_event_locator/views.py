import rebuild_index
import random
import string

from .forms import *
from .helpers import change_username, send_email, write_categories_table

# UserInfo is the class from the models.py folder. userinfo is the table name in SQL.
# Use UserInfo if you need info from the table for multiple users/unauthenticated users (via userInfo.objects...)
# Use userinfo if you need info from the table for the current user (via request.user.userinfo)
from .models import userInfo, Category, Program, resetPWURLs
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout,
    update_session_auth_hash,
)
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User as UserAccount
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, reverse
from django.template.loader import render_to_string
from haystack.generic_views import SearchView
from haystack.forms import SearchForm
from smtplib import SMTPRecipientsRefused

# View for about.html
def aboutContact(request):
    return render(request, "about.html", context={"config": settings.CONFIG,})


# View for admin.html
def admin(request):
    if request.user.is_authenticated and request.user.userinfo.isAdmin:
        pendingUserList = userInfo.objects.filter(isPending=True)
        # editOf refers to the ID number of an event, not 0/1.
        # pendingEventList filters on pending events with an editOf of 0 (meaning they are not edits)
        # pendingEditList filters on pending events that do not have an editof of 0 (meaning that they are edits of somethign)
        pendingEventList = Program.objects.filter(isPending=True).filter(editOf=0)
        pendingEditList = Program.objects.filter(isPending=True).exclude(editOf=0)
        context = {
            "pendingUserList": pendingUserList,
            "pendingEventList": pendingEventList,
            "pendingEditList": pendingEditList,
        }
        if request.method == "POST":
            # Change email/username. Checks that the new email is not the same as the old one.
            if request.POST.get("changeemail") and (
                request.user.username != request.POST["changeemail"]
            ):
                # Checks that the email does not already exist, if it does, add user_exists to the context,
                # which will display the appropriate message in the template.
                if UserAccount.objects.filter(
                    username=request.POST["changeemail"]
                ).exists():
                    context = {
                        "pendingUserList": pendingUserList,
                        "pendingEventList": pendingEventList,
                        "pendingEditList": pendingEditList,
                        "user_exists": True,
                    }
                else:
                    # If the email does not exists, and it passed the first check (old email != new email),
                    # change the username.
                    change_username(
                        request.user.username, request.POST["changeemail"], request
                    )
            # Change password, check that all three fields are filled out,
            # and that the new/confirm matches (validation also handles this).
            if (
                request.POST.get("current")
                and request.POST.get("new")
                and request.POST.get("confirm")
            ) and (request.POST.get("new") == request.POST.get("confirm")):
                current = request.POST["current"]
                new = request.POST["new"]
                # Checks if the password is actually right (check_password)
                if request.user.check_password(current):
                    # If it is, set the password to new, and save the user.
                    request.user.set_password(new)
                    request.user.save()
                    # Keep user logged in after the password change.
                    update_session_auth_hash(request, request.user)
                else:
                    # If the password check fails (is not the current password, pass incorrect_password to the context
                    # to display the appropriate message in the template)
                    context = {
                        "pendingUserList": pendingUserList,
                        "pendingEventList": pendingEventList,
                        "pendingEditList": pendingEditList,
                        "incorrect_password": True,
                    }
                    return render(request, "admin.html", context)
            # Check if a deny_user_reason (from the deny modal) exists.
            if request.POST.get("deny_user_reason"):
                context = {
                    "pendingUserList": pendingUserList,
                    "pendingEventList": pendingEventList,
                    "pendingEditList": pendingEditList,
                }
                # userid is a hidden field in the modal form. It needs to get passed to the denyUser function
                # to indicate which user to deny.
                denyUser(
                    request,
                    request.POST.get("userid"),
                    request.POST.get("deny_user_reason"),
                )
            # Check if a deny_event_reason (from the deny modal) exists.
            if request.POST.get("deny_event_reason"):
                context = {
                    "pendingUserList": pendingUserList,
                    "pendingEventList": pendingEventList,
                    "pendingEditList": pendingEditList,
                }
                # eventid is a hidden field in the modal form. It needs to get passed to the denyUser function
                # to indicate which edit to deny.
                denyEvent(
                    request,
                    request.POST.get("eventid"),
                    request.POST.get("deny_event_reason"),
                )
            # Check if a edit_event_reason (from the deny modal) exists.
            if request.POST.get("edit_event_reason"):
                print(request.POST.get("edit_event_reason"))
                context = {
                    "pendingUserList": pendingUserList,
                    "pendingEventList": pendingEventList,
                    "pendingEditList": pendingEditList,
                }
                # editevent is a hidden field in the modal form. It needs to get passed to the denyUser function
                # to indicate which edit to deny.
                denyEdit(
                    request,
                    request.POST.get("editeventid"),
                    request.POST.get("edit_event_reason"),
                )
            return render(request, "admin.html", context)
        return render(request, "admin.html", context)
    if request.user.is_authenticated and request.user.userinfo.isAdmin is False:
        return HttpResponseRedirect(reverse("provider_page"))
    else:
        return HttpResponseRedirect(reverse("login_page"))
    return render(request, "admin.html")


# View for initial_setup, which creates a superuser and writes categories to the table.
def initial_setup(request):
    config = settings.CONFIG
    # Check if the there are any admins. If not, then begin the process of creating an admin user.
    userList = userInfo.objects.filter(isAdmin=True)
    if not userList:
        # Create the Django user.
        newUser = UserAccount.objects.create_superuser(
            config["admin_email"], config["admin_email"], "Password1"
        )
        newUser.save()
        # Create the userInfo table user. Keep in mind, the table is linked to the Django user's table
        # for easy cross-referencing.
        uInfo = userInfo(
            user=newUser, org_name="Administrator", isAdmin=True, isPending=False
        )
        uInfo.save()
    # Check if there are any categories.
    categoryList = Category.objects.all()
    if not categoryList:
        write_categories_table()
    return HttpResponseRedirect(reverse("search"))


# View for allUsers.html (actually only displays all providers)
def allUsers(request):
    if (
        request.user.is_authenticated
        and request.user.userinfo.isAdmin
        and not request.user.userinfo.isPending
    ):
        # userList contains users that are not pending, and not admins.
        userList = userInfo.objects.filter(isPending=False).filter(isAdmin=False)
        context = {"userList": userList}
        if request.method == "POST":
            if request.POST.get("emailAddr"):
                # Try block is here to catch invalid email addresses,
                # which would normally throw an exception.
                # We want any exception here to be caught and the user made known
                # the email was invalid.
                try:
                    send_email(
                        [request.POST.get("emailAddr")],
                        render_to_string("messaging/invite_provider_subject.txt"),
                        render_to_string(
                            "messaging/invite_provider_mail.txt",
                            context={"config": settings.CONFIG,},
                        ),
                    )
                    # Message to indicate that sent_invite was successful.
                    context = {"userList": userList, "sent_invite": True}
                except SMTPRecipientsRefused:
                    # Message to indicate that the invite failed (note that the user will still be created)
                    context = {"userList": userList, "invite_failure": True}
            if request.POST.get("delete"):
                deleteUser(request, request.POST.get("delete"))
        return render(request, "allUsers.html", context)
    return HttpResponseRedirect(reverse("search"))


# View for allAdmins.html
def allAdmins(request):
    if (
        request.user.is_authenticated
        and request.user.userinfo.isAdmin
        and not request.user.userinfo.isPending
    ):
        # Note we are not writing to the context yet.
        # All if statements below cover all ways of getting to the page,
        # and none of them only have userList as the context.
        userList = userInfo.objects.filter(isAdmin=True)
        if request.method == "POST":
            # Check if both password fields are filled out
            if request.POST.get("current") and request.POST.get("confirm"):
                # Check if the new passwords are equal.
                if request.POST.get("current") == request.POST.get("confirm"):
                    # Check for Duplicate Email Entry (Email Already in Database)
                    emailAddr = request.POST["emailAddr"]
                    # Check if the new admin's email already exists in the database.
                    checkInfo = UserAccount.objects.filter(email=emailAddr)
                    if checkInfo.count() >= 1:
                        context = {"userList": userList, "emailTaken": True}
                        return render(request, "allAdmins.html", context)
                    else:
                        # If the new user is unique to the database, create the Django superuser.
                        current = request.POST["current"]
                        newUser = UserAccount.objects.create_superuser(
                            emailAddr, emailAddr, current
                        )
                        # Also create the userInfo user table.
                        uInfo = userInfo(
                            user=newUser,
                            org_name="Administrator",
                            isAdmin=True,
                            isPending=False,
                        )
                        uInfo.save()
                        # Also try to send an email to the new admin's email.
                        try:
                            send_email(
                                [emailAddr],
                                render_to_string("messaging/invite_admin_subject.txt"),
                                render_to_string("messaging/invite_admin_mail.txt"),
                            )
                        # But if it fails, write to the context invalidEmail,
                        # which displays the appropriate message in the template.
                        except SMTPRecipientsRefused:
                            context = {"invalidEmail": True, "userList": userList}
                            return render(request, "allAdmins.html", context)
                        # Set emailTaken to False, which will not show the email taken message in the template,
                        # as expected.
                        context = {"userList": userList, "emailTaken": False}
                        return render(request, "allAdmins.html", context)
            if request.POST.get("delete"):
                deleteUser(request, request.POST.get("delete"))
                context = {"userList": userList}
                return render(request, "allAdmins.html", context)
        else:
            context = {"userList": userList, "emailTaken": False}
            return render(request, "allAdmins.html", context)
    return HttpResponseRedirect(reverse("search"))


# View for allEvents.html
def allEvents(request):
    if (
        request.user.is_authenticated
        and request.user.userinfo.isAdmin
        and not request.user.userinfo.isPending
    ):
        programList = Program.objects.filter(isPending=False)
        context = {"programList": programList}
        if request.method == "POST":
            if request.POST.get("delete"):
                deleteEvent(request.POST.get("delete"))
        return render(request, "allEvents.html", context)
    return HttpResponseRedirect(reverse("search"))


# View for createEvent.html
def createevent(request):
    context = {
        "config": settings.CONFIG,
    }
    if request.user.is_authenticated and request.user.userinfo.isPending == False:
        if request.method == "POST":
            g = str(request.user.userinfo.id)
            # .title() sets the first letter of each word to be uppercase, this fixes the sorting issue where capital letters would appear on top
            program = Program(
                # This sets the user_id_id to the creator's id.
                user_id_id=g,
                title=(request.POST["title"]).title(),
                content=request.POST["content"],
                address=request.POST["address"],
                website=request.POST["website"],
                fees=float(request.POST["fees"]),
                contact_name=request.POST["contact_name"],
                contact_email=request.POST["contact_email"],
                contact_phone=request.POST["contact_phone"],
                # lat and lng are hidden values in the form that are determined from MapQuest,
                # after the form is submitted, based on the inputted street address.
                lat=request.POST["lat"],
                lng=request.POST["lng"],
            )
            program.save()
            i = 0
            # For the following "for tag" statements,
            # the categories from the POST statements are read through one at a time
            # and written to "var".
            # Then that category is written to the link table,
            # linking the program and it's categories together.
            for tag in request.POST.getlist("activity"):
                var = Category.objects.get(
                    description=str(request.POST.getlist("activity")[i])
                )
                var.save()
                program.categories.add(var)
                i = i + 1
            i = 0
            # There are only two options for transportation,
            # "Provided" or "Not Provided".
            # If transportation is provided, write it as such, but if Not-Provided, do not write anything.
            # If nothing is written, Not Provided will be shown in the event page template by default.
            for tag in request.POST.getlist("transportation"):
                if str(request.POST.getlist("transportation")[i]) != "Not-Provided":
                    var = Category.objects.get(
                        description=str(request.POST.getlist("transportation")[i])
                    )
                    var.save()
                    program.categories.add(var)
                    i = i + 1
            i = 0
            for tag in request.POST.getlist("grades"):
                var = Category.objects.get(
                    description=str(request.POST.getlist("grades")[i])
                )
                var.save()
                program.categories.add(var)
                i = i + 1
            i = 0
            # Similar case here as in Transportation.
            # Write male or female only, otherwise, Non Specific will be displayed.
            for tag in request.POST.getlist("gender"):
                if str(request.POST.getlist("gender")[i]) != "Non-Specific":
                    var = Category.objects.get(
                        description=str(request.POST.getlist("gender")[i])
                    )
                    var.save()
                    program.categories.add(var)
                    i = i + 1
            i = 0
            for tag in request.POST.getlist("timing"):
                var = Category.objects.get(
                    description=str(request.POST.getlist("timing")[i])
                )
                var.save()
                program.categories.add(var)
                i = i + 1
            return HttpResponseRedirect(reverse("provider_page"))
        else:
            return render(request, "createEvent.html", context)
    else:
        return HttpResponseRedirect(reverse("search"))


def getEventInfo(eventID):
    """Function to get information on events for the events page

        Takes the event ID from the url provided to the event view, and gathers the appropriate information to return
        to the template for use.

        Args:
            eventID: An integer that is associated with an event, the end of the /event/{#} url.
        Returns:
            context: The information about the event, for use by the template.
        """
    # Get the program from the table.
    event = Program.objects.get(pk=eventID)
    # To be used in the for loops below, the following lists must be declared here:
    grades_list_pub = ""
    timing_list_pub = ""
    gender_list_pub = ""
    transportation_list_pub = ""

    # Filter the link table twice for the queried event, the result is to get categories with results 20-24,
    # which correspond with the grades.
    grades_list = event.categories.filter(id__gte=20)
    grades_list = grades_list.filter(id__lte=24)
    # Then write those to the pub variable, with a comma in between each.
    for g in grades_list:
        grades_list_pub = grades_list_pub + str(g) + ", "
    # Remove the last two characters, to remove the trailing ", "
    grades_list_pub = grades_list_pub[:-2]

    # See above comments.
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
    # At this point, write any gender if there is no list (aka, male and female were not written to the link table)
    if gender_list.count() == 0:
        gender_list_pub = "Any Gender"

    transportation_list = event.categories.filter(id__gte=19)
    transportation_list = transportation_list.filter(id__lte=19)
    for t in transportation_list:
        transportation_list_pub = transportation_list_pub + str(t)
    # See above regarding Any Gender and the usage of Not Provided here.
    if transportation_list.count() == 0:
        transportation_list_pub = "Not Provided"

    # Write all to context for usage by the template, add formatting to fees to avoid extra 0's in the price.
    context = {
        "config": settings.CONFIG,
        "event": event,
        "fees": "{:0.2f}".format(event.fees),
        "gender_list_pub": gender_list_pub,
        "grades_list_pub": grades_list_pub,
        "timing_list_pub": timing_list_pub,
        # topic_list just needs to be a list rather than a string, as it is looped through in the template.
        "topic_list": event.categories.filter(id__lte=18),
        "transportation_list_pub": transportation_list_pub,
    }

    # Take the address from the event, and split it by the "+" symbol,
    # which was used during the submit as a delimiter.
    tempAddress = context["event"].address.split("+")
    address = []
    # Write each part of the address to the address list, removing any white space.
    for i in range(0, len(tempAddress)):
        address.append(tempAddress[i].strip())

    # Add address to the context.
    context["address"] = address

    return context


# View for event/<eventID>
# Note that the ID comes from the end of the URL, see the urls.py file for specifics.
def event(request, eventID):
    event = Program.objects.get(pk=eventID)
    if event.isPending:
        # This checks for an authenticated, non-pending user who is an admin or the creator of the event.
        if (
            request.user.is_authenticated
            and request.user.userinfo.isPending == False
            and (
                request.user.userinfo.isAdmin
                or request.user.userinfo.id == event.user_id.id
            )
        ):
            # Write the context from getEventInfo using the provided eventID to the event page's context.
            context = getEventInfo(eventID)
            # Then load the page with the event info.
            return render(request, "event.html", context)
        # If the user does not match the above, redirect to search.
        else:
            return HttpResponseRedirect(reverse("search"))
    # If not pending, load the page.
    context = getEventInfo(eventID)
    return render(request, "event.html", context)


# View for editEvent/<eventID>.
# Note that eventID is provided in the URL, see the urls.py file for details.
def editEvent(request, eventID):
    # Get the event.
    event = Program.objects.get(pk=eventID)
    if (
        # Make sure the user is authenticated, not pending, and is either the admin or the event creator.
        request.user.is_authenticated
        and request.user.userinfo.isPending == False
        and (
            request.user.userinfo.isAdmin
            or request.user.userinfo.id == event.user_id.id
        )
    ):
        # Most of this is the same as the createEvent view,
        # however, note that editOf will store the original event's ID.
        if request.method == "POST":
            g = str(request.user.userinfo.id)
            program = Program(
                user_id_id=g,
                title=request.POST["title"],
                content=request.POST["content"],
                address=request.POST["address"],
                website=request.POST["website"],
                fees=float(request.POST["fees"]),
                contact_name=request.POST["contact_name"],
                contact_email=request.POST["contact_email"],
                contact_phone=request.POST["contact_phone"],
                lat=request.POST["lat"],
                lng=request.POST["lng"],
                editOf=eventID,
            )
            program.save()
            i = 0
            for tag in request.POST.getlist("activity"):
                var = Category.objects.get(
                    description=str(request.POST.getlist("activity")[i])
                )
                var.save()
                program.categories.add(var)
                i = i + 1
            i = 0
            for tag in request.POST.getlist("transportation"):
                if str(request.POST.getlist("transportation")[i]) != "Not-Provided":
                    var = Category.objects.get(
                        description=str(request.POST.getlist("transportation")[i])
                    )
                    var.save()
                    program.categories.add(var)
                    i = i + 1
            i = 0
            for tag in request.POST.getlist("grades"):
                var = Category.objects.get(
                    description=str(request.POST.getlist("grades")[i])
                )
                var.save()
                program.categories.add(var)
                i = i + 1
            i = 0
            for tag in request.POST.getlist("gender"):
                if str(request.POST.getlist("gender")[i]) != "Non-Specific":
                    var = Category.objects.get(
                        description=str(request.POST.getlist("gender")[i])
                    )
                    var.save()
                    program.categories.add(var)
                    i = i + 1
            i = 0
            for tag in request.POST.getlist("timing"):
                var = Category.objects.get(
                    description=str(request.POST.getlist("timing")[i])
                )
                var.save()
                program.categories.add(var)
                i = i + 1
            return redirect("provider_page")

        # If get, then get the information from the event to prefill the edit page.
        elif request.method == "GET":
            context = getEventInfo(eventID)
            activities = []
            for activity in context["topic_list"]:
                activities.append(str(activity))
            context["topic_list"] = activities

            timing1 = context["timing_list_pub"].split(",")
            timing2 = []

            for time in timing1:
                timing2.append(time.strip())
            context["timing_list_pub"] = timing2

            grades1 = context["grades_list_pub"].split(",")
            grades2 = []

            for grade in grades1:
                grades2.append(grade.strip())
            context["grades_list_pub"] = grades2

            return render(request, "editEvent.html", context)
    else:
        return redirect("login_page")

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
        "event": event,
        "timing_list_pub": timing_list_pub,
        "gender_list_pub": gender_list_pub,
        "transportation_list_pub": transportation_list_pub,
        "fees": "{:0.2f}".format(event.fees),
    }
    return render(request, "event.html", context)


# View for site/login
def login(request):
    # If a user is already logged in, redirect to search.
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("search"))
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        # This will check that the user is approved, if not
        # (say and un-approved account) it will not let them
        # log in. Same if no email/password match a row in the
        # database, but will log them in and cause .is_authenticated
        # to return true otherwise.
        if user is not None and user.userinfo.isPending:
            # Logic to see if the user is pending or doesn't exist
            context = {"pendingUser": True, "wrongCredentials": False}
            return render(request, "login.html", context)
        # Check if a user's credentials are correct, and if the user is pending.
        if user is not None and not user.userinfo.isPending:
            auth_login(request, user)
            # Then redirect to admin or provider depending on the account.
            if request.user.userinfo.isAdmin:
                return HttpResponseRedirect(reverse("admin_page"))
            else:
                return HttpResponseRedirect(reverse("provider_page"))
        else:
            # Display message for wrong credentials in the template if nessasary.
            context = {"pendingUser": False, "wrongCredentials": True}
            return render(request, "login.html", context)
    else:
        context = {"pendingUser": False, "wrongCredentials": False}
        return render(request, "login.html", context)
    return render(request, "login.html", context)


# View for site/logout.
# Simply pass it the request.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("search"))


# View for site/index.
# It redirects the user to search.
def index(request):
    return redirect("search")


# View for provider.html
def provider(request):
    # currentUser gets the userInfo table information for the template (may not be used?).
    currentUser = userInfo.objects.filter(user=(request.user.userinfo.id - 1))
    # Get the user's programs.
    myEventList = Program.objects.filter(user_id=request.user.userinfo.id)
    if request.method == "POST":
        if request.POST.get("changeemail") and (
            request.user.username != request.POST["changeemail"]
        ):
            if UserAccount.objects.filter(
                username=request.POST["changeemail"]
            ).exists():
                context = {
                    "config": settings.CONFIG,
                    "currentUser": currentUser,
                    "myEventList": myEventList,
                    "user_exists": True,
                }
                return render(request, "provider.html", context)
            else:
                change_username(
                    request.user.username, request.POST.get("changeemail"), request
                )
        if request.POST.get("changename"):
            u = userInfo.objects.get(pk=request.user.id)
            u.org_name = request.POST["changename"]
            u.save()
            rebuild_index.rebuildWhooshIndex()
        if request.POST.get("current") and (
            request.POST.get("new") == request.POST.get("confirm")
        ):
            current = request.POST["current"]
            new = request.POST["new"]
            if request.user.check_password(current):
                request.user.set_password(new)
                request.user.save()
                currentUser = userInfo.objects.filter(
                    user=(request.user.userinfo.id - 1)
                )
                myEventList = Program.objects.filter(user_id=request.user.userinfo.id)
                update_session_auth_hash(request, request.user)
            else:
                currentUser = userInfo.objects.filter(
                    user=(request.user.userinfo.id - 1)
                )
                myEventList = Program.objects.filter(user_id=request.user.userinfo.id)
                context = {
                    "config": settings.CONFIG,
                    "currentUser": currentUser,
                    "myEventList": myEventList,
                    "incorrect_password": True,
                }
                return render(request, "provider.html", context)
        if request.POST.get("delete"):
            deleteEvent(request.POST.get("delete"))
    if (
        request.user.is_authenticated
        and not request.user.userinfo.isAdmin
        and not request.user.userinfo.isPending
    ):
        currentUser = userInfo.objects.filter(user=(request.user.userinfo.id - 1))
        myEventList = Program.objects.filter(user_id=request.user.userinfo.id)
        context = {
            "config": settings.CONFIG,
            "currentUser": currentUser,
            "myEventList": myEventList,
        }
        return render(request, "provider.html", context)
    if (
        request.user.is_authenticated
        and request.user.userinfo.isAdmin
        and not request.user.userinfo.isPending
    ):
        return HttpResponseRedirect(reverse("admin_page"))
    else:
        return HttpResponseRedirect(reverse("login_page"))


# View for register.html.
def register(request):
    if request.method == "POST" and request.POST["current"] == request.POST["confirm"]:
        emailAddr = request.POST["emailAddr"]
        orgName = request.POST["orgName"]
        current = request.POST["current"]
        contact_name = request.POST["contact_name"]
        contact_email = request.POST["contact_email"]
        contact_phone = request.POST["contact_phone"]
        # Check for Duplicate Email Entry (Email Already in Database)
        checkInfo = UserAccount.objects.filter(email=emailAddr)
        if checkInfo.count() >= 1:
            context = {
                "config": settings.CONFIG,
                "emailTaken": True,
            }
            return render(request, "register.html", context)
        else:
            # Create Django user.
            newUser = UserAccount.objects.create_user(emailAddr, emailAddr, current)
            # Create userInfo table entry. This is linked to the Django user system.
            uInfo = userInfo(
                user=newUser,
                org_name=orgName,
                contact_name=contact_name,
                contact_email=contact_email,
                contact_phone=contact_phone,
            )
            uInfo.save()
            return redirect("login_page")
    else:
        context = {
            "config": settings.CONFIG,
            "emailTaken": False,
        }
        return render(request, "register.html", context)
    context = {
        "config": settings.CONFIG,
        "emailTaken": False,
    }
    return render(request, "register.html", context)


# View for resetPW.html (the page to put an email address in)
def resetpw(request):
    if request.method == "POST":
        # Check for if the account exists.
        if UserAccount.objects.filter(username=request.POST["emailAddr"]).exists():
            try:
                # This line attempts to delete any existing entry in the reset URL table for the user so the user cannot generate multiple reset links.
                resetPWURLs.objects.get(user_ID=request.POST["emailAddr"]).delete()
            # If there is no entry in the table, let the app continue withiut throwing an error.
            except resetPWURLs.DoesNotExist:
                pass
            # Create reset link, a 15 characrer string, then write to table,
            # alomg with the associated user, and the exiration time.
            reset_link = "".join(
                [random.choice(string.ascii_letters + string.digits) for n in range(15)]
            )
            resetPWURL = resetPWURLs(
                user_ID=request.POST["emailAddr"],
                reset_string=reset_link,
                expiry_time=(datetime.now() + timedelta(minutes=60)),
            )
            resetPWURL.save()
            # Add reset link to the contt to be used in the email.
            email_context = {
                "config": settings.CONFIG,
                "reset_link": reset_link,
            }
            send_email(
                [request.POST["emailAddr"]],
                render_to_string("messaging/reset_password_subject.txt"),
                render_to_string(
                    "messaging/reset_password_mail.txt", context=email_context
                ),
            )
        # If the email is sent correctly, set email_submitted to true to display the appropriate message in the template.
        return render(request, "resetPW.html", context={"email_submitted": True})
    else:
        return render(request, "resetPW.html")


# View for resetPWForm.html/<reset_string>.
def resetPWForm(request, reset_string):
    try:
        # Check if the current time is greater than the timestamp in the table (which is 60 minutes after submission)
        if datetime.now() > datetime.strptime(
            resetPWURLs.objects.get(reset_string=reset_string).expiry_time,
            "%Y-%m-%d %H:%M:%S.%f",
        ):
            # If so, show the expired message, hide the form.
            context = {"expired": True, "valid_string": False}
            # Then delete the associated table entry that's out of date.
            resetPWURLs.objects.get(reset_string=reset_string).delete()
            return render(request, "resetPWForm.html", context)
        # This is the most typical situation, where the form has a reset_string with a valid time.
        else:
            # The form should be showing if valid.
            context = {"valid_string": True}
            # If a post went through (check for the time again!), and the input was valid, change the password.
            if request.method == "POST":
                if request.POST.get("new") == request.POST.get("confirm"):
                    print(reset_string)
                    username = resetPWURLs.objects.get(reset_string=reset_string)
                    user = UserAccount.objects.get(username=username.user_ID)
                    user.set_password(request.POST["new"])
                    user.save()
                    resetPWURLs.objects.get(reset_string=reset_string).delete()
                    return redirect("login_page")
                else:
                    # If the inputted passwords do not match, bring up the "confirm match" message, and continue to show the form.
                    context = {"pwdmatch": True, "valid_string": True}
                    return render(request, "resetPWForm.html", context)
            return render(request, "resetPWForm.html", context)
    except resetPWURLs.DoesNotExist:
        # If the entry is not found, hide the resetPW form and show the "link expired message".
        context = {"expired": True, "valid_string": False}
        return render(request, "resetPWForm.html", context)
        # This is only triggered when no reset string is present. Note that this situation cannot happen without editing the URL file.
    return render(request, "resetPWForm.html")


# Functional views, post only, need to be logged in admin, self defining names

# View for <url>/approve_user/userID.
def approveUser(request, userID):
    """Function to approve new users.

        Takes the indicated userID, and makes it so that user can log in.
        
        Args:
            request: The Django request, which is used to determine whether the currently authenticated user is an admin.
            userID: An integer indicating which user to approve.
            
        Returns:
            Redirects the user to the admin page. However, if the user is not authenticated, or not the admin,
            the page redirects to the login page, with the expectation that the admin will log in.
        """
    if (
        request.user.is_authenticated
        and request.user.userinfo.isAdmin
        and not request.user.userinfo.isPending
    ):
        # Set ispending to false, save he user. This will allow the user to log in.
        u = userInfo.objects.get(pk=userID)
        u.isPending = False
        u.save()
        # Send emails to the provider and alt. contact addresss.
        email_context = {
            "config": settings.CONFIG,
            "user": u,
        }
        send_email(
            [str(u.user)],
            render_to_string("messaging/provider_account_approval_subject.txt"),
            render_to_string(
                "messaging/provider_account_approval_mail.txt", context=email_context
            ),
        )
        send_email(
            [str(u.contact_email)],
            render_to_string("messaging/alternate_contact_confirm_subject.txt"),
            render_to_string(
                "messaging/alternate_contact_confirm_mail.txt", context=email_context
            ),
        )
        return redirect("admin_page")
    else:
        return redirect("login_page")


def denyUser(request, userID, deny_user_reason):
    """Function to deny new users.

        Takes the indicated userID, and removes that user from the Django users and userInfo table.
        Also takes the reason for the denial from the modal, and sends that reason to the provider email.

        Args:
            request: The Django request, which is used to determine whether the currently authenticated user is an admin.
            userID: An integer indicating which user to delete.
            deny_user_reason: A string from the modal, which is sent to the provider account's email address.
        
        Returns:
            Redirects the user to the admin page. However, if the user is not authenticated, or not the admin,
            the page redirects to the login page, with the expectation that the admin will log in. No changes are made
            to the accounts if this is the case.
        """
    if (
        request.user.is_authenticated
        and request.user.userinfo.isAdmin
        and not request.user.userinfo.isPending
    ):
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
                },
            ),
        )
        # Delete both the Django and userInfo user entries.
        u.delete()
        v.delete()
        rebuild_index.rebuildWhooshIndex()
        return redirect("admin_page")
    else:
        return redirect("login_page")


# Function to delete an existing user.
def deleteUser(request, userID):
    """Function to delete existing users, usually via the allAdmins or allUsers page.

        Takes the indicated userID, and removes that user from the Django and userInfo tables.
        Also removes all events associated with the deleted user. No reason for the deletion is collected.

        Args:
            request: The Django request, which is used to determine whether the currently authenticated user is an admin.
            userID: An integer indicating which user to delete.
        
        Returns:
            Redirects the user to the admin page. However, if the user is not authenticated, or not the admin,
            the page redirects to the login page, with the expectation that the admin will log in. No changes are made
            to the accounts if this is the case.
        """
    if (
        request.user.is_authenticated
        and request.user.userinfo.isAdmin
        and not request.user.userinfo.isPending
    ):
        u = userInfo.objects.get(pk=userID)
        v = UserAccount.objects.get(id=userID)
        # Delete the user from the Django and userInfo tables. This also removes any associated events.
        u.delete()
        v.delete()
        # Rebuild the index to update search results.
        rebuild_index.rebuildWhooshIndex()
        return redirect("admin_page")
    else:
        return redirect("login_page")


# View for <url>/approve_event/<eventID>
def approveEvent(request, eventID):
    """Function to approve pending events.
    
        Takes the indicated eventID, and sets the event's isPending to False. This makes is so the event shows up in search results.

        Args:
            request: The Django request, which is used to determine whether the currently authenticated user is an admin.
            eventID: An integer indicating which event to approve.
        
        Returns:
            Redirects the user to the admin page. However, if the user is not authenticated, or not the admin,
            the page redirects to the login page, with the expectation that the admin will log in. No changes are made
            to the accounts if this is the case.
        """
    if (
        request.user.is_authenticated
        and request.user.userinfo.isAdmin
        and not request.user.userinfo.isPending
    ):
        p = Program.objects.get(pk=eventID)
        p.isPending = False
        p.save()
        rebuild_index.rebuildWhooshIndex()

        email_context = {
            "config": settings.CONFIG,
            "event_id": eventID,
            "program": p,
        }
        send_email(
            [str(UserAccount.objects.get(pk=p.user_id.user_id))],
            render_to_string(
                "messaging/event_approved_confirm_subject.txt", context=email_context
            ),
            render_to_string(
                "messaging/event_approved_confirm_mail.txt", context=email_context
            ),
        )
        return redirect("admin_page")
    else:
        return redirect("login_page")


def deleteEvent(eventID):
    """Function to delete existing events, usually done via the allEvents page, or the provider portal. 
    
        Takes the indicated eventID, and deletes it from the program table.

        Args:
            eventID: An integer indicating which event to delete.
        
        Returns:
            Returns to the page the user was originally on.
        """
    p = Program.objects.get(pk=eventID)
    p.delete()
    rebuild_index.rebuildWhooshIndex()


# View for url/deny_edit/<editID>
def denyEvent(request, eventID, deny_event_reason):
    """Function to deny pending events.

        Takes the indicated eventID, and deletes the event.
        Also takes the reason for the denial from the modal, and sends that reason to the provider email.

        Args:
            request: The Django request, which is used to determine whether the currently authenticated user is an admin.
            eventID: An integer indicating which user to delete.
            deny_event_reason: A string from the modal, which is sent to the provider account's email address.
        
        Returns:
            Redirects the user to the admin page. However, if the user is not authenticated, or not the admin,
            the page redirects to the login page, with the expectation that the admin will log in. No changes are made
            to the accounts if this is the case.
        """
    p = Program.objects.get(pk=eventID)
    if (
        request.user.is_authenticated
        and request.user.userinfo.isPending is False
        and (request.user.userinfo.isAdmin or request.user.userinfo.id is p.user_id.id)
    ):
        email_context = {
            "config": settings.CONFIG,
            "denied_reason": deny_event_reason,
            "program": p,
        }
        send_email(
            [str(UserAccount.objects.get(pk=p.user_id.user_id))],
            render_to_string(
                "messaging/event_denied_confirm_subject.txt", context=email_context
            ),
            render_to_string(
                "messaging/event_denied_confirm_mail.txt", context=email_context
            ),
        )
        p.delete()
        rebuild_index.rebuildWhooshIndex()
        return redirect("admin_page")
    else:
        return redirect("login_page")


# View for <url>/approve_edit/<editID>
def approveEdit(request, editID):
    """Function to approve pending edits.

        Takes the indicated editID, and applies it's changes to it's original event. The edit is then deleted.
        This is done so that the link to the event is not changed between edits.

        Args:
            request: The Django request, which is used to determine whether the currently authenticated user is an admin.
            editID: An integer indicating which event to approve.

        Returns:
            Redirects the user to the admin page. However, if the user is not authenticated, or not the admin,
            the page redirects to the login page, with the expectation that the admin will log in. No changes are made
            to the accounts if this is the case.
        """
    if (
        request.user.is_authenticated
        and request.user.userinfo.isAdmin
        and not request.user.userinfo.isPending
    ):
        p = Program.objects.get(pk=editID)
        # Check if oldP still exists (may have been deleted)
        oldP = Program.objects.filter(pk=p.editOf)
        # If there is an old event, write the edit's information to the original event
        if oldP.count() >= 1:
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
            # Save the old event, delete the edit.
            oldP.save()
            p.delete()
            email_context = {
                "config": settings.CONFIG,
                "event_id": str(oldP.id),
                "program": oldP,
            }
            send_email(
                [str(UserAccount.objects.get(pk=oldP.user_id.user_id))],
                render_to_string(
                    "messaging/edit_approved_confirm_subject.txt", context=email_context
                ),
                render_to_string(
                    "messaging/edit_approved_confirm_mail.txt", context=email_context
                ),
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
                    context={"program": p},
                ),
                render_to_string(
                    "messaging/edit_approved_confirm_mail.txt",
                    context={
                        "config": settings.CONFIG,
                        "event_id": str(p.id),
                        "program": p,
                    },
                ),
            )
        rebuild_index.rebuildWhooshIndex()
        return redirect("admin_page")
    else:
        return redirect("login_page")


# View for <url>/deny_edit/<editID>
def denyEdit(request, editID, deny_edit_reason):
    """Function to deny pending events.

        Takes the indicated editID, and deletes the edit.
        Also takes the reason for the denial from the modal, and sends that reason to the provider email.

        Args:
            request: The Django request, which is used to determine whether the currently authenticated user is an admin.
            eventID: An integer indicating which edit to delete.
            deny_edit_reason: A string from the modal, which is sent to the provider account's email address.

        Returns:
            Redirects the user to the admin page. However, if the user is not authenticated, or not the admin,
            the page redirects to the login page, with the expectation that the admin will log in. No changes are made
            to the accounts if this is the case.
        """
    if (
        request.user.is_authenticated
        and request.user.userinfo.isAdmin
        and not request.user.userinfo.isPending
    ):
        p = Program.objects.get(pk=editID)
        email_context = {
            "config": settings.CONFIG,
            "program": p,
            "denied_reason": deny_edit_reason,
        }
        send_email(
            [str(UserAccount.objects.get(pk=p.user_id.user_id))],
            render_to_string(
                "messaging/edit_denied_confirm_subject.txt", context=email_context
            ),
            render_to_string(
                "messaging/edit_denied_confirm_mail.txt", context=email_context
            ),
        )
        p.delete()
        return redirect("admin_page")
    else:
        return redirect("login_page")


class programSearchView(SearchView):
    template_name = "search/search.html"
    form_class = grasaSearchForm
