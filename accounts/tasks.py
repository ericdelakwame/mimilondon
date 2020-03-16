from celery import task
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient
from accounts.models import User


sender = ''
sendgrid_token = ''


@task
def welcome_email(user_id):
    user = User.objects.get(id=user_id)
    mimi_subject = 'Welcome {}. '
    content = 'We are pleased to have you at mimilondonglamour. Please log in to your account and enjoy the freshest fabrics and clothing from our vendors. Thank You'
    message = Mail(
        from_email=sender,
        to_emails=user.email,
        subject=mimi_subject,
        html_content=content
    )

    try:
        sg = SendGridAPIClient(api_key=sendgrid_token)
        sg.send(message)
    except Exception as e:
        print(e)

