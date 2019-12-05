"""Miscellaneous helper functions used across grasa_event_locator.

This file includes various functions used across different parts of the Django
application. Additional code should only be added to this file if there is not a more
suitable place somewhere else.
"""

from django.core.mail import send_mail
from django.db import connection
from django.template.loader import render_to_string
from .models import Category, Program


def send_email(recip_address, subject, message):
    """Function to send an email using arguments provided in views.py

    Gathers the recipient address, subject, and message from views.py, and runs them through
    Django's send_mail function.

    Args:
        recip_address: A list of strings containing addresses to serve as the recipients.
        subject: String containing the email's subject.
        message: String containing the email's message.

    Returns:
        i: 0 or 1, indicating whether a message was sent or not. This is actually the number of emails sent,
        but the function used can only send one message at a time.
    """
    # The third argument in the send_mail is the origin email address.
    # When false, fail_silently specifcally raises an SMTPException if there's an error while sending mail.
    i = send_mail(subject, message, "grasatest@yahoo.com", recip_address, fail_silently=False)
    return i


def change_username(old_email, new_email, request):
    """Function to change an account's username.

        Gathers the old, new email addresses for the desired account, and the Django request,
        and changes the username using Django's provided function.

        Args:
            old_email: String containing the old email address/username of the account. In views.py, this is provided by a Django function.
            new_email: String containing the new email, provided from the change email form.
            request: Django request, used to change the username of the currently logged in user.
        """

    #Set existing username to the new email, then send an email to the old and new email.
    request.user.username = new_email
    request.user.save()
    request.user.email = new_email
    request.user.save()
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
    """Write the categories to the database.

        Because the database does not ship with the categories, this function writes the categories in.
        This is accessed via the <siteURL>/initial_setup link.
        """
    # Delete the contents of the lists of programs and categories.
    # While these should already be empty at the start, this is a precaution if the tables are tampered with pre-setup.
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
    # Begin a connection to the database to change the auto increment.
    # This will not open the app to SQL injection, because this does not take inputs from the user.
    with connection.cursor() as cursor:
        # Set the auto increment of the category table to 1,
        # to prevent a situation where the table attempts to count from a non-1 number.
        cursor.execute("ALTER TABLE grasa_event_locator_category AUTO_INCREMENT = 1")

    # Write categories to table using a for loop.
    # "description" is the column in the categories table where the category names go.
    for filter in categories:
        table = Category(description=filter)
        table.save()