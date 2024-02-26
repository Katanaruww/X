import logging
import sqlite3 as sq

from aiogram import Router, Bot
from aiogram.types import FSInputFile
from aiogram import types
import config
from inline_but import *
from routers import check_lang, db_rep_lang, db_add_start_deals, db_delete_deal
from translate import _
from inline_but import setting_rasilka, crypto_valets
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
    base.execute('''
        CREATE TABLE IF NOT EXISTS offline_exchange(
            id_num INTEGER PRIMARY KEY AUTOINCREMENT,
            id INTEGER PRIMARY KEY,
            user_name TEXT,
            deal TEXT,
            current TEXT,
            1)C INTEGER,
            2)C INTEGER
        )
        ''')
    base.commit()

"""РАССЫЛКА"""
async def send_broadcast(message_text, photo_url):
    cur.execute('SELECT id FROM users_id')
    users = cur.fetchall()
    for user in users:
        try:
            lang = await check_lang(user[0])
            await bot.send_photo(user[0], photo=photo_url, caption=message_text, reply_markup=setting_rasilka(lang).as_markup())
        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю {user[0]}: {e}")


async def send_broadcast2(text):
    cur.execute('SELECT id FROM users_id')
    users = cur.fetchall()
    for user in users:
        # try:
            lang = await check_lang(user[0])
            await bot.send_message(user[0], text=text, reply_markup=setting_rasilka(lang).as_markup())

        # except Exception as e:
        #     print(f"Не удалось отправить сообщение пользователю {user[0]}: {e}")


async def get_user_value(val_1):
    cur.execute("INSERT OR IGNORE INTO users_id (id) VALUES (?)", (val_1,))
    base.commit()

"""РАССЫЛКА"""
async def replace_language(call):
    try:
        lang = call.data[7:]
        if lang == "RU":
            lang_db = "EN"
        else:
            lang_db = "RU"
        await db_rep_lang(call.message.chat.id, lang_db)

        try:
            await call.message.edit_caption(caption=f"{_('Настройки', lang_db)}",
                                            reply_markup=setting_btn(call, lang_db).as_markup())
        except Exception as e:
            logging.error(f"Ошибка при редактировании сообщения: {e}")
    except Exception as e:
        logging.exception(e)


async def start_c(call):
    lang = await check_lang(call.message.chat.id)
    photo = FSInputFile("media/logo.png")
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await call.message.answer_photo(
        caption=f"<b>{_('Добро пожаловать', lang[0])}, <i>{call.message.chat.first_name}</i></b>",
        reply_markup=start_but(lang[0]).as_markup(), photo=photo)

"""ПРОЦЕСС СОЗДАНИЯ ОФФАЙН СДЕЛКИ"""
async def get_crypto(call : types.CallbackQuery):
    try:
        lang = await check_lang(call.message.chat.id)
        await call.message.edit_text(f'❗<i>Выберите интересующие направление для вас</i>❗\n<b>Формат:</b>\n'
                                  f'<b>Отдаёте-получаете</b>',
                                  reply_markup=crypto_valets(lang).as_markup())
    except Exception as err:
        logging.exception(err)
async def get_messa(call : types.CallbackQuery):
    try:
        lang = await check_lang(call.message.chat.id)
        localized_message = _(f'<b>Доставка курьером производится по этапу:</b>\n1)💸Создаём заявку в боте.\n2)🚛С вами '
                              f'связывается курьер.\n3)🏎 '
                              f'Встречаетесь с курьером.\n4)🚀Проверяем и получаем средства', lang=lang[0])
        await call.message.edit_text(f"{_(text=localized_message)}", reply_markup=setting_rasilka(lang).as_markup())
    except Exception as err:
        logging.exception(err)

"""КОНЕЦ ПРОЦЕСС СОЗДАНИЯ ОФФАЙН СДЕЛКИ"""
### ПРОЦЕСС СОЗДАНИЯ СДЕЛКИ ОНЛАЙН ###
async def deals_online_start(call):
    try:
        lang = await check_lang(call.message.chat.id)
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await call.message.answer(f"<b>{_('Выберите действие', lang[0])}:</b>",
                                  reply_markup=exc_btn_start(lang[0]).as_markup())
    except Exception as e:
        logging.exception(e)


async def deals_online_change_type(call):
    try:
        lang = await check_lang(call.message.chat.id)
        await call.message.edit_text(f"<b>{_('Выберите действие', lang[0])}:</b>",
                                     reply_markup=exc_type_onl_btn(call, lang[0]).as_markup())
    except Exception as e:
        logging.exception(e)


async def deals_online_type_add(call):
    try:
        id_us = call.data.split("_")[1]
        type_d = call.data.split("_")[2]
        lang = await check_lang(call.message.chat.id)
        await db_add_start_deals(id_us, type_d)
        await call.message.edit_text(f"<i>{_('Что отдаете', lang[0])}?</i>",
                                     reply_markup=exc_online_cancel(call, lang[0]).as_markup())
    except Exception as e:
        logging.exception(e)


async def deals_online_cancel(call):
    try:
        id_us = call.data.split("_")[1]
        lang = await check_lang(call.message.chat.id)
        await db_delete_deal(id_us)
        await call.message.edit_text(f"<b>{_('Выберите действие', lang[0])}:</b>",
                                  reply_markup=exc_btn_start(lang[0]).as_markup())
    except Exception as e:
        logging.exception(e)

### КОНЕЦ СОЗДАНИЯ СДЕЛКИ ОНЛАЙН ###
