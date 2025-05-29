import pyttsx3

def speak(text):
    if not text:
        return
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

