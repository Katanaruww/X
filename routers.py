import sqlite3
import logging

import config


conn = sqlite3.connect(config.name_db[0], check_same_thread=False)
curs = conn.cursor()


async def start_db(user_id, f_name, l_name):
    curs.execute("INSERT INTO users (id_us, tag, name) VALUES (?, ?, ?)", (user_id, f_name, l_name))
    conn.commit()


async def check_us(us_id):
    try:
        return curs.execute("SELECT * FROM users WHERE id_us = ?", (us_id,)).fetchone()
    except Exception as e:
        logging.warning(e)


async def check_tech():
    try:
        return curs.execute("SELECT * FROM technical").fetchone()
    except Exception as e:
        logging.warning(e)

async def add_lang(lang, id_us):
    try:
        curs.execute("UPDATE users SET lang = ? WHERE id_us = ?", (lang, id_us))
        conn.commit()
    except Exception as e:
        logging.warning(e)

async def check_lang(id_us):
    try:
        return curs.execute("SELECT lang FROM users WHERE id_us = ?", (id_us, )).fetchone()
    except Exception as e:
        logging.warning(e)

def check_lang_smail(id_us):
    lang = curs.execute("SELECT * FROM users WHERE id_us = ?", (id_us,)).fetchone()
    if lang[4] == "RU":
        return lang[4], "🇷🇺"
    else:
        return lang[4], "🇬🇧"

async def db_rep_lang(id_us, lang):
    try:
        curs.execute("UPDATE users SET lang = ? WHERE id_us = ?", (lang, id_us))
        conn.commit()
    except Exception as e:
        logging.warning(e)
