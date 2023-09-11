import smtplib
from email.message import EmailMessage

# Create object -> From -> To -> Subject -> initialize
msg = EmailMessage()
msg['From'] = 'from@gmail.com'
msg['To'] = 'receiver@gmail.com'
msg['Subject'] = 'Test email'
msg.set_content('Hello python ')

# loop server -> start server -> login -> send message  