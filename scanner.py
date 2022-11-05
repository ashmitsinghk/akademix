import cv2
import numpy as np
from pyzbar.pyzbar import decode
import time
from threading import Timer
import os, subprocess
import markAttendance, akademix


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
    # i = 0
    # while i < 10:
    #     print("processing code for " + str(i) + " seconds")
    #     i += 1
    #     time.sleep(1)
    print(str(barcodeData) + " is processed")
    markAttendance.markAttendance(str(barcodeData))
    subprocess.Popen(['python', 'akademix.py'])
    os._exit(0)()



def time_out_exit() :
    print("No QR Code Found")
    subprocess.Popen(['python', 'akademix.py'])
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

if __name__ == '__main__':
    open_scanner()