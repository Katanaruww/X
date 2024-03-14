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
                     add_cards_start, delete_cards, add_cards_rub_type, view_list_card, check_status_card_bd)
from translate import _
from inline_but import setting_rasilka, crypto_valets
from limits import limits_currency_pairs
from func import bot
#ertyui
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
                                         reply_markup=admin_exc_rub_add_card(call_id, "add").as_markup())
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
        await call.message.edit_text("<b>Удалено(</b>\n", reply_markup=admin_exc().as_markup())
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
            pass
        else:
            row = await view_list_card(type_v)
            mark = InlineKeyboardBuilder()

            for i in range(len(row)):
                smile = await check_status_card(row[i][5])
                print(smile)
                mark.button(text=f"{row[i][3]}", callback_data=f"see-card_{row[i][5]}")
                mark.button(text=smile, callback_data=f"activate-card_{row[i][5]}")
            mark.button(text="Назад🔙", callback_data="back_admin")
            mark.adjust(2, 2, 2, 2, 2, 1)
            await call.message.edit_text("<b>Список карт:</b>", reply_markup=mark.as_markup())

    except Exception as e:
        logging.exception(e)


async def check_status_card(call_id):
    row = await check_status_card_bd(call_id)
    print(row)
    if row[0] == "1":
        return "🟢"
    elif row[0] == "0":
        return "🔴"
