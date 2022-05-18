# | fim da tarefa ||IA-10 do jira}}
import os
import subprocess

import speech_recognition as sr
from gtts import gTTS

from Assistente.rosto.rosto import Window
from Assistente.sensor import sensor

window = Window()


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
    window.falar()
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
        audio = mic.listen(source, phrase_time_limit=3)
        try:
            escuta = mic.recognize_google(audio, language='pt-BR')
            data = escuta.lower()
        except sr.UnknownValueError:
            fala("Não entendi, pode repetir")
            return "None"
        return data


if __name__ == '__main__':
    """principal
    """
    window.dorme()
    while sensor() <= 60.0:
        fala("Olá! Tudo bem com você?")
        fala("Vamos ser amigos?")
        frase = get_audio().lower()
        match frase:
            case 'pare' | 'tchau' | 'até mais' | 'não':
                fala("Até mais tarde!")
                break
            case 'sim':
                fala("Primeiro, me diga seu nome?")
                window.pisca()
                continue
            case 'marcos' | 'rafael' | 'augusto' | 'sabrina' | 'alexandra':
                fala("Agora me conte quantos anos você tem?")
                window.olhos()
                continue
            case '5 anos' | '6 anos' | '7 anos' | '8 anos' | '9 anos':
                fala("Que legal! Você quer fazer uma experiência comigo? Diga que vamos!")
                window.choque()
                continue
            case 'vamos':
                fala("Então vamos lá:")
                fala("Primeiro, eu quero que você ande bem devagarzinho neste tapete, que se encontra aqui no chão.")
                window.pisca()
                break
