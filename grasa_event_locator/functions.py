from django.core.mail import send_mail
from .models import *
from django.db import connection

def send_email(address, subject, message):
    i = send_mail(
        subject,
        message,
        'grasatest@yahoo.com',
        address,
        fail_silently=False,
    )
    return i
def change_username(old_email, new_email, request):
    old_email = request.user.username
    request.user.username = request.POST['changeemail']
    request.user.save()
    request.user.email = request.POST['changeemail']
    request.user.save()
    new_email = request.user.username
    send_email([old_email, new_email], "GRASA - Email Changed",
               "The email for the " + request.user.userinfo.org_name + " account has changed from " + old_email + " to " + new_email + ". This email is being sent as a notification to both addresses.")
    return 0

def change_username(old_email, new_email, request):
    old_email = request.user.username
    request.user.username = request.POST['changeemail']
    request.user.save()
    request.user.email = request.POST['changeemail']
    request.user.save()
    new_email = request.user.username
    send_email([old_email, new_email], "GRASA - Email Changed",
               "The email for the " + request.user.userinfo.org_name + " account has changed from " + old_email + " to " + new_email + ". This email is being sent as a notification to both addresses.")
    return 0

def write_categories_table():
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
    # Refactored to match header and forms as well as fix duplicate search bug
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
    # Refactored to match header and forms
    table = Category(description="Non-Specific")
    table.save()
    # Refactored to match header and forms as well as fix duplicate search bug
    table = Category(description="Female-Only")
    table.save()
    # Refactored to match header and forms as well as fix duplicate search bug
    table = Category(description="Male-Only")
    table.save()
    # Refactored to match header and forms as well as fix duplicate search bug
    table = Category(description="Before-School")
    table.save()
    # Refactored to match header and forms as well as fix duplicate search bug
    table = Category(description="After-School")
    table.save()
    table = Category(description="Evenings")
    table.save()
    table = Category(description="Weekends")
    table.save()
    table = Category(description="Summer")
    table.save()
    # Refactored to "Other Time" to avoid conflicts with activities "Other" as well as fix duplicate search bug
    table = Category(description="Other-Time")
    table.save()
    return table