import os
import json
from celery import task
from django.core.mail import send_mail
from .models import Order, OrderItem
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient
from orders.models import OrderItem
sendgrid_key = os.environ.get('SENDGRID_API_KEY')
sender = os.environ.get('EMAIL_SENDER')


@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    receipient = order.email
    mail_subject = 'Order No.  {}'.format(order_id)
    body = 'Dear {}, \n\n You have successfully placed an order. \
        Your order Id is {}. '.format(order.first_name, order.id)
    message = Mail(
        from_email=sender, to_emails=receipient,
        subject=mail_subject,
        html_content=body,

    )
    message.dynamic_template_data = {

        'first_name': '{}'.format(order.first_name),
    }
    message.template_id = 'd-6b98c063f48449a289b249dda5cb6197'
    try:
        sg = SendGridAPIClient(api_key=sendgrid_key)
        sg.send(message)
    except Exception as e:
        print(e)


