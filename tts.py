import pyttsx3
n = 0
while n < 3:
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.setProperty("rate", 130)
    engine.say("This is the text to speech testing program.Speaking"+ str(n) +"time")
    engine.runAndWait()
    n=n+1