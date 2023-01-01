import cv2
import numpy as np
from pyzbar.pyzbar import decode
from threading import Timer
import os, subprocess
from functionalities import markAttendance


def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    barcode = decode(gray_img)
    for obj in barcode:           
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))        
        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        process_code(barcodeData)

def process_code(barcodeData):
    print("cancel timer")
    Timer(10.0, time_out_exit).cancel()
    print(str(barcodeData) + " is processed")
    markAttendance.markAttendance(str(barcodeData))
    subprocess.Popen(['python', './main.py'], shell=True)
    os._exit(0)()



def time_out_exit() :
    print("No QR Code Found")
    subprocess.Popen(['python', './main.py'], shell=True)
    os._exit(0)()

def open_scanner():
    Timer(10.0, time_out_exit).start()
    #add cv2.CAP_DSHOW on windows while developing, remove on RBPI
    cap = cv2.VideoCapture(0 , cv2.CAP_DSHOW)
    #cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        decoder(frame)
        cv2.imshow('AKADEMIX ATTENDANCE SCANNER', frame)
        code = cv2.waitKey(1)
        if code == ord('q'):
            exit()
