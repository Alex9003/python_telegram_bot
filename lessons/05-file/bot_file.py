import telebot


token = '7528021097:AAEo3NfNANiqOsSHjRZ1udZRbWfhHi--Zm0'
bot = telebot.TeleBot(token)
# file_text = "bot_text.txt"
# file_number = "bot_text.txt"
def f1(v):
    try:
        int(v)
        return True
    except ValueError:
        return False


# --- Message -------------------------
@bot.message_handler(content_types=['text'])
def is_text(message):
    if not f1(message.text):
        filename = "bot_text.txt"
    else:
        filename = "bot_number.txt"

    with open(filename, 'a') as file:
        file.write(message.text + '\n')


    bot.send_message(message.chat.id, 'Збережено до файла!')


if __name__ == '__main__':
    bot.polling()