import config
import asyncio
import aiogram
import logging
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import Router, Bot
from aiogram.types import FSInputFile
from aiogram import types
from inline_but import *
from routers import (check_lang, db_rep_lang, db_add_start_deals, db_delete_deal, add_pars_deals_onl, db_view_type_give,
                     add_cards_start, delete_cards, add_cards_rub_type, view_list_card, check_status_card_bd,
                     see_cards_db, get_card_db, get_data_deals, edit_amount, print_deals)
from routers import conn, curs
from translate import _
from inline_but import setting_rasilka, crypto_valets
from limits import limits_currency_pairs
from datetime import datetime
import traceback

# ertyui
bot = Bot(config.token[0])
logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s", encoding="UTF-8")


async def add_start_card(call):
    try:
        await call.message.edit_text("<b>Ввод карты!</b>\n"
                                     "<i>Введите валюту, для которой хотите вставить реквизит:</i>",
                                     reply_markup=admin_exc_add_card(call.id, "add").as_markup())
    except Exception as e:
        logging.warning(e)


async def add_currency_card(call):
    try:
        call_id = call.data.split("_")[2]
        type_v = call.data.split("_")[1]
        await add_cards_start(type_v, call_id)
        if type_v == "RUB":
            await call.message.edit_text("<b>Добавили🟢</b>\n"
                                         "<i>Теперь выберите тип оплаты:</i>",
                                         reply_markup=admin_exc_rub_add_card("add", call_id).as_markup())
        else:
            await call.message.edit_text("<b>Добавили🟢</b>\n"
                                         "<i>Теперь введите реквизит:</i>",
                                         reply_markup=adm_exc_cancel_card(call_id).as_markup())
            return call_id
    except Exception as e:
        logging.warning(e)


async def add_type_pay_exc_admin(call):
    try:
        type_b = call.data.split("_")[1]
        call_id = call.data.split("_")[2]
        await add_cards_rub_type(type_b, call_id)
        await call.message.edit_text("<b>Добавили🟢</b>\n"
                                     "<i>Теперь введите реквизит:</i>",
                                     reply_markup=adm_exc_cancel_card(call_id).as_markup())
        return call_id
    except Exception as e:
        logging.warning(e)


async def cancel_add_card(call):
    try:
        call_id = call.data.split("_")[1]
        print(call_id)
        await delete_cards(call_id)
        await call.message.edit_text("<b>Админ-панель</b>\n", reply_markup=admin_exc().as_markup())
    except Exception as e:
        logging.warning(e)


async def get_start_card(call):
    try:
        await call.message.edit_text("<b>Выберите валюту:</b>",
                                     reply_markup=admin_exc_add_card(call.id, "get").as_markup())
    except Exception as e:
        logging.exception(e)


async def get_list_card(call):
    try:
        type_v = call.data.split("_")[1]

        if type_v == "RUB":
            await call.message.edit_text("<b>Выберите тип оплаты:</b>",
                                         reply_markup=admin_exc_rub_add_card("get").as_markup())
        else:
            await print_list_card(call, type_v)

    except Exception as e:
        logging.exception(e)


async def print_list_card(call, type_v, v="None"):
    try:
        if type_v == "RUB":
            row = await view_list_card(type_v, v)
            print(row)
        else:
            row = await view_list_card(type_v)
        mark = InlineKeyboardBuilder()

        for i in range(len(row)):
            smile = await check_status_card(row[i][5])
            mark.button(text=f"{row[i][3]}", callback_data=f"see-card_{row[i][5]}")
            mark.button(text=smile, callback_data=f"activate-card_{row[i][5]}")
        mark.button(text="Назад🔙", callback_data="back_admin")
        mark.adjust(2, 2, 2, 2, 2, 1)
        print(mark.as_markup())
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await call.message.answer("<b>Список карт:</b>\n"
                                  f"<i>Обновлено:</i> <code>{datetime.now().strftime('%H:%M:%S')}</code>\n",
                                  reply_markup=mark.as_markup())
    except Exception as e:
        logging.warning(e)


async def see_card(call):
    try:
        call_id = call.data.split("_")[1]
        row = await see_cards_db(call_id)
        if row[1] == "RUB":
            await print_card_tg(call, row)
        else:
            await print_card_tg(call, row)
    except Exception as e:
        logging.warning(e)


async def print_card_tg(call, row):
    try:

        smile = await check_status_card(row[5])
        message = ""
        message += f"<i>Валюта:</i> <code>{row[1]}</code>\n"
        if row[1] == "RUB":
            message += f"<i>Тип оплаты:</i> <code>{row[2]}</code>\n"
        else:
            pass
        message += (f"<i>Реквизиты:</i> <code>{row[3]}</code>\n"
                    f"<i>Статус:</i> <code>{smile}</code>\n")
        await call.message.edit_text(message, reply_markup=delete_card_button(row[5]).as_markup())
    except Exception as e:
        logging.warning(e)


async def check_status_card(call_id):
    print(call_id)
    row = await check_status_card_bd(call_id)
    if row[0] == "1":
        return "🟢"
    elif row[0] == "0":
        return "🔴"


async def activate_card(call):
    try:
        x = call.data.split("_")[1]
        data = curs.execute("SELECT * FROM cards WHERE id_c = ?", (x,)).fetchone()

        # Используйте один запрос для получения обоих условий и уменьшения вызовов к базе данных
        status_on_data = conn.execute("SELECT id_c, status FROM cards WHERE type_pay = ? AND st = '1'",
                                      (data[2],)).fetchall()
        data_all = next((item for item in status_on_data if item[1] == '0'), None)
        data_lal = next((item for item in status_on_data if item[1] == '1'), None)

        try:
            if data[4] == "1":
                if data[6] == '1':
                    if data_all:
                        curs.execute("UPDATE cards SET status = '1' WHERE id_c = ?", (data_all[0],))
                        conn.commit()
                    curs.execute("UPDATE cards SET st = '0', status = '0' WHERE id_c = ?", (x,))
                    conn.commit()
                else:
                    curs.execute("UPDATE cards SET st = '0' WHERE id_c = ?", (x,))
                    conn.commit()
            elif data[4] == "0":
                if data_lal:
                    curs.execute("UPDATE cards SET status = '0' WHERE id_c = ?", (data_lal[0],))
                    conn.commit()
                curs.execute("UPDATE cards SET st = '1', status = '1' WHERE id_c = ?", (x,))
                conn.commit()
        except Exception as e:
            logging.warning(f"Произошла ошибка: {e}")  # Лучше логировать или печатать исключение для отладки.

        try:
            await call.message.edit_reply_markup(reply_markup=await print_list_card(call, data[1], data[2]))
        except Exception as e:
            logging.warning(f"Не удалось изменить разметку ответа сообщения: {e}")
    except Exception as e:
        logging.warning(e)


async def get_card_check(name_bank):
    try:
        return await get_card_db(name_bank)
    except Exception as e:
        logging.warning(e)


async def get_card_check_deals(deal_id):
    try:
        data_our = await print_deals(deal_id)
        data = await get_data_deals(1)
        if len(data) == 1 and data[0][11] == deal_id:
            return await get_card_db(data[2], data[7])
        else:
            for a in range(len(data)):  # тут сравниваем сделки между собой
                if data_our[5] == data[a][5]:
                    amount_high = await limits_currency_pairs(data_our[2])
                    amount = float(data_our[5]) + float(amount_high[0])
                    await edit_amount(data_our[11], amount)
                    return await get_card_db(data_our[2], data[a][7])
    except Exception as e:
        logging.warning(e)
        logging.error(traceback.print_exc())
