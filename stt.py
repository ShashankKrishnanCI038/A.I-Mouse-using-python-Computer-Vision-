import speech_recognition as sr

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
    recorder = r.recognize_google(audio)

    if recorder == 'exit the program':
        exit()
    if recorder == 'hello':
        print('hello Boss. How can i help you ?')