#Samuel Juarez = Spam Email Project

import smtplib, ssl

def sendEmail(message):
    smtp_server = "smtp.gmail.com"
    port = 587
    aender_email = "the sender's email"
    password = "passwordiscool"
    receiver_email = "receiver email"

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendemail(sender_email, receiver_email, message)

    except Exception as e:
        print(e)
        finally:
            server.quit()

sendEmail("Hello how was your day my dear lad")