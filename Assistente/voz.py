# fim da tarefa ||IA-10 do jira
import speech_recognition as sr
from gtts import gTTS
import requests
import os
import subprocess


# engine = pyttsx3.init()
# engine.setProperty('voice', 'Brazil')
# engine.setProperty('rate', 178)
# engine.setProperty('volume', 1.)

def fala(resultado):
    """função fala

    Args:
        resultado (string): pega o texto falado pelo microfone e converte em fala
    """
    num = 0
    print(resultado)
    num += 1
    response = gTTS(text=resultado, lang='pt-BR')
    nomearquivo = str(num) + ".mp3"
    response.save(nomearquivo)
    subprocess.call("mpg123 " + nomearquivo, shell=False)
    print(str(nomearquivo))
    os.remove(nomearquivo)


def get_audio():
    """get_audio

    Returns:
        dicionário: configura o microfone e escuta o usuário
    """
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escutando...")
        mic.adjust_for_ambient_noise(source, duration=0.5)
        mic.pause_threshold = 1
        audio = mic.listen(source, phrase_time_limit=5)
        try:
            escuta = mic.recognize_google(audio, language='pt-BR')
            query = escuta.lower()
        except sr.UnknownValueError:
            fala("Não entendi, pode repetir")
            return "None"
        return query


if __name__ == '__main__':
    """principal
    """
    fala("Olá! Tudo bem com você?")
    fala("Vamos ser amigos?")
    while 1:
        frase = get_audio().lower()
        if frase == 0:
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
            idade = frase.split(" anos")
            fala("Que legal! Você quer fazer uma experiência comigo? Diga que vamos!")
            continue
        if 'vamos' in str(frase):
            fala("Então vamos lá:")
            fala("Primeiro, eu quero que você ande bem devagarzinho neste tapete, que se encontra aqui no chão.")
            break
        else:
            print("Primeiro, me diga seu nome?")
            print("Agora conte-me quantos anos você tem?")
            print("Que legal! Você quer fazer uma experiência comigo? Diga que vamos!")
            print("Então vamos lá:")
            print("Primeiro, eu quero que você ande bem devagarzinho neste tapete, que se encontra aqui no chão.")
            break
