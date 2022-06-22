# | fim da tarefa ||IA-10 do jira}}
import pyttsx3
import speech_recognition as sr

# from Assistente.rosto.rosto import Window
# from Assistente.sensor import sensor

engine = pyttsx3.init()

pt_br_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\Ricardo RSI Harpo 22kHz"

engine.setProperty('voice', pt_br_voice_id)
engine.setProperty('volume', 1.)
engine.setProperty('rate', 140)
engine.runAndWait()


def get_audio():
    """get_audio():
    Returns:
        Retorna o audio dito no microfone"""
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        # engine.say("Estou ouvindo")
        # engine.runAndWait()
        mic.adjust_for_ambient_noise(source, duration = 0.5)
        mic.pause_threshold = 1
        audio = mic.listen(source, phrase_time_limit = 3)
        try:
            escuta = mic.recognize_google(audio, language = 'pt-BR')
            data = escuta.lower()
        except sr.UnknownValueError:
            engine.say("Não entendi, pode repetir?")
            engine.runAndWait()
            return "None"
        return data


if __name__ == '__main__':
    # principal
    # window.dorme()
    # nomes = {}
    # nome = ['Miguel', 'Davi', 'Gabriel', 'Arthur', 'Lucas', 'Matheus', 'Pedro', 'Guilherme', 'Gustavo',
    #         'Rafael', 'Felipe', 'Bernardo', 'Enzo', 'Nicolas', 'João Pedro', 'Pedro Henrique', 'Cauã',
    #         'Vitor', 'Eduardo', 'Daniel', 'Henrique', 'Murilo', 'Vinicius', 'Samuel', 'Pietro',
    #         'João Vitor', 'Leonardo', 'Caio', 'Heitor', 'Lorenzo', 'Isaac', 'Lucca', 'Thiago',
    #         'João Gabriel', 'João', 'Theo', 'Bruno', 'Bryan', 'Carlos Eduardo', 'Luiz Felipe', 'Breno',
    #         'Emanuel', 'Ryan', 'Vitor Hugo', 'Yuri', 'Benjamin', 'Erick', 'Enzo Gabriel', 'Fernando',
    #         'Joaquim', 'André', 'Tomás', 'Francisco', 'Rodrigo', 'Igor', 'Antonio', 'Ian', 'Luiz Otávio',
    #         'Juan', 'João Guilherme', 'Diogo', 'Otávio', 'Nathan', 'Calebe', 'Danilo', 'Luan',
    #         'Luiz Henrique', 'Kaique', 'Alexandre', 'João Miguel', 'Iago', 'Ricardo', 'Raul', 'Marcelo',
    #         'Julio César', 'Cauê', 'Benício', 'Vitor Gabriel', 'Augusto', 'Pedro Lucas', 'Luiz Gustavo',
    #         'Giovanni', 'Renato', 'Diego', 'João Paulo', 'Renan', 'Luiz Fernando', 'Anthony',
    #         'Lucas Gabriel', 'Thales', 'Luiz Miguel', 'Henry', 'Marcos Vinicius', 'Kevin', 'Levi',
    #         'Enrico', 'João Lucas', 'Hugo', 'Luiz Guilherme', 'Matheus Henrique', 'Julia', 'Sophia',
    #         'Isabella', 'Maria Eduarda', 'Manuela', 'Giovanna', 'Alice', 'Laura', 'Luiza', 'Beatriz',
    #         'Mariana', 'Yasmin', 'Gabriela', 'Rafaela', 'Maria Clara', 'Maria Luiza', 'Ana Clara',
    #         'Isabelle', 'Lara', 'Ana Luiza', 'Letícia', 'Ana Julia', 'Valentina', 'Nicole', 'Sarah',
    #         'Vitória', 'Isadora', 'Lívia', 'Helena', 'Ana Beatriz', 'Lorena', 'Clara', 'Larissa',
    #         'Emanuelly', 'Heloisa', 'Marina', 'Melissa', 'Gabrielly', 'Eduarda', 'Maria Fernanda',
    #         'Rebeca', 'Amanda', 'Alícia', 'Bianca', 'Lavínia', 'Fernanda', 'Ester', 'Carolina', 'Emily',
    #         'Cecília', 'Maria Júlia', 'Pietra', 'Ana Carolina', 'Milena', 'Marcela', 'Laís', 'Natália',
    #         'Maria', 'Bruna', 'Camila', 'Luana', 'Ana Laura', 'Catarina', 'Maria Vitória', 'Maria Alice',
    #         'Olivia', 'Agatha', 'Mirella', 'Sophie', 'Stella', 'Stefany', 'Isabel', 'Kamilly', 'Elisa',
    #         'Luna', 'Eloá', 'Joana', 'Mariane', 'Bárbara', 'Juliana', 'Rayssa', 'Alana', 'Ana Sophia',
    #         'Ana Lívia', 'Caroline', 'Brenda', 'Evelyn', 'Débora', 'Raquel', 'Maitê', 'Ana', 'Nina',
    #         'Maria Sophia', 'Maria Cecília', 'Luiz', 'Antonella', 'Jennifer', 'Betina', 'Mariah',
    #         'Sabrina', 'Maurício', 'Antenor', 'Juliano', 'Sérgio', 'Breno', 'Fábio', 'Sílvio', 'Kléber', 'José',]
    # idades = {'idade': = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90}
    engine.say("Oi, eu sou o Doutor Kids, fui criado para te ajudar a escolher a palmilha ideal para seu pezinho")
    engine.say("Diga o seu nome?")
    engine.runAndWait()
    frase = get_audio()

    while True:
        if frase == 0:
            continue
        if 'rudinei' in str(frase) or 'tetsuo' in str(frase) or 'felipe' in str(frase) or 'sabrina' in str(
                frase) or 'adriana' in str(frase):
            engine.say("Quantos anos você tem?")
            engine.runAndWait()
            frase = get_audio()
            # window.olhos()
            # window.pisca()
            # window.choque()
            continue
        if '6' in str(frase) or '7' in str(frase) or '8' in str(frase) or '9' in str(frase):
            engine.say("Você quer fazer uma experiência comigo?")
            engine.say("Diga Sim ou Não.")
            engine.runAndWait()
            frase = get_audio()
            continue
        if 'sim' in str(frase):
            engine.say("Então vamos lá,")
            engine.say("ande bem naturalmente sobre o tapete iluminado que está ao lado,")
            engine.say("seguindo as instruções do nosso pessoal.")
            engine.say("Obrigado pela participação.")
            engine.say("A kidy está sempre preocupada em desenvolver o melhor calçado para as crianças")
            engine.runAndWait()
            break
        if 'não' in str(frase):
            engine.say("Aaaaahh... que pena, fica para próxima então!")
            engine.say("Obrigado.")
            engine.say("A kidy está sempre preocupada em desenvolver o melhor calçado para as crianças.")
            engine.runAndWait()
            break
