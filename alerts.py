#5_alerts.py
import smtplib

def send_alert(message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("your_email@gmail.com", "password")
    server.sendmail("your_email@gmail.com",
                    "receiver@gmail.com",
                    message)
    server.quit()