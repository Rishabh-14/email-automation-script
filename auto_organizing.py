from imapclient import IMAPClient

# Login details
EMAIL = 'you@example.com'
PASSWORD = 'password'
IMAP_SERVER = 'imap.example.com'

# Connect to the server and login
with IMAPClient(IMAP_SERVER) as client:
    client.login(EMAIL, PASSWORD)
    client.select_folder('INBOX')

    # Filter emails from a specific domain and move them to 'Promotions' folder
    messages_from_promotions = client.search(['FROM', 'promotion@example.com'])
    client.move(messages_from_promotions, 'Promotions')

    # Similarly, you can add more criteria and organize other emails
