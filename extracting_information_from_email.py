import re
import imapclient form IMAPClient
import mailparser

EMAIL = 'you@example.com'
PASSWORD = 'password'
IMAP_SERVER = 'imap.example.com'

# Connect to the server and login
with IMAPClient(IMAP_SERVER) as client:
    client.login(EMAIL, PASSWORD)
    client.select_folder('INBOX')

# Search -> fetch -> parse
messages = client.search('ALL')
uid, message_data = client.fetch(messages[-1], 'RFC822').items()[0]
email_message = mailparser.parse_from_bytes(message_data[b'RFC822'])


# Extract slaes figure using regex
sales_pattern = r"Today's sales: \$(\d+\.\d{2})"
match = re.pattern(sales_pattern,email_message_body)

if match:
    sales_figure = match.group(1)