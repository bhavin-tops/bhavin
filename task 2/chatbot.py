from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

trainer.train([
    'Hi',
    'Hello',
    'I need your assistance regarding my order',
    'Please, Provide me with your order id',
    'I have a complaint.',
    'Please elaborate, your concern',
    'How long it will take to receive an order ?',
    'An order takes 3-5 Business days to get delivered.',
    'Okay Thanks',
    'No Problem! Have a Good Day!'
])

response = bot.get_response('I have a complaint.')

print("Bot Response:", response)

from gtts import gTTS
import os

def text_to_speech(text):
    speaker = gTTS(text=text, lang="en", slow=False)
    speaker.save("res.mp3")
    os.system("start res.mp3")  
    os.remove("res.mp3")

bot = ChatBot(
    'Buddy',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
         print("listening...")
         audio = recognizer.listen(mic)
    try:
         text = recognizer.recognize_google(audio)
         print("me --> ", text)
    except:
         print("me -->  ERROR")

name=input("Enter Your Name: ")
print("Welcome to the Bot Service! Let me know how can I help you?")
while True:
    request=input(name+':')
    if request=='Bye' or request =='bye':
        print('Bot: Bye')
        break
    else:
        response=bot.get_response(request)
        print('Bot:',response)

