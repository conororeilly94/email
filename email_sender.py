import smtplib
from email.message import EmailMessage
from string import Template # Allows us to subsitute
from pathlib import Path # os.path. Access HTML file

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Conor O Reilly'
email['to'] = 'oreilly114@yahoo.com'
email['subject'] = 'You won a million euro'

#email.set_content('I am a Python pro') # Content of the email
email.set_content(html.subsitute({name = 'TinTin'}), 'html') # Changes $name in HTML file

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo() # Wake up message
	smtp.starttls() # Encryption mechanism
	smtp.login('email@gmail.com', 'password')
	smtp.send_message(email)
	print('All good')