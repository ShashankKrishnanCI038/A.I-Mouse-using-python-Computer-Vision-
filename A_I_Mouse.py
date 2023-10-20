import cv2
import keyboard
import numpy as np
import TraceHand as thp
import time
import autopy
import pyautogui
import pyttsx3
import speech_recognition as sr
###############################################.VARIABLES.##############################################################
CamWid, CamHei = 640, 480
frRed = 170
Smooth = 25
ScanDisp = cv2.VideoCapture(0)
ScanDisp.set(3, CamWid)
ScanDisp.set(4, CamHei)
PrevTime = 0
PrevLocX, PrevLocY = 0, 0
CurrLocX, CurrLocY = 0, 0
Finder = thp.DetectHand(maxiHands=1)
ScrW, ScrH = autopy.screen.size()
######################################################.EXECUTION.#######################################################
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
    recorder = r.recognize_google(audio)
    if recorder == 'terminate the program':
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[1].id)
        engine.setProperty("rate", 130)
        engine.say("A I Mouse program is switching off")
        print("A I Mouse program is switching off")
        engine.runAndWait()
        exit()
    if recorder == 'hello bot':
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[1].id)
        engine.setProperty("rate", 130)
        engine.say("Artificial Intelligence Virtual Mouse powering ON ")
        print("Artificial Intelligence Virtual Mouse powering ON")
        engine.runAndWait()
        print("\n")
        print("Type 'o' to turn off: ")
    ########################################################################################################################
        while True:

            if keyboard.is_pressed("o"):
                engine = pyttsx3.init()
                voices = engine.getProperty("voices")
                engine.setProperty("voice", voices[1].id)
                engine.setProperty("rate", 130)
                engine.say("A I Mouse turned off")
                engine.runAndWait()
                break

            # 1. Find hand gesture marks points
            success, Pic = ScanDisp.read()
            Pic = Finder.findHands(Pic)
            ListSet, box = Finder.findPos(Pic)

            # 2. verify tip of the index and middle fingers
            if len(ListSet) != 0:
                x1, y1 = ListSet[8][1:]
                x2, y2 = ListSet[12][1:]

                # 3. Check the fingers
                Fingers = Finder.fingersUp()
                # print(fingers)
                cv2.rectangle(Pic, (frRed, frRed), (CamWid - frRed, CamHei - frRed),
                              (255, 0, 255), 2)

                # 4.Index Finger up = Moving the mouse cursor
                if Fingers[1] == 1 and Fingers[2] == 0:
                    # 5. Convert Coordinates
                    x3 = np.interp(x1, (frRed, CamWid - frRed), (0, ScrW))
                    y3 = np.interp(y1, (frRed, CamHei - frRed), (0, ScrH))

                    # 6. Smoothe the movement of mouse
                    CurrLocX = PrevLocX + (x3 - PrevLocX) / Smooth
                    CurrLocY = PrevLocY + (y3 - PrevLocY) / Smooth
    ##############################################.MOUSE_OPERATIONS.########################################################
                    # 7. Move Mouse
                    autopy.mouse.move(ScrW - CurrLocX, CurrLocY)
                    cv2.circle(Pic, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                    PrevLocX, PrevLocY = CurrLocX, CurrLocY
    ##########################################.Operations.##################################################################
                if Fingers[0] == 0 and Fingers[1] == 1 and Fingers[2] == 1 and Fingers[3] == 0 and Fingers[4] == 0:
                    LSize, Pic, _ = Finder.findDistance(8, 12, Pic)
                    if LSize < 50:
                        cv2.circle(Pic, (x1, y1), 15, (0, 255, 0), cv2.FILLED)
                        pyautogui.leftClick()
                        time.sleep(0.1)

                if Fingers[0] == 0 and Fingers[1] == 1 and Fingers[2] == 1 and Fingers[3] == 1 and Fingers[4] == 0:
                    pyautogui.rightClick()
                    time.sleep(0.5)

                if Fingers[0] == 1 and Fingers[1] == 1 and Fingers[2] == 1 and Fingers[3] == 1 and Fingers[4] == 1:
                    pyautogui.scroll(150)

                if Fingers[0] == 0 and Fingers[1] == 1 and Fingers[2] == 1 and Fingers[3] == 1 and Fingers[4] == 1:
                    pyautogui.scroll(-150)

                if Fingers[0] == 0 and Fingers[1] == 1 and Fingers[2] == 0 and Fingers[3] == 0 and Fingers[4] == 1:
                    mw, mh = pyautogui.position()
                    pyautogui.mouseDown(mw, mh)

                if Fingers[0] == 1 and Fingers[1] == 0 and Fingers[2] == 0 and Fingers[3] == 0 and Fingers[4] == 0:
                    pyautogui.press('win')
                    time.sleep(0.5)

                if Fingers[0] == 1 and Fingers[1] == 1 and Fingers[2] == 1 and Fingers[3] == 0 and Fingers[4] == 0:
                    pyautogui.hotkey('ctrl', 'x')
                    time.sleep(0.7)

                if Fingers[0] == 1 and Fingers[1] == 1 and Fingers[2] == 0 and Fingers[3] == 0 and Fingers[4] == 0:
                    pyautogui.hotkey('ctrl', 'c')
                    time.sleep(0.7)

                if Fingers[0] == 1 and Fingers[1] == 0 and Fingers[2] == 0 and Fingers[3] == 0 and Fingers[4] == 1:
                    pyautogui.hotkey('ctrl', 'v')
                    time.sleep(0.7)

                if Fingers[0] == 0 and Fingers[1] == 0 and Fingers[2] == 0 and Fingers[3] == 0 and Fingers[4] == 1:
                    pyautogui.hotkey('ctrl', 'z')
                    time.sleep(0.5)
            # 11.Frame
            CurrTime = time.time()
            FrPerSec = 1 / (CurrTime - PrevTime)
            PrevTime = CurrTime
            cv2.putText(Pic, str(int(FrPerSec)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
            # 12.Display
            cv2.imshow("Image", Pic)
            cv2.waitKey(1)