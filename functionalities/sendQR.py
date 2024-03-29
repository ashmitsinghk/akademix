import smtplib
import imghdr
from email.message import EmailMessage


def sendQR(studentID, studentEmail):
    Sender_Email = "akademixrecords@gmail.com"
    Reciever_Email = studentEmail

    Password = "jbafgvdpehdpsldn"

    newMessage = EmailMessage()
    newMessage['Subject'] = "Your Attendance QR Code"
    newMessage['From'] = Sender_Email
    newMessage['To'] = Reciever_Email
    newMessage.set_content(' ')

    with open(f"./QR/QR_STUDENT_{studentID}.png", 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name

    newMessage.add_attachment(image_data, maintype='image',
                              subtype=image_type, filename=image_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Sender_Email, Password)
        smtp.send_message(newMessage)