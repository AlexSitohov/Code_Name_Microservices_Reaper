import smtplib
from email.message import EmailMessage

from mail_service_config import SMTP_USER, SMTP_PASSWORD

SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 587

SMTP_USER = SMTP_USER
SMTP_PASSWORD = SMTP_PASSWORD


async def send_email(username, user_email, verify_token):
    email = await create_email_template(username, user_email, verify_token)

    smtp_server = smtplib.SMTP(host=SMTP_HOST, port=SMTP_PORT)
    smtp_server.starttls()
    smtp_server.login(SMTP_USER, SMTP_PASSWORD)
    smtp_server.send_message(email)


async def create_email_template(username, user_email, verify_token):
    email = EmailMessage()
    email['Subject'] = "Код для подтверждение почты"
    email['From'] = SMTP_USER
    email['To'] = user_email
    email.set_content(f"Привет {username}. Вот твой код подтверждения: {verify_token}")

    return email
