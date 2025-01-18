import config
import telebot
import time
import threading
import sqlite3
bot = telebot.TeleBot(config.BOT_TOKEN)

# === SQLIFE ======================================
db = sqlite3.connect('notebook.db')
cur = db.cursor()

# cur.execute('''CREATE TABLE user (
#         id INTEGER PRIMARY KEY,
#         chat_id INTEGER NOT NULL,
#         name TEXT DEFAULT 'Unknown',
#         role INTEGER DEFAULT 0,
#         delete INTEGER DEFAULT 0
#     )''')
# db.commit()

# === Functions ===================================
def send_text_message():
    while True:
        bot.send_message('998074865', 'Щось спрацювало')
        time.sleep(10)


# === Message-handlers ============================

@bot.message_handler(commands=['start'])
def bot_start(message):

    # TODO: контекст ...............
    cur.execute("SELECT chat_id FROM user")
    row = cur.fetchone()
    if not row:
        cur.execute(f"INSERT INTO user (chat_id, name) VALUES ({message.chat.id}, {message.from_user.username})")
        db.commit()

    bot.send_message(message.chat.id, f'Користувача [{message.from_user.username}]')


@bot.message_handler(content_types=['text'])
def text_message(message):
    # print(message.chat.id)
    bot.send_message(message.chat.id, 'Працює!')



if __name__ == '__main__':
    # thread = threading.Thread(target=send_text_message)
    # thread.start()
    bot.infinity_polling()