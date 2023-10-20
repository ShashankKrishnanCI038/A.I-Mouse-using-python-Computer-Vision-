import cv2
import speech_recognition as sr
import pyttsx3

CamWid, CamHei = 640, 480
ScanDisp = cv2.VideoCapture(0)
ScanDisp.set(3, CamWid)
ScanDisp.set(4, CamHei)
#----------------------------------------------------------------------------------------------------------------------#
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
    recorder = r.recognize_google(audio)

    if recorder == 'switch off':
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[2].id)
        engine.setProperty("rate", 130)
        engine.say("camera is switching off, See you soon, Byee ")
        engine.runAndWait()
        exit()
    if recorder == 'on the camera':
        print('CAMERA IS ON!')
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[2].id)
        engine.setProperty("rate", 130)
        engine.say("camera turned on")
        engine.runAndWait()
        while True:
            success, Pic = ScanDisp.read()
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Speak:")
                audio = r.listen(source)
            recorder = r.recognize_google(audio)
            if recorder == 'packet':
                engine = pyttsx3.init()
                voices = engine.getProperty("voices")
                engine.setProperty("voice", voices[2].id)
                engine.setProperty("rate", 130)
                engine.say("camera turned off")
                engine.runAndWait()
                break

            cv2.imshow("Image", Pic)
            cv2.waitKey(1)
