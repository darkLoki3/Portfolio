# import pyttsx3
import requests

response = requests.get('https://httpbin.org/ip')

print('Seu IP é {0}'.format(response.json()['origin']))

# engine = pyttsx3.init()
# voices = engine.getProperty("voices")
#
# for voice in voices:
#     print(voice.id, voice.name, voice.languages)
