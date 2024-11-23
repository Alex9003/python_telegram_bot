import telebot

token = '7528021097:AAEo3NfNANiqOsSHjRZ1udZRbWfhHi--Zm0'
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def test_text(message):
    print(message)

    msg = message.text + ' - this is a text message'
    bot.send_message(message.chat.id, msg)


if __name__ == '__main__':
    bot.polling()

