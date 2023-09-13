from imapclient import IMAPClient

EMAIL = 'you@example.com'
PASSWORD = 'password'
IMAP_SERVER = 'imap.example.com'

important_senders = ["important@partner.com", "boss@company.com"]
important_keywords = ["urgent", "contract", "meeting"]

priority_emails = []

with IMAPClient(IMAP_SERVER) as client:
    client.login(EMAIL, PASSWORD)
    client.select_folder('INBOX')
    
    # Prioritize by sender
    for sender in important_senders:
        messages_from_sender = client.search([f'FROM {sender}'])
        priority_emails.extend(messages_from_sender)

    # Prioritize by keywords in the email body
    for keyword in important_keywords:
        messages_with_keyword = client.search([f'BODY "{keyword}"'])
        priority_emails.extend(messages_with_keyword)

# Remove duplicates
priority_emails = list(set(priority_emails))
