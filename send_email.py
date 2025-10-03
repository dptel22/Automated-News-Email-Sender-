import os
from dotenv import load_dotenv
import smtplib, ssl


load_dotenv()
gmail_password = os.getenv("GMAIL_PASSWORD")
gmail_user = os.getenv("GMAIL_USER")

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = gmail_user
    password = gmail_password

    receiver = gmail_user

    message = message.encode('utf-8')
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
