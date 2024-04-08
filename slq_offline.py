import sqlite3

import logging

from aiogram import Router, Bot

import config

conn = sqlite3.connect(config.name_db[0], check_same_thread=False)
curs = conn.cursor()
logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s", encoding="UTF-8")


router = Router()
bot = Bot(config.token[0])



