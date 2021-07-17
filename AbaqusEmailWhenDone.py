# ABAQUS Email When Done
# Adapted By RJ Scales from https://programmersought.com/article/39731132377/ which contained typos
# Also aided by https://realpython.com/python-send-email/
#
# msg_from = "sender@gmail.com" # The email account used to send from, best if burner email.
# msg_from does not have to be from gmail. Turn ON "Allow less secure apps", this risks
# your account but makes it easier. Can do it via OAuth2 to keep the security via
# https://developers.google.com/gmail/api/quickstart/python
#
# passwd = "password" # Password for email account being sent from.
#
# msg_to = "sendee@gmail.com" # Account to which the email is to be sent to.
#
# subject = "ABAQUS Notification" # Subject of email
#
# content = "ABAQUS batch calculation completed" # The text content contained within the email

import smtplib  # Comes with the python version that Abaqus uses
from email.mime.text import MIMEText  # Comes with the python version that Abaqus uses


def AbaqusEmailWhenDone(msg_from, passwd, msg_to, subject, content):
    # Constructing the email
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to

    # Attempts sending the text only email
    try:
        s = smtplib.SMTP_SSL("smtp.gmail.com", 465) # 465 For SSL
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("Email sent successfully")
        s.quit()
    except Exception as e:
        print("Email failed to send due to "+str(e))
