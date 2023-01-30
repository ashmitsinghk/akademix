import pyqrcode
import png

def generateQR(studentID):
    url = pyqrcode.create(studentID)
    url.png("./QR/QR_STUDENT_" + studentID + ".png", scale = 10)