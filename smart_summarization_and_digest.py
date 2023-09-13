# pip install sumy

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Parser -> sumarizer -> parser.document -> Join str
def summarizer_email(email.content):
    parser = PlaintextParser.from_string(email_content, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, 3)  # 3 sentences summary
    return " ".join([str(sentence) for sentence in summary])

# Fetch -> decode ->summarize
with IMAPClient(IMAP_SERVER) as client:
    client.login(EMAIL, PASSWORD)
    client.select_folder('INBOX')
    messages = client.search()
