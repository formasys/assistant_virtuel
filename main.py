import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import datetime

listener=sr.Recognizer()
engine=ttx.init()
voice=engine.getProperty('voices')
engine.setProperty('voice','french')

def parler(text):
    engine.say(text)
    engine.runAndWait()

def ecouter():
    try:
        with sr.Microphone() as source:
            print("parlez maintenant")
            voix=listener.listen(source)
            command=listener.recognize_google(voix,language='fr-FR')
            command.lower()
    except:
        pass
    return command

def lancer_assistant():
    command=ecouter()
    print(command)
    if 'mets la chanson de' in command:
        chanteur=command.replace('mets la chanson de','')
        print(chanteur)
        pywhatkit.playonyt(chanteur)
    elif 'heure' in command:
        heure=datetime.datetime.now().strftime('%H:%M')
        parler('il est'+heure)
    elif 'Bonjour' in command:
        parler('bonjour,ca va?')
    else:
        print('je ne comprends pas')


while True:
    lancer_assistant()