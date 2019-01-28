# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#create a name for the bot
bot = ChatBot('Halo')

#Train the bot with base statement

data = open('chatbotdata.txt').read()
conversations = data.strip().split('\n')

bot.set_trainer(ListTrainer)
bot.train(conversations)
#provide the question and chatbot answer
while True:
   try:
      s=input('I')
      print('Steven:'+s+'')
      response = bot.get_response(s)
      print('HelpDesk:'+str(response))
   except (KeyboardInterrupt, EOFError, SystemExit):
      break



