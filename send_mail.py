import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(subject, body, to_email, from_email, password):
    smtp_server = "smtp.mail.ru"
    smtp_port = 587

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, password)

        server.sendmail(from_email, to_email, msg.as_string())
        print("Письмо успешно отправлено!")
    except Exception as e:
        print(f"Ошибка при отправке письма: {e}")