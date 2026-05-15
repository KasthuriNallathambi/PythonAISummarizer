import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
load_dotenv()

def send_email(message):

    host = "smtp.gmail.com"
    port = 465

    username = "welcomekasthuri@gmail.com"
    password = os.getenv("PASSWORD")

    receiver_email = "welcomekasthuri@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver_email,message)

