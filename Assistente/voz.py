#fim da tarefa ||IA-10 do jira
#from winsound import PlaySound
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import requests
import playsound
import os
import subprocess

#engine = pyttsx3.init()
#engine.setProperty('voice', 'Brazil')
#engine.setProperty('rate', 178)
#engine.setProperty('volume', 1.)

# def assistente():


#def fala(text):
#    engine.say(text)
#    engine.runAndWait()

def fala(output):
    """função fala

    Args:
        output (string): pega o texto falado pelo microfone e converte em fala
    """
    num=0
    print(output)
    num+=1
    response=gTTS(text=output,lang='pt-BR')
    nomearquivo = str(num)+".mp3"
    response.save(nomearquivo)
    os.system("mpg123 " + nomearquivo)
    print(str(nomearquivo))
    os.remove(nomearquivo)


def get_audio():
    """get_audio

    Returns:
        dicionário: configura o microfone e escuta o usuário
    """
    input = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escutando...")
        input.adjust_for_ambient_noise(source, duration=0.5)
        input.pause_threshold = 1
        audio = input.listen(source, phrase_time_limit=5)
        query = ""
        try:
            escuta = input.recognize_google(audio, language='pt-BR')
            query = escuta.lower()
            if not 'tchau!' in query or 'pare' in query:
                fala(query)
                print(query)
            #engine.say("Frase dita por você é: " + Data)
        except sr.UnknownValueError:
            fala("Não entendi, pode repetir")
            return "None"
        return query

""" 
def Ola():
    fala("Olá! Tudo bem com você?")
    fala(" Vamos ser amigos?")
    return
 """

""" def responde(data):

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
    return """

if __name__=='__main__':
    """principal
    """
    fala("Olá! Tudo bem com você?")
    fala("Vamos ser amigos?")
    while 1:
        frase = get_audio().lower()
        if frase==0:
            continue
        if 'pare' in str(frase) or 'tchau' in str(frase) or 'até mais' in str(frase) or 'não' in str(frase):
            fala("Até mais tarde!")
            break
        if 'sim' in str(frase):
            fala("Primeiro, me diga seu nome?")
            continue
        if 'marcos' in str(frase) or 'rafael' in str(frase) or 'augusto' in str(frase) or 'sabrina' in str(frase):
            nome = frase
            fala("Agora me conte quantos anos você tem?")
            continue
        if '5 anos' in str(frase) or '6 anos' in str(frase):
            idade = frase
            fala("Que legal! Você quer fazer uma experiência comigo? Diga que vamos!")
            continue
        if 'vamos' in str(frase):
            fala("Então vamos lá: Primeiro, eu quero que você ande bem devagarzinho neste tapete, que se encontra aqui no chão.")
            break
        else:
            print("Primeiro, me diga seu nome?")
            print("Agora conte-me quantos anos você tem?")
            print("Que legal! Você quer fazer uma experiência comigo? Diga que vamos!")
            print("Então vamos lá: Primeiro, eu quero que você ande bem devagarzinho neste tapete, que se encontra aqui no chão.")
            break