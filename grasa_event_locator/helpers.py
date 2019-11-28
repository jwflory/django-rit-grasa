"""Miscellaneous helper functions used across grasa_event_locator.

This file includes various functions used across different parts of the Django
application. Additional code should only be added to this file if there is not a more
suitable place somewhere else.
"""

from django.core.mail import send_mail
from django.db import connection
from django.template.loader import render_to_string
from .models import Category, Program


def send_email(address, subject, message):
    i = send_mail(subject, message, "grasatest@yahoo.com", address, fail_silently=False)
    return i


def change_username(old_email, new_email, request):
    old_email = request.user.username
    request.user.username = request.POST["changeemail"]
    request.user.save()
    request.user.email = request.POST["changeemail"]
    request.user.save()
    new_email = request.user.username
    send_email(
        [old_email, new_email],
        render_to_string("messaging/email_change_confirm_subject.txt"),
        render_to_string(
            "messaging/email_change_confirm_mail.txt",
            context={
                "request": request,
                "old_email": old_email,
                "new_email": new_email,
            },
        ),
    )
    return


def write_categories_table():
    Program.objects.all().delete()
    Category.objects.all().delete()
    categories = [
        "Academic Support",
        "Arts and Culture",
        "Career or College Readiness",
        "Civic Engagement",
        "Community Service / Service Learning",
        "Entrepreneurship / Leadership",
        "Financial Literacy",
        "Health and Wellness",
        "Media Technology",
        "Mentoring",
        "Nature / Environment",
        "Play",
        "Public Speaking",
        "Social and Emotional Learning (SEL)",
        "Sports and Recreation",
        "Science, Tech, Engineering, Math (STEM)",
        "Tutoring",
        "Other",
        "Provided",
        "K-3rd",
        "K-5th",
        "3rd-5th",
        "6th-8th",
        "9th-12th",
        "Female-Only",
        "Male-Only",
        "Before-School",
        "After-School",
        "Evenings",
        "Weekends",
        "Summer",
        "Other-Time",
    ]
    # Had to leave this in but there's no way for someone to inject SQL here
    with connection.cursor() as cursor:
        cursor.execute("ALTER TABLE grasa_event_locator_category AUTO_INCREMENT = 1")

    for filter in categories:
        table = Category(description=filter)
        table.save()
