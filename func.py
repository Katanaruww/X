import logging
import types

from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import FSInputFile
from aiogram.types import Message
from translate import _
import config
from inline_but import *
from routers import start_db, check_us, check_lang, db_rep_lang

import sqlite3 as sq

import asyncio
router = Router()
bot = Bot(config.token[0])
logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                        format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s", encoding="UTF-8")

def sql_start():
    global base, cur
    base = sq.connect('users_bd.bd')
    cur = base.cursor()
    if base:
        print(f"Database connect OK")
    base.execute('CREATE TABLE IF NOT EXISTS users_id(id INTEGER PRIMARY KEY)')
    base.commit()


async def send_broadcast(message_text, photo_url):
    cur.execute('SELECT id FROM users_id')
    users = cur.fetchall()
    for user in users:
        try:
            await bot.send_photo(user[0], photo=photo_url, caption=message_text)
        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю {user[0]}: {e}")


async def send_broadcast2(text):
    cur.execute('SELECT id FROM users_id')
    users = cur.fetchall()
    for user in users:
        try:
            await bot.send_message(user[0], text=text)

        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю {user[0]}: {e}")

async def get_user_value(val_1):
    cur.execute("INSERT OR IGNORE INTO users_id (id) VALUES (?)", (val_1,))
    base.commit()

async def replace_language(call):
    try:
        print(call.data[7:])
        lang = call.data[7:]
        if lang == "RU":
            lang_db = "EN"
        else:
            lang_db = "RU"
        await db_rep_lang(call.message.chat.id, lang_db)

        try:
            photo = FSInputFile("media/x.jpg")
            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            await call.message.answer_photo(caption=f"{_('Настройки', lang)}",
                                            reply_markup=setting_btn(call, lang_db).as_markup(), photo=photo)
        except Exception as e:
            logging.error(f"Ошибка при редактировании сообщения: {e}")
    except Exception as e:
        logging.exception(e)

