import logging
import types

from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import FSInputFile
from aiogram.types import Message

import config
from inline_but import *
from routers import start_db, check_us

import sqlite3 as sq

import asyncio
router = Router()
bot = Bot(config.token[0])


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

