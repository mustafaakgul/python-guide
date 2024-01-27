import smtplib

sender = 'asdawd@gmail.com'
receivers = ['asdas@gmail.com']
message = """From: From Person <asda
To: To Person <
Subject: SMTP e-mail test"""

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    print("Successfully sent email")
except smtplib.SMTPException:
    print("Error: unable to send email")