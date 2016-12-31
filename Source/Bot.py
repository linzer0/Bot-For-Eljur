#-*- coding: utf-8 -*-
import telebot
import config
#import Main
import config
bot = telebot.TeleBot(config.token)
#bot.send_message(config.chat_id,"Test");
@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id,message.text)
bot.polling(none_stop=True,interval=0)