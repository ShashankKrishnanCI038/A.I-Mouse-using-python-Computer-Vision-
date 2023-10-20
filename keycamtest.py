import cv2
import keyboard

CamWid, CamHei = 640, 480
ScanDisp = cv2.VideoCapture(0)
ScanDisp.set(3, CamWid)
ScanDisp.set(4, CamHei)
#----------------------------------------------------------------------------------------------------------------------#
while True:
    if keyboard.is_pressed('0'):
        exit()
    if keyboard.is_pressed('1'):
        while True:
            success, Pic = ScanDisp.read()
            if keyboard.is_pressed('2'):
                break
            cv2.imshow("Image", Pic)
            cv2.waitKey(1)


