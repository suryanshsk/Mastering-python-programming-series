import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    from_email = "myemail@outlook.com"
    password = "my_app_password"

    # Email content
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    # Sending email
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

send_email(
    'Project Update Required',
    'Please update the project status by end of the day.',
    'manager@company.com'
)
