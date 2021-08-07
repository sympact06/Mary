import pyttsx3
import pyaudio
import speech_recognition as sr
import AI as ai
import functions as func
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')
engine.setProperty('rate', 160)


def talk():
    input = sr.Recognizer()
    with sr.Microphone() as source:
        audio = input.listen(source)
        data = ""
        try:
            data = input.recognize_google(audio)
            print(data)

            ai._ai_basic(data)


        except sr.UnknownValueError:
            func.respond("Sorry I did not hear your question, Please repeat again.")

        return talk()


talk()




