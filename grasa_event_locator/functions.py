from django.core.mail import send_mail

def send_email(address, subject, message):
    i = send_mail(
        subject,
        message,
        'grasatest@yahoo.com',
        address,
        fail_silently=False,
    )
    return i