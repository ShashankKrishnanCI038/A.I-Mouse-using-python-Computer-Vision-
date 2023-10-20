import speech_recognition as sr
import pyttsx3

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
    recorder = r.recognize_google(audio)

    if recorder == 'exit the program':
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[2].id)
        engine.setProperty("rate", 130)
        engine.say("exiting the program, See you soon, Byee ")
        engine.runAndWait()
        exit()
    if recorder == 'hello starah':
        print('hello Boss. How can i help you ?')
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[1].id)
        engine.setProperty("rate", 130)
        engine.say("hello Boss. How can i help you ?")
        engine.runAndWait()