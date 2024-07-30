import sqlite3
import logging

import config

conn = sqlite3.connect(config.name_db[0], check_same_thread=False)
curs = conn.cursor()


async def start_db(user_id, f_name, l_name):
    curs.execute("INSERT INTO users (id_us, tag, name) VALUES (?, ?, ?)", (user_id, f_name, l_name))
    conn.commit()


async def getegtegeteg():
    curs.execute("INSERT INTO deals_off (id_us) VALUES (?)", (123131232,))
    conn.commit()


async def check_us(us_id):
    try:
        return curs.execute("SELECT * FROM users WHERE id_us = ?", (us_id,)).fetchone()
    except Exception as e:
        logging.warning(e)


# werftghyjkl
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


async def check_lang(id_us):  # проверка языка пользователя
    try:
        return curs.execute("SELECT lang FROM users WHERE id_us = ?", (id_us,)).fetchone()
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


async def db_view_type_give(id_call, typ):
    try:
        if typ == "give":
            return curs.execute("SELECT give FROM deals_onl WHERE id_call = ?", (id_call,)).fetchone()
        elif typ == "get":
            return curs.execute("SELECT get FROM deals_onl WHERE id_call = ?", (id_call,)).fetchone()
    except Exception as e:
        logging.warning(e)


async def db_delete_deal(call_id):
    try:
        curs.execute("DELETE FROM deals_onl WHERE id_call = ?", (call_id,))
        conn.commit()
    except Exception as e:
        logging.warning(e)


async def add_pars_deals_onl(call_id, typ, val):
    try:
        if typ == "give":
            curs.execute("UPDATE deals_onl SET give = ? WHERE id_call = ?", (val, call_id))
            conn.commit()
        elif typ == "get":
            curs.execute("UPDATE deals_onl SET get = ? WHERE id_call = ?", (val, call_id))
            conn.commit()
    except Exception as e:
        logging.warning(e)


async def add_amount_deals_onl(id_call, amount, rekv_us):
    try:
        curs.execute('UPDATE deals_onl SET amount_in = ?, rekv_user = ? WHERE id_call = ?', (amount, rekv_us, id_call))
        conn.commit()
    except Exception as e:
        logging.warning(e)


async def print_deals(call_id):
    try:
        return curs.execute("SELECT * FROM deals_onl WHERE id_call = ?", (call_id,)).fetchone()
    except Exception as e:
        logging.warning(e)


async def add_amount_out(amount_out, curr, oper, call_id):
    try:
        curs.execute("UPDATE deals_onl SET amount_out = ?, currency = ?, id_oper= ? WHERE id_call = ?",
                     (amount_out, curr, oper, call_id))
        conn.commit()
    except Exception as e:
        logging.warning(e)


async def add_t_p(t_p, call_id):
    try:
        curs.execute("UPDATE deals_onl SET type_pay = ? WHERE id_call = ?", (t_p, call_id,))
        conn.commit()
    except Exception as e:
        logging.warning(e)


async def add_type_our(rekv_our, call_id, t_p="None"):
    try:
        curs.execute("UPDATE deals_onl SET type_pay = ?, rekv_our = ? WHERE id_call = ?", (t_p, rekv_our, call_id))
        conn.commit()
    except Exception as e:
        logging.warning(e)


async def get_data_deals(st):
    try:
        return curs.execute("SELECT * FROM deals_onl WHERE status = ?", (st,)).fetchall()
    except Exception as e:
        logging.warning(e)


async def get_card_db(value, name_bank=None):
    try:
        if name_bank is None:
            row = conn.execute("SELECT rekv FROM cards WHERE curr = ? AND st = '1' AND status ='1'",
                               (value,)).fetchone()
        else:
            row = conn.execute("SELECT rekv FROM cards WHERE curr = ? AND type_pay = ? AND st = '1' AND status ='1'",
                               (value, name_bank,)).fetchone()
        rekv = row[0]
        return rekv
    except TypeError:
        return None
    except Exception as e:
        logging.warning(e)


async def edit_amount(deal_onl, amount):
    try:
        conn.execute('UPDATE deals_onl SET amount_in = ? WHERE id_call = ?', (amount, deal_onl))
        conn.commit()
    except Exception as e:
        logging.warning(e)


### НИЖЕ НЕ ЛЕЗТЬ ###

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
            row = curs.execute("SELECT * FROM cards WHERE curr = ? AND type_pay = ?", (type_v, v)).fetchall()
            return row
        else:
            row = curs.execute("SELECT * FROM cards WHERE curr = ?", (type_v,)).fetchall()
            return row
    except Exception as e:
        logging.exception(e)


async def check_status_card_bd(call_id):
    try:
        print(call_id)
        row = curs.execute("SELECT st FROM cards WHERE id_c = ?", (call_id,)).fetchone()
        return row
    except Exception as e:
        logging.warning(e)


async def see_cards_db(call_id):
    try:
        row = curs.execute("SELECT * FROM cards WHERE id_c = ?", (call_id,)).fetchone()
        return row
    except Exception as e:
        logging.warning(e)

async def change_number_deal(call_id, num):
    try:
        curs.execute("UPDATE deals_onl SET status = ? WHERE id_call = ?", (num, call_id, ))
        conn.commit()
        return 200
    except Exception as e:
        logging.warning(e)

