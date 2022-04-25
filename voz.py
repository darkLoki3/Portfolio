import speech_recognition as sr
import pyttsx3
from gtts import gTTS
from playsound import playsound
import os

#engine = pyttsx3.init()
#engine.setProperty('voice', 'Brazil')
#engine.setProperty('rate', 178)
#engine.setProperty('volume', 1.)

# def assistente():


#def fala(text):
#    engine.say(text)
#    engine.runAndWait()

def fala(text):
    tts = gTTS(text=text, lang='pt-BR')
    nomearquivo = "/home/pi/Documentos/mypython/Python/voice.mp3"
    tts.save(nomearquivo)
    playsound(nomearquivo)


def get_audio():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        print(".")
        mic.adjust_for_ambient_noise(source, duration=0.5)
        mic.pause_threshold = 1
        Audio = mic.listen(source, phrase_time_limit=5)
        Data = ""
        try:
            escuta = mic.recognize_google(Audio, language='pt-BR')
            Data = escuta.lower()
            if not 'Tchau!' in Data or 'Pare' in Data:
                fala(Data)
            #engine.say("Frase dita por você é: " + Data)
        except sr.UnknownValueError:
            fala("Não entendi, pode repetir")
            return "None"
        return Data


def Ola():
    fala("Olá! Tudo bem com você?")
    fala(" Vamos ser amigos?")
    return


def responde(data):

    ouvindo = True
    Ola()
    data = get_audio().lower()
    if 'sim' in data:
            fala("Primeiro, me diga qual o seu nome?")
            data = get_audio().lower()
    elif 'Marcos' in data or 'Raphael' in data or 'Augusto' in data or 'Sérgio' in data or 'Sabrina' in data or 'Amanda' in data or 'Gabriela' in data:
            fala("Agora me conte quantos anos você tem?")
            data = get_audio().lower()
    elif '2 anos' or '3 anos' or '4 anos' or '5 anos' or '6 anos' or '7 anos' in data:
            fala("Que legal! você quer fazer uma expericia comigo?")
            data = get_audio().lower()
    elif 'vamos' in data:
            fala("Então vamos lá: Primeiro, eu quero que você ande bem devargarzinho neste tapete que se encontra aqui no chão.")
            data = get_audio().lower()

    # elif nome in data:
    #    escutando
    return

Ola()
frase = get_audio()
responde(frase)