import os
import sys
from aiogram import Bot, types

def send_telegram_message(bot_token, chat_id):
    bot = Bot(token=bot_token)
    message_text = 'Привет, группа! Это сообщение от вашего бота из Github actions.'

    bot.send_message(chat_id, message_text, parse_mode=types.ParseMode.HTML, thread_id=9)

if __name__ == '__main__':
    bot_token = sys.argv[1]
    chat_id = sys.argv[2]

    send_telegram_message(bot_token, chat_id)
