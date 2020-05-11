#! /usr/bin/env python
# -*- coding: utf-8 -*-

import telebot

bot = telebot.TeleBot('1076763292:AAE6xteIV1gqIfv3x27Ed5sIAYTraglvXDE')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "4 lab":
        bot.send_message(message.from_user.id, "net")
    elif message.text == "sho":
        bot.send_message(message.from_user.id, "kavo")

    elif message.text == "1":
        bot.send_message(message.from_user.id, "alo")
    else:
        bot.send_message(message.from_user.id, "7 days on this laba")

bot.polling(none_stop=True, interval=2) 