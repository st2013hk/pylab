# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
from chatterbot.trainers import ChatterBotCorpusTrainer
#create a name for the bot
bot = ChatBot('Halo')

#Train the bot with base statement

# data = open('printerdata.txt').read()
# conversations = data.strip().split('\n')
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("chatterbot.corpus.english")
bot.set_trainer(ListTrainer)
for _file in os.listdir('traindata'):
   conversations = open('traindata/' + _file, 'r').readlines()
   bot.train(conversations)
#provide the question and chatbot answer
while True:
   try:
      s=input("You: ")
      response = bot.get_response(s)
      if response.confidence > 0.7:
         print("HelpDesk_bot:",response)
      else:
         print("I have no idea. Please contact IT staff to help")
   except (KeyboardInterrupt, SystemExit):
      print('goodbye!')
      break



