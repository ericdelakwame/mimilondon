from celery import task
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient
from accounts.models import User
import os

sender = 'ericdelakwame@gmail.com'
sendgrid_token = os.environ.get('SENDGRID_API_KEY')


@task
def welcome_email(user_id):
    user = User.objects.get(id=user_id)
    mimi_subject = 'Welcome {}. '.format(user.first_name)
    content = 'We are pleased to have you at mimilondonglamour. Please log in to your account and enjoy the freshest fabrics and clothing from our latest collections. Thank You'
    message = Mail(
        from_email=sender,
        to_emails=user.email,
        subject=mimi_subject,
        html_content=content
    )
    message.template_id = 'd-c50dde4efc894586a1046c32c8e066bb'

    try:
        sg = SendGridAPIClient(api_key=sendgrid_token)
        sg.send(message)
    except Exception as e:
        print(e)

