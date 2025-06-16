from datetime import date,datetime
from email.message import EmailMessage
import ssl
import smtplib

current_date = date.today()
current_date = str(current_date).replace('-', '')

def send_mail(total, success, reject):
    subject = f'validation email {current_date}'
    body = f'FILE VALIDATION DETAILS \n' \
           f'1. Number of files - {total} \n' \
           f'2. Number of successful files - {success} \n' \
           f'3. Number of rejected files - {reject} \n'



    sender_email = "vineet.sk666@gmail.com"
    receiver_email = "vineet.sk666@gmail.com"
    password = "lsel flar uyfw sgcd"  # Use app-specific password for Gmail

    # Create the email message
    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.set_content(body)

    # Secure connection
    context = ssl.create_default_context()

    # Send the email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.send_message(message)