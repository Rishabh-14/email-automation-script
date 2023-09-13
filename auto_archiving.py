from datetime import datetime, timedelta
from imapclient import IMAPClient

# Login details
EMAIL = 'you@example.com'
PASSWORD = 'password'
IMAP_SERVER = 'imap.example.com'

# Connect to the server and login
with IMAPClient(IMAP_SERVER) as client:
    client.login(EMAIL, PASSWORD)
    client.select_folder('INBOX')

    # Calculate the date 30 days ago
    cutoff_date = (datetime.now() - timedelta(days=30)).strftime('%d-%b-%Y')
    
    # Search for emails older than the cutoff date
    old_emails = client.search(['BEFORE', cutoff_date])
    
    # Move the old emails to an 'Archive' folder
    if old_emails:
        client.move(old_emails, 'Archive')
