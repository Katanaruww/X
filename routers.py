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

async def check_lang(id_us): # проверка языка пользователя
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

async def db_add_start_deals(id_us, call_id):
    try:
        curs.execute("INSERT INTO deals_onl (id_user, id_call) VALUES (?, ?)", (id_us, call_id))
        conn.commit()
    except Exception as e:
        logging.warning(e)
async def db_view_type_give(id_call, type):
    try:
        if type == "give":
            return curs.execute("SELECT give FROM deals_onl WHERE id_call = ?", (id_call,)).fetchone()
        elif type == "get":
            return curs.execute("SELECT get FROM deals_onl WHERE id_call = ?", (id_call,)).fetchone()
    except Exception as e:
        logging.warning(e)


async def db_delete_deal(call_id):
    try:
        curs.execute("DELETE FROM deals_onl WHERE id_call = ?", (call_id, ))
        conn.commit()
    except Exception as e:
        logging.warning(e)

async def add_pars_deals_onl(call_id, type, val):
    try:
        if type == "give":
            curs.execute("UPDATE deals_onl SET give = ? WHERE id_call = ?", (val, call_id))
            conn.commit()
        elif type == "get":
            curs.execute("UPDATE deals_onl SET get = ? WHERE id_call = ?", (val, call_id))
            conn.commit()
    except Exception as e:
        logging.warning(e)


async def add_amount_deals_onl(id_call, amount):
    try:
        curs.execute('UPDATE deals_onl SET amount_in = ? WHERE id_call = ?', (amount, id_call))
        conn.commit()
    except Exception as e:
        logging.warning(e)


async def add_cards_start(type_v, call_id):
    try:
        curs.execute("INSERT INTO cards (curr, id_c) VALUES (?, ?)", (type_v, call_id))
        conn.commit()
    except Exception as e:
        logging.warning(e)


async def add_cards_rub_type(type_b, call_id):
    try:
        curs.execute("UPDATE cards SET type_pay = ? WHERE id_c = ?", (type_b, call_id))
        conn.commit()
    except Exception as e:
        logging.warning(e)


async def delete_cards(call_id):
    try:
        curs.execute("DELETE FROM cards WHERE id_c = ?", (call_id,))
        conn.commit()
    except Exception as e:
        logging.warning(e)


async def add_rekv_cards(rekv, call_id):
    try:
        curs.execute("UPDATE cards SET rekv = ? WHERE id_c = ?", (rekv, call_id))
        conn.commit()
    except Exception as e:
        logging.warning(e)


async def view_list_card(type_v, v="None"):
    try:
        if type_v == "RUB":
            pass
        else:
            row = curs.execute("SELECT * FROM cards WHERE curr = ?", (type_v,)).fetchall()
            return row
    except Exception as e:
        logging.exception(e)


async def check_status_card_bd(call_id):
    try:
        row = curs.execute("SELECT st FROM cards WHERE id_c = ?", (call_id,)).fetchone()
        return row
    except Exception as e:
        logging.warning(e)
