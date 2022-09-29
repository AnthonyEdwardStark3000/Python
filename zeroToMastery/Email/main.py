import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html_location = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Suresh Babu'
email['to'] = 'sureshbabuj09@gmail.com'
email['subject'] = 'checking email with Python (SMTP)'

email.set_content(html_location.substitute(name='Suresh', language1='Python', language2='Logical ability'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # smtp.login(user='udemo1403@gmail.com', password='Sureshbabu.j01@')
    smtp.login(user='udemo1403@gmail.com', password='uldmusukixpnpbnb')
    smtp.send_message(email)
    print('Completed with sending the email.')
