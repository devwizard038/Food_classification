import smtplib
import email
from email.header import decode_header

# IMAP settings
IMAP_SERVER = 'gmail.com'
EMAIL = ''
PASSWORD = ''

# Connect to the IMAP server
mail = smtplib.SMTP(IMAP_SERVER)
mail.login(EMAIL, PASSWORD)
mail.select('inbox')

# Search for unseen messages
status, messages = mail.search(None, 'UNSEEN')

if status == 'OK':
    for num in messages[0].split():
        status, data = mail.fetch(num, '(RFC822)')
        if status == 'OK':
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)
            subject = decode_header(msg['Subject'])[0][0]
            sender = decode_header(msg['From'])[0][0]
            
            print(f'Subject: {subject}')
            print(f'Sender: {sender}')
            # Add your logic to trigger actions based on the email content

mail.close()
mail.logout()