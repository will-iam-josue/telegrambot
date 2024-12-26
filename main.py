import telebot
from telebot import types

TOKEN = '7720106365:AAFpfu8g_TkcztUL9D5C8u3anKRvN0XPKcc'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hola Soy el bot de DRSP que se esta creando!!!...')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Se pueden usar comandos para interactuar conmigo, po ahora, solo /start pronto tendre mas funcionalidad')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


@bot.message_handler(commands=['busqueda'])



if __name__ == "__main__":
    bot.polling(non_stop=True)