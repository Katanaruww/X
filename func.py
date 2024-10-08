import logging
import sqlite3 as sq
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import Router, Bot
from aiogram.types import FSInputFile
from aiogram import types
import config
from inline_but import *
from routers import (check_us, check_lang, db_rep_lang, db_add_start_deals, db_delete_deal, add_pars_deals_onl, db_view_type_give,
                     print_deals, add_amount_out, add_t_p, add_type_our, get_card_db, change_number_deal)
from cards import get_card_check_deals
from translate import _
from inline_but import setting_rasilka, crypto_valets, admin_but_blaack_list, add_cur_offline
from limits import limits_currency_pairs
from translate import _
from routers import check_lang, st_move_cards
from inline_but import add_cur_offline, dell_state
import sqlite3
from currency import get_pars, get_pars2
from dop_func.func_float import format_number
from auto import check_transaction
from aiogram.enums.parse_mode import ParseMode
import traceback
# ERTYU
# пенис
router = Router()
bot = Bot(config.token[0])
logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s", encoding="UTF-8")


class FSM(StatesGroup):
    set_amount = State()



def sql_start():
    global base, cur
    base = sq.connect('users_bd.db')
    cur = base.cursor()
    if base:
        print(f"Database connect OK")
    base.execute('CREATE TABLE IF NOT EXISTS users_id(id INTEGER PRIMARY KEY)')

    base.execute('CREATE TABLE IF NOT EXISTS ban_users(username TEXT PRIMARY KEY, id INTEGER)')

    base.execute('CREATE TABLE IF NOT EXISTS courier(id INTEGER PRIMARY KEY AUTOINCREMENT ,username TEXT, tg_id INTEGER, name TEXT, area TEXT, Like INTEGER)')

    base.execute('CREATE TABLE IF NOT EXISTS deals(username TEXT, id INTEGER, onecur TEXT, twocur INTEGER, cash TEXT, '
                 'innn TEXT, out TEXT, area TEXT, time TEXT)')

    base.execute('CREATE TABLE IF NOT EXISTS Reviews(username TEXT NOT NULL , stars TEXT NOT NULL)')
    base.execute('''
            CREATE TABLE IF NOT EXISTS Curs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                c1 TEXT,
                c2 TEXT,
                c3 TEXT,
                c4 TEXT,
                c5 TEXT
            )
        ''')
    base.execute('''
                CREATE TABLE IF NOT EXISTS Curs2 (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    c1 TEXT
                )
            ''')
    base.execute('''
                CREATE TABLE IF NOT EXISTS Curs3 (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    c1 TEXT,
                    c2 TEXT,
                    c3 TEXT,
                    c4 TEXT,
                    c5 TEXT
                )
            ''')

    base.execute('''
                    CREATE TABLE IF NOT EXISTS Curs4 (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        c1 TEXT
                    )
                ''')
    base.execute('''
                    CREATE TABLE IF NOT EXISTS Curs5 (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        c1 TEXT
                    )
                ''')
    base.execute('''
                    CREATE TABLE IF NOT EXISTS Curs6 (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        c1 TEXT
                    )
                ''')
    base.execute('''
                    CREATE TABLE IF NOT EXISTS Curs7 (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        c1 TEXT
                    )
                ''')

    base.execute('''
                        CREATE TABLE IF NOT EXISTS Curs8 (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            c1 TEXT
                        )
                    ''')

    base.execute('''
                            CREATE TABLE IF NOT EXISTS Curs9 (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                c1 TEXT
                            )
                        ''')

    base.execute('''
                            CREATE TABLE IF NOT EXISTS Curs10 (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                c1 TEXT
                            )
                        ''')
    base.commit()


"""РАССЫЛКА"""
async def add_values(c1, c2, c3, c4, c5):
        cur.execute('''
            INSERT INTO Curs (c1, c2, c3, c4, c5)
            VALUES (?, ?, ?, ?, ?)
        ''', (c1, c2, c3, c4, c5))
        base.commit()


async def add_values2(c1):
    cur.execute('''
            INSERT INTO Curs2 (c1)
            VALUES (?)
        ''', (c1,))
    base.commit()

async def add_values3(c1, c2, c3, c4, c5):
    cur.execute('''
            INSERT INTO Curs3 (c1, c2, c3, c4, c5)
            VALUES (?, ?, ?, ?, ?)
        ''', (c1, c2, c3, c4, c5))
    base.commit()

async def add_values4(c1):
    cur.execute('''
            INSERT INTO Curs4 (c1)
            VALUES (?)
        ''', (c1,))
    base.commit()
async def add_values5(c1):
    cur.execute('''
            INSERT INTO Curs5 (c1)
            VALUES (?)
        ''', (c1,))
    base.commit()
async def add_values6(c1):
    cur.execute('''
            INSERT INTO Curs6 (c1)
            VALUES (?)
        ''', (c1,))
    base.commit()
async def add_values7(c1):
    cur.execute('''
            INSERT INTO Curs7 (c1)
            VALUES (?)
        ''', (c1,))
    base.commit()
async def add_values8(c1):
    cur.execute('''
            INSERT INTO Curs8 (c1)
            VALUES (?)
        ''', (c1,))
    base.commit()

async def add_values9(c1):
    cur.execute('''
            INSERT INTO Curs9 (c1)
            VALUES (?)
        ''', (c1,))
    base.commit()

async def add_values10(c1):
    cur.execute('''
            INSERT INTO Curs10 (c1)
            VALUES (?)
        ''', (c1,))
    base.commit()
async def get_values_from_column(column_name):
    query = f"SELECT {column_name} FROM Curs"
    with sqlite3.connect('users_bd.db') as db:
        cursor = db.execute(query)
        rows = cursor.fetchall()
        return [row[0] for row in rows]

async def get_values_from_column2(column_name):
    query = f"SELECT {column_name} FROM Curs2"
    with sqlite3.connect('users_bd.db') as db:
        cursor = db.execute(query)
        rows = cursor.fetchall()
        return [row[0] for row in rows]

async def get_values_from_column3(column_name):
    query = f"SELECT {column_name} FROM Curs3"
    with sqlite3.connect('users_bd.db') as db:
        cursor = db.execute(query)
        rows = cursor.fetchall()
        return [row[0] for row in rows]

async def get_values_from_column4(column_name):
    query = f"SELECT {column_name} FROM Curs4"
    with sqlite3.connect('users_bd.db') as db:
        cursor = db.execute(query)
        rows = cursor.fetchall()
        return [row[0] for row in rows]
async def get_values_from_column5(column_name):
    query = f"SELECT {column_name} FROM Curs5"
    with sqlite3.connect('users_bd.db') as db:
        cursor = db.execute(query)
        rows = cursor.fetchall()
        return [row[0] for row in rows]
async def get_values_from_column6(column_name):
    query = f"SELECT {column_name} FROM Curs6"
    with sqlite3.connect('users_bd.db') as db:
        cursor = db.execute(query)
        rows = cursor.fetchall()
        return [row[0] for row in rows]
async def get_values_from_column7(column_name):
    query = f"SELECT {column_name} FROM Curs7"
    with sqlite3.connect('users_bd.db') as db:
        cursor = db.execute(query)
        rows = cursor.fetchall()
        return [row[0] for row in rows]
async def get_values_from_column8(column_name):
    query = f"SELECT {column_name} FROM Curs8"
    with sqlite3.connect('users_bd.db') as db:
        cursor = db.execute(query)
        rows = cursor.fetchall()
        return [row[0] for row in rows]

async def get_values_from_column9(column_name):
    query = f"SELECT {column_name} FROM Curs9"
    with sqlite3.connect('users_bd.db') as db:
        cursor = db.execute(query)
        rows = cursor.fetchall()
        return [row[0] for row in rows]

async def get_values_from_column10(column_name):
    query = f"SELECT {column_name} FROM Curs10"
    with sqlite3.connect('users_bd.db') as db:
        cursor = db.execute(query)
        rows = cursor.fetchall()
        return [row[0] for row in rows]
async def send_deals(o, n, e, r, w, t, j, i, k):
    cur.execute("INSERT INTO deals (username, id, onecur, twocur, cash, innn, out, area, time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (o, n, e, r, w, t, j, i, k,))
    base.commit()

async def get_average_rating(courier_id, idsse):
    try:
        cur.execute('SELECT SUM(stars), COUNT(stars) FROM Reviews WHERE username = ?', (courier_id,))
        result = cur.fetchone()
        lang = await check_lang(idsse)
        if result and result[1] == 0:  # Если записей нет
            return f"{_("Курьер на стажировке", lang[0])}"
        if result and result[0] is not None and result[1] is not None and result[1] != 0:
            total_sum = result[0]
            count = result[1]
            return round(total_sum / count, 2)  # Округление до двух знаков после запятой
        return f"{_("Курьер на стажировке", lang[0])}"
    except sqlite3.Error as e:
        logging.error(f"SQLite error: {e}")
        return f"{_("Курьер на стажировке", lang[0])}"



async def send_reviews(o, n):
    cur.execute("INSERT INTO Reviews (username, stars) VALUES (?, ?)", (o, n))
    base.commit()

async def send_broadcast(message_text, photo_url):
    cur.execute('SELECT id FROM users_id')
    users = cur.fetchall()
    for user in users:
        try:
            lang = await check_lang(user[0])
            await bot.send_photo(user[0], photo=photo_url, caption=message_text,
                                 reply_markup=setting_rasilka(lang).as_markup())
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


"""ЧЕРНЫЙ СПИСОК2"""


async def ban_us(val_1):
    cur.execute("INSERT OR IGNORE INTO ban_users (username) VALUES (?)", (val_1,))
    base.commit()


async def ban_us2(val_1):
    cur.execute("INSERT OR IGNORE INTO ban_users (id) VALUES (?)", (val_1,))
    base.commit()


async def ban_users_us(message: types.Message, val_1):
    try:
        cur.execute("SELECT username FROM ban_users")
        ids = [row[0] for row in cur]
        for i in ids:
            if i == val_1:
                lang = await check_lang(message.chat.id)
                # await message.answer(f"<b><i>{_('К сожалению вы забанены', lang[0])}</i></b>")
                await message.answer("К сожалению вы забанены")
    except Exception as e:
        logging.warning(e)


async def ban_users_us2(message: types.Message, val_1):
    try:
        cur.execute("SELECT id FROM ban_users")
        ids = [row[0] for row in cur]
        for i in ids:
            if i == val_1:
                lang = await check_lang(message.chat.id)
                # await message.answer(f"<b><i>{_('К сожалению вы забанены', lang[0])}</i></b>")
                await message.answer("К сожалению вы забанены")
    except Exception as e:
        logging.warning(e)


async def check_bans():
    try:
        cur.execute("SELECT username FROM ban_users")
        ids = [row[0] for row in cur]
        return ids
    except Exception as e:
        logging.warning(e)


async def check_bans2():
    try:
        cur.execute("SELECT id FROM ban_users")
        ids = [row[0] for row in cur]
        return ids
    except Exception as e:
        logging.warning(e)


"""КОНЕЦ ЧЕРНЫЙ СПИСОК2"""
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

cur111 = ["RUB", "IDR", "USD", "USDT", "BTC", "LTC"]

async def get_cur(a111, call: types.CallbackQuery):
    lang = await check_lang(call.message.chat.id)
    try:
        if a111 in cur111:
            # return f"<b><i>💸{_(text='Отлично! Первый пункт выполнен!', lang=lang[0])}</i></b>"
            return True
        else:
            return False
    except Exception as err:
        logging.exception(err)

# async def get_cur2(val_out, call: types.CallbackQuery, val_in, amount):
#     lang = await check_lang(call.message.chat.id)
#     try:
#         if val_in in cur111:
#             curs = round(float(await get_pars_rub(amount=amount, val_in=val_in, val_out=val_out)))
#             return f"<b><i>💸{_(text='Отлично! Обмен по актуальному курсу будет составлять - ', lang=lang[0])} {curs}</i></b>"
#         else:
#             return f"{_(text='Повторите попытку', lang=lang[0])}"
#     except Exception as err:
#         logging.exception(err)
async def get_cur2(val_out, call: types.CallbackQuery, val_in, amount, state: FSMContext):
    lang = await check_lang(call.message.chat.id)
    try:

        if val_in in cur111:
            result = await get_pars2(amount=int(amount), val_in=val_in, val_out=val_out)
            resultone = await get_pars2(amount=1, val_in=val_in, val_out=val_out)
            print(result)
            print(resultone)
            if result is not None:
                curs = round(float(result))
                print(f"val_in {val_in}")
                print(f"val_out {val_out}")
                return (f"<b><i>💰 {_(text='Актуальный курс', lang=lang[0])}: {format_number(float(resultone), val_out)} {val_out}\n💳 "
                        f"{_(text='Вы отдадите', lang=lang[0])}: {format_number(float(amount), val_in)} {val_in}\n💸 "
                        f"{_(text='Обмен по актуальному курсу будет составлять:', lang=lang[0])}"
                        f"{str(format_number(float(format_number(float(resultone), val_out))*float(format_number(float(amount), val_in)), val_out))} {val_out}</i></b>")
            else:
                # Если результат None, то сообщение об ошибке
                return f"{_(text='Не удалось получить курс. Повторите попытку позже.', lang=lang[0])}"
        else:
            return f"{_(text='Повторите попытку', lang=lang[0])}"
    except Exception as err:
        logging.exception(err)
        return f"{_(text='Произошла ошибка. Повторите попытку позже.', lang=lang[0])}"


async def get_messs(a000, call: types.CallbackQuery):
    lang = await check_lang(call.message.chat.id)
    name = await limits_currency_pairs(f"{a000}")
    await call.message.edit_text(f'<b><i>{_(text="Введите сумму на обмен. Минимальное значение - ", lang=lang[0])} {name[0]}</i></b>', reply_markup=dell_state(lang).as_markup())




async def get_cb(call: types.CallbackQuery, state: FSMContext):
    try:
        lang = await check_lang(call.message.chat.id)
        # await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await call.message.answer(f"<b>{_('Выберите действие', lang[0])}:</b>",
                                  reply_markup=exc_btn_start(lang[0]).as_markup())
        await state.clear()
    except Exception as err:
        logging.exception(err)



async def get_black_list(call: types.CallbackQuery):
    try:
        await call.message.edit_text(f'Выберите способ бана пользователя:',
                                     reply_markup=admin_but_blaack_list().as_markup())
    except Exception as err:
        logging.exception(err)


async def get_messa(call: types.CallbackQuery):
    try:
        lang = await check_lang(call.message.chat.id)
        localized_message = f'<b>{_("Доставка курьером производится по этапу:", lang[0])}</b>\n' \
                            f'<b><i>💸{_("Создаём заявку в боте.", lang[0])}</i></b>\n' \
                            f'<b><i>🚛{_("С вами связывается курьер.", lang[0])}</i></b>\n' \
                            f'<b><i>🏎{_("Встречаетесь с курьером.", lang[0])}</i></b>\n' \
                            f'<b><i>🚀{_("Проверяем и получаем средства.", lang[0])}</i></b>\n'

        await call.message.edit_text(f"{_(text=localized_message)}",
                                     reply_markup=setting_rasilka(lang).as_markup())
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


async def deals_online_type_add(call, type="start"):
    try:
        if type == "start":
            id_us = call.message.chat.id
            lang = await check_lang(call.message.chat.id)
            await db_add_start_deals(id_us, call.id)
            await call.message.edit_text(f"<i>{_('Что отдаете', lang[0])}?</i>",
                                         reply_markup=exc_type_onl_btn(call.id, lang[0], "give").as_markup())
    except Exception as e:
        logging.exception(e)


async def deals_add_curr(call):
    try:
        type = "give"
        val = call.data.split("_")[1]
        idd = call.data.split("_")[2]
        await add_pars_deals_onl(idd, type, val)
        lang = await check_lang(call.message.chat.id)
        if type == "give":
            await call.message.edit_text(f"<i>{_('Что хотите получить', lang[0])}?</i>",
                                         reply_markup=exc_type_onl_btn(idd, lang[0], "get").as_markup())
    except Exception as e:
        logging.exception(e)


async def deals_add_curr_finish(call, state: FSMContext):
    try:
        tep = "get"
        val = call.data.split("_")[1]
        idd = call.data.split("_")[2]
        await add_pars_deals_onl(idd, tep, val)
        lang = await check_lang(call.message.chat.id)
        view_give = await db_view_type_give(idd, "give")
        view_get = await db_view_type_give(idd, "get")
        min_am = await limits_currency_pairs(view_give[0])
        await call.message.edit_text(f"<i>{_('Отлично! Теперь введите сумму в', lang[0])} <i>{view_give[0]}</i>, "
                                     f"{_('которую хотите обменять на', lang[0])} {view_get[0]}</i>\n"
                                     f"<b><i>{_('Минимальная сумма', lang[0])}:</i></b> <i>{min_am[0]} {view_give[0]}</i>",
                                     reply_markup=exc_btn_cancel(idd, lang[0], ).as_markup())
        return idd, min_am[0]
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


async def transaction_con(message, call_id):
    try:
        row = await print_deals(call_id)
        curr = await get_pars(row[2], row[3])
        amount_out = float(curr * row[5] * config.percent)
        oper = config.operators[0][0]
        await add_amount_out(amount_out, curr, oper, call_id)
        deal = await print_deals(call_id)
        lang = await check_lang(message.chat.id)

        mess = (f"<b>{_('Актуальный курс', lang[0])}: <code>{format_number(deal[4], deal[3])}</code></b> <i>{deal[3]}</i>\n\n"
                f"<b>{_('Вы отдадите', lang[0])}:</b> <code>{deal[5]}</code> <i>{deal[2]}</i>\n"
                f"<b>{_('Вы получите', lang[0])}:</b> <code>{format_number(deal[6], deal[3])}</code> <i>{deal[3]}</i>\n\n")
        if deal[2] == "RUB":
            mess += f"<i>{_('Для продолжения выберите способ оплаты', lang[0])}:</i>"
            await message.answer(mess, reply_markup=admin_exc_rub_add_card("print", "deal", call_id,0, lang[0]).as_markup())
        else:
            rekv = await get_card_check_deals(deal[11])
            await add_type_our(rekv, call_id)
            await message.answer(mess, reply_markup=continue_add_deal(call_id, lang[0]).as_markup())


    except Exception as e:
        logging.exception(e)


async def choose_pay_method(call):
    try:
        lang = await check_lang(call.message.chat.id)
        call_id = call.data.split("_")[2]
        deal = await print_deals(call_id)
        t_p = call.data.split("_")[1]
        await add_t_p(t_p, call_id)
        rekv = await get_card_check_deals(deal[11])
        await add_type_our(rekv, call_id, t_p)
        mess = (f"<b>{_('Актуальный курс', lang[0])}: <code>{format_number(deal[4], deal[3])}</code></b> <i>{deal[3]}</i>\n\n"
                f"<b>{_('Вы отдадите', lang[0])}:</b> <code>{deal[5]}</code> <i>{deal[2]}</i>\n"
                f"<b>{_('Вы получите', lang[0])}:</b> <code>{format_number(deal[6], deal[3])}</code> <i>{deal[3]}</i>\n\n"
                f"<b>{_('Тип оплаты', lang[0])}:</b> <code>{t_p}</code>")

        await call.message.edit_text(mess, reply_markup=continue_add_deal(call_id, lang[0]).as_markup())
    except Exception as e:
        logging.exception(e)


async def continue_in_deals(call):
    try:
        id_deals = call.data.split("_")[1]
        lang = await check_lang(call.message.chat.id)
        data = await print_deals(id_deals)
        message = (f"<b>{_('Сделка №', lang[0])}{data[0]}</b>\n\n"
                   f"<b>{_('Актуальный курс', lang[0])}:</b> <code>{format_number(data[4], data[3])} {data[3]}</code>\n\n"
                   f"<b>{_('Отдаете', lang[0])}:</b> <code>{data[5]} {data[2]}</code>\n"
                   f"<b>{_('Получаете', lang[0])}:</b> <code>{format_number(data[6], data[3])} {data[3]}</code>\n\n"
                   f"<b>{_('Вы переводите на', lang[0])}:</b> <code>{data[8]}</code>\n")
        if data[7] is not None and data[2] == "RUB":
            message += f"<b>{_('Тип оплаты', lang[0])}:</b> <code>{data[7]}</code>\n\n"
        message += (f"<b>{_('Получаете сюда', lang[0])}:</b> <code>{data[9]}\n\n</code>"
                    f"<b>{_('По всем вопросам', lang[0])}:</b> @{data[10]}")
        x = await change_number_deal(id_deals, 1)
        await st_move_cards(data[2], data[7])
        if x == 200:
            await call.message.edit_text(message, reply_markup=accept_deals(id_deals, lang[0]).as_markup())
    except Exception as e:
        logging.exception(e)

async def accept_in_deals(call):
    try:
        id_deal = call.data.split("_")[2]
        print(id_deal)
        username = call.message.chat.username
        lang = await check_lang(call.message.chat.id)
        deal_info = await print_deals(id_deal)
        stat = await change_number_deal(id_deal, 2)
        if stat == 200:
            await call.message.edit_text(
                f"<b>{_('Благодарим вас!', lang[0])}</b>\n\n"
                f"<i>{_('Сделка №', lang[0])}{deal_info[0]}</i>\n"
                f"<i>{_('Актуальный курс', lang[0])}: <b>{format_number(deal_info[4], deal_info[3])} {deal_info[3]}\n</b></i>"
                f"<i>{_('Отдаете', lang[0])}: <b>{deal_info[5]} {deal_info[2]}\n</b></i>"
                f"<i>{_('Получаете', lang[0])}: <b>{format_number(deal_info[6], deal_info[3])} {deal_info[3]}\n\n</b></i>"
                f"<code>{_('Ожидайте подтверждение перевода!', lang[0])}</code>\n"
                f"<code>{_('По любым вопросам обращайтесь к своему оператору', lang[0])} @{deal_info[10]}</code>")
        print(deal_info[7])
        answer = await check_transaction.auto_check(id_deal, deal_info[7])
        if answer == True:
            print("ok")
            user = await check_us(deal_info[1])
            await bot.send_message(deal_info[1], f"<b>{_('Перевод подтвержден', lang[0])}🎉</b>\n\n"
                                            f"<code>{_('Ожидайте подтверждение перевода вам', lang[0])})</code>", parse_mode="HTML")
            await bot.send_message(-1002224991103, f"<b>Сделка №{deal_info[0]}</b>\n\n"
                                                   f"<b>Платеж подтвержден🟢</b>\n\n"
                                                   f"<b>Валюта:</b> <i>{deal_info[3]}</i>\n"
                                                   f"<b>Реквизиты:</b> <code>{deal_info[9]}</code>\n\n"
                                                   f"<b>>Сумма перевода:</b> <code>{format_number(deal_info[6], deal_info[3])}</code> <i>{deal_info[3]}</i>", parse_mode="HTML", reply_markup=final_button(id_deal, user[2]).as_markup())
        if answer == False:
            user = await check_us(deal_info[1])
            await bot.send_message(deal_info[1], f"<b>{_('Что то пошло не так', lang[0])}(</b>\n\n"
                                                 f"<code>{_('Напишите своему оператору для уточнения информации', lang[0])}</code>", parse_mode="HTML", reply_markup=help_oper(deal_info[10], lang[0]).as_markup())
            await bot.send_message(-1002224991103, f"<b>Сделка №{deal_info[0]}</b>\n\n"
                                                   f"<b>Платеж НЕ подтвержден🛑</b>\n\n"
                                                   f"<b>Валюта:</b> <i>{deal_info[3]}</i>\n"
                                                   f"<b>Реквизиты:</b> <code>{deal_info[9]}</code>\n\n"
                                                   f"<b>Сумма перевода:</b> <code>{format_number(deal_info[6], deal_info[3])}</code> <i>{deal_info[3]}</i>\n\n"
                                                   f"Свяжитесь с покупателем для уточнения информации", parse_mode="HTML", reply_markup=final_button(id_deal, user[2]).as_markup())


    except Exception as e:
        traceback.print_exc()
        logging.exception(e)


async def final_deals(call):
    try:
        id_deal = call.data.split("_")[1]
        deal_info = await print_deals(id_deal)
        user = await check_us(deal_info[1])
        lang = await check_lang(user[1])
        stat = await change_number_deal(id_deal, 3)
        await call.message.edit_text(f"<b>Сделка №{deal_info[0]} завершена</b>🟢\n"
                                        f"<i>Пользователь: @{user[2]}</i>")
        await bot.send_message(user[1], f"{_('Оператор подтвердил перевод средств', lang[0])}🟢\n"
                                            f"{_('Ожидайте поступлление средств', lang[0])}\n\n"
                                            f"{_('Если в течении 20 минут вам не поступили средства напишите оператору', lang[0])}\n\n"
                                            f"{_('Хорошего дня', lang[0])}⚡️", reply_markup=help_oper(deal_info[10], lang[0], 1).as_markup())
    except Exception as e:
        traceback.print_exc()
        logging.warning(e)


async def cancel_final_deals(call):
    try:
        id_deal = call.data.split("_")[1]
        await call.message.edit_text(f"<b>Введите причину отмены сделки:</b>\n")
        return id_deal
    except Exception as e:
        traceback.print_exc()
        logging.warning(e)
### КОНЕЦ СОЗДАНИЯ СДЕЛКИ ОНЛАЙН ###
