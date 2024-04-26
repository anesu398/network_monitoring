import smtplib
from email.mime.text import MIMEText

def send_email_alert(sender_email, receiver_email, subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    smtp_server = smtplib.SMTP('smtp.example.com', 587)
    smtp_server.starttls()
    smtp_server.login(sender_email, 'password')
    smtp_server.sendmail(sender_email, [receiver_email], msg.as_string())
    smtp_server.quit()

# Example usage
send_email_alert('sender@example.com', 'receiver@example.com', 'Network Alert', 'Network issue detected!')
