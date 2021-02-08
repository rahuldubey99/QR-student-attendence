import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys
import time
import pybase64
#start webcam
cap = cv2.VideoCapture(0)
name =[]
# function for attendence file
fob = open('attendence.txt','a+')
def enterdata(z):
    if z in names:
        pass
    else:
        names.append(z)
        z = ''.join(str(z))
        fob.write(z+'\n')
        return names
print('Reading code ...............')

#function data present or not
def checkData(data):
    data = str(data)
    if data in names:
        print('Already')
    else:
        print('\n'+str(len(names)+1)+'\n'+'Present Done')
        enterdata(data)
while True:
    _,frame = cap.read()
    decodedObject = pyzbar.decoded(frame)
    for obj in decodedobject:
        checkData(obj.data)
        time.sleep(1)
    cv2.imshow('frame',frame)

    #close
    if cv2.waitKey(1)& 0xFF ==ord('s'):
        cv2.destroyAllWindows()
        break
fob.close()