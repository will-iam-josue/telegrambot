import telebot
import logging
from telebot import types
from flask import Flask, render_template

TOKEN = '7720106365:AAFpfu8g_TkcztUL9D5C8u3anKRvN0XPKcc'

bot = telebot.TeleBot(TOKEN)

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hola Soy el bot de DRSP que se esta creando!!!...')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Se pueden usar comandos para interactuar conmigo, po ahora, solo /start pronto tendre mas funcionalidad')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


@app.route("/")
def home():
    bot.polling(non_stop=True)
    return render_template('home.html',)

#@bot.message_handler(commands=['busqueda'])
#def send_search(message):

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)