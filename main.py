import telebot

bot = telebot.TeleBot('1076763292:AAE6xteIV1gqIfv3x27Ed5sIAYTraglvXDE')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Лаба 4 починилась?":
        bot.send_message(message.from_user.id, "Нет, перезапускай знов шарманку")
    elif message.text == "А зараз?":
        bot.send_message(message.from_user.id, "нет")
    else:
        bot.send_message(message.from_user.id, "та перезапусти")

bot.polling(none_stop=True, interval=2)