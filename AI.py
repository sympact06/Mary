import pyttsx3
import wikipedia
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')
engine.setProperty('rate', 150)
import functions as func



def _ai_basic(data):
    func.containsword('hi', data, "Hi. I am Mary. Your virtual assistant.. I would like to help you! Please ask me a question! ")
    func.containsword('hello', data, "Hi. I am Mary. Your virtual assistant.. I would like to help you! Please ask me a question! ")
    func.containsword('yes', data, "Hi. I am Mary. Your virtual assistant.. I would like to help you! Please ask me a question! ")
    func.containsword('bye', data, "Ok. Bye then... ")
    func.containsword('goodbye', data, "Ok. Bye then... ")
    func.containsword('boomer', data, "No you are a boomer. Uno reverse mate..")
    func.containsword('life', data, "Life hurts")
    if 'Wikipedia' in data:
        _wikipedia(data)
        return
    return func.respond("You told me " + data + " But we cant reconize it. Please ask a other question or ask it again. Only English")


def _wikipedia(data):
    #to do convert data to string
    #to do remove the first word (wikipedia) from the string
    func.SearchWiki(data)
    exit(69)