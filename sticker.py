import telebot
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

token = '7528021097:AAEo3NfNANiqOsSHjRZ1udZRbWfhHi--Zm0'
bot = telebot.TeleBot(token)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"

db = SQLAlchemy(app)

class Base(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test = db.Column(db.String(), nullable=False)


@app.route('/')
def index():
    mes = Base.query.all()
    return render_template('index.html', mes=mes)


sticker_list = [
    'CAACAgIAAxkBAAOjZ1Qm11vs58CmTX1LG6juqeoV5-YAAgFWAAJZ7olIfuE3QeAgZRI2BA',
    'CAACAgIAAxkBAAOsZ1Qm89MrVK5m2xJsraSc66345fsAAq8yAAIZGhhJx27mTyu4f6I2BA',
    'CAACAgIAAxkBAAOzZ1QnRMigODhWEoi4jMqtRQNcQ68AArVbAAI7SoFIX1hrr3x0uJM2BA',
    'CAACAgIAAxkBAAO1Z1QnRELvBMhsakSUxTcKIQ3ZRk0AAqFUAAK15YhIgfWcyajA9zA2BA',
    'CAACAgIAAxkBAAPLZ1QqG0r-xsivsH_3vCiT6RCrJlkAAglZAAKkC4hI1kQQBG9dIyA2BA'
]

@bot.message_handler(content_types = ['sticker'])
def handler_sticker(message):
    id = message.sticker.file_id
    em = message.sticker.emoji
    text = f"ІД стікера = ({id}). Емоджі: ({em})"
    bot.reply_to(message, text)

@bot.message_handler(commands=['f'])
def handler_f(message):
    current_path_app = os.path.abspath(__file__)
    current_path = os.path.dirname(current_path_app)
    my_file = os.path.join(current_path, 'dog.webm')

    with open(my_file, 'rb') as sticker:
        bot.send_sticker(message.chat.id, sticker)

@bot.message_handler(content_types = ['text'])
def is_text(message):

    if message.text == 'a':
        bot.send_sticker(message.chat.id, sticker_list[0])
        return True
    elif message.text == 'b':
        bot.send_sticker(message.chat.id, sticker_list[1])
        return True
    elif message.text == 'c':
        bot.send_sticker(message.chat.id, sticker_list[2])
        return True
    elif message.text == 'd':
        bot.send_sticker(message.chat.id, sticker_list[3])
        return True

    elif message.text == 'e':
        bot.send_sticker(message.chat.id, sticker_list[4])
        return True
    bot.send_message(message.chat.id, 'Текст')

if __name__ == '__main__':
    bot.infinity_polling()