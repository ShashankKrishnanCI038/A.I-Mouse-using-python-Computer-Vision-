import cv2

CamWid, CamHei = 640, 480
ScanDisp = cv2.VideoCapture(0)
ScanDisp.set(3, CamWid)
ScanDisp.set(4, CamHei)

while True:
    success, Pic = ScanDisp.read()
    cv2.imshow("Image", Pic)
    cv2.waitKey(1)