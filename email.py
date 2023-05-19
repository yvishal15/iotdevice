import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "XXXXX sender_mail XXXXX"
    msg['from'] = user
    password = "XXX password_after_setting_up_two-factor-auth XXXXXX"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

if __name__ == '__main__' :
    email_alert("hey", "hello world", "rec_email")
