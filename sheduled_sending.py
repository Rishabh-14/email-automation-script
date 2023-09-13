#pip install schedule

import smtplib
import schedule
import time
from email.message import EmailMessage

def send_email():
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('you@example.com', 'password')

        msg = EmailMessage()
        msg['From'] = 'you@example.com'
        msg['To'] = 'recipient@example.com'
        msg['Subject'] = 'Scheduled Email'
        msg.set_content('This is a scheduled email.')
        server.send_message(msg)
        print("Email sent!")
    
schedule.ever()day.at('10:00').do(send_email)

while True:
    schedule.run_pending()
    time.sleep(1)