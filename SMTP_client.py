import smtplib

#Set us the SMTP server

smtp_server = 'smtp.gmail.com'
stmp_port = 587
username = "madhikarmianshu@gmail.com"
password = "ruvypegoojuivjtr"

#Set up the message

from_address = "madhikarmianshu@gmail.com"
to_address = "madhikarmianshu@gmail.com"
subject = "Test Subject"
body = "Based SMTP"

message = f"""From: {from_address}
To: {to_address}
Subject: {subject}


{body}"""

#Send the message

with smtplib.SMTP(smtp_server, stmp_port) as server:
    server.starttls()
    server.login(username, password)
    server.sendmail(from_address, to_address, message)