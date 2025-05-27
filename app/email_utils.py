import sendgrid
from sendgrid.helpers.mail import Mail
from flask import render_template
import os

def send_email(to_email, subject, template, context):
    sg = sendgrid.SendGridAPIClient(api_key=os.getenv("SENDGRID_API_KEY"))
    content = render_template(template, **context)
    message = Mail(from_email=os.getenv("SENDER_EMAIL"), to_emails=to_email, subject=subject, html_content=content)
    response = sg.send(message)
    return response.status_code
