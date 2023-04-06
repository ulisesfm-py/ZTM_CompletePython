import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # os.path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Ulises Fernández'
email['to'] = 'ulisestgy@gmail.com'
email['subject'] = 'this is a Python exercise'

#email.set_content('I am practicing email sending through Python')
# email.set_content(html.substitute({'name' = 'TinTin'}), 'html')
email.set_content(html.substitute({'name': 'Tintin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    # this will be confusing, but you just need to copy
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ulisestgy@gmail.com', 'notarealpassword')
    smtp.send_message(email)
    print('all good')
