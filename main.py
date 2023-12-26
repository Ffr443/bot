import telebot

bot = telebot.Telebot('6428217862:AAG2q-SlY8t7t32ZmbN7RcXG-gGq98yrmlw')

@message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id, 'hello world')

bot.infinity_polling()
