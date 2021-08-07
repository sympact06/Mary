import pyttsx3
import pyaudio
import wikipedia
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')
engine.setProperty('rate', 150)

def SearchWiki(data):
    respond(wikipedia.summary(data))

def respond(text):
    engine.say(text)
    engine.runAndWait()


def containsword(word, data, talkback):
    if word in data:
        respond(talkback)
        exit(69)