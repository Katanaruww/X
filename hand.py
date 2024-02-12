import logging

from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import FSInputFile
from aiogram.types import Message

import config
from inline_but import *
from routers import start_db, check_us

# from func import start_menu, check_admin
router = Router()


class fsm(StatesGroup):
    adm_id = State()


bot = Bot(config.token[0])


@router.message(Command("start"))
async def start_handler(msg: Message):
    try:
        check = await check_us(msg.chat.id)
        print(check)
        if check is not None:
            try:
                photo = FSInputFile("media/logo.png")
                await msg.answer_photo(
                    caption=f"<b>Добро пожаловать, <i>{msg.chat.first_name}</i></b>",
                    reply_markup=start_but().as_markup(), photo=photo)
            except Exception as err:
                logging.warning(err)
        else:
            await msg.answer("<b>тут будут правила</b>", reply_markup=rules().as_markup())
    except Exception as e:
        logging.exception(e)


@router.callback_query(lambda call: True)
async def cal(call):
    if call.data == "agree_rules":
        try:
            await start_db(call.message.chat.id, call.message.chat.username, call.message.chat.first_name)
            photo = FSInputFile("media/logo.png")
            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            await call.message.answer_photo(caption=f"<b>Добро пожаловать, <i>{call.message.chat.first_name}</i></b>",
                                            reply_markup=start_but().as_markup(), photo=photo)
        except Exception as err:
            logging.exception(err)
