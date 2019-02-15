from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import os

app = Flask(__name__)

# english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("chatterbot.corpus.english")

bot.set_trainer(ListTrainer)
for _file in os.listdir('traindata'):
   conversations = open('traindata/' + _file, 'r').readlines()
   bot.train(conversations)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    # return str(english_bot.get_response(userText))
    s = bot.get_response(userText)
    if s.confidence > 0.7:
       return 'helpdesk_bot:  '+ str(bot.get_response(userText))
    else:
        return "helpdesk_bot:  Please contact IT staff to help"

if __name__ == "__main__":
    app.run()