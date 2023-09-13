'''
import smtplib
from email.message import EmailMessage

# Create object -> From -> To -> Subject -> initialize
msg = EmailMessage()
msg['From'] = 'from@gmail.com'
msg['To'] = 'receiver@gmail.com'
msg['Subject'] = 'Test email'
msg.set_content('Hello python ')

#add attachment -> read object -> application type -> filename
with open('report.pdf','rb') as f: # add attachment
    msg.add_Attachment(f.read(),maintype = 'application', subtype = 'octet-stream',filename = 'report.pdf')

# start server -> login -> message

with smtplib.SMTP('smtp.example.com', 587) as server:
    server.starttls() # This starts the server
    server.login('you@example.com', 'password') # Authenticated login using email and password
    server.send_message(msg) # Sends email from message
'''