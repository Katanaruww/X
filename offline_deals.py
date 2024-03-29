import sqlite3
import logging
from aiogram import Router, Bot
import config
from aiogram.filters import Command
import logging
import sqlite3 as sq
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import Router, Bot
from aiogram.types import FSInputFile
from aiogram import types
import config
from aiogram.fsm.state import StatesGroup, State
conn = sqlite3.connect(config.name_db[0], check_same_thread=False)
curs = conn.cursor()
logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s", encoding="UTF-8")


router = Router()
bot = Bot(config.token[0])


class RUBIDR(StatesGroup):
    RUBIDR = State()



@router.callback_query(lambda callback: callback.data or  call.data.startswith("lang_"))
async def call(callback: types.CallbackQuery):
    if callback.data == "RUB|IDR":
        pass



class IDRRUB(StatesGroup):
    IDRRUB = State()



class USDTIDR(StatesGroup):
    USDTIDR = State()


class IDRUSDT(StatesGroup):
    IDRUSDT = State()



class USDIDR(StatesGroup):
    USDIDR = State()



class IDRUSDT(StatesGroup):
    IDRUSDT = State()



class USDUSDT(StatesGroup):
    USDUSDT = State()



class USDTUSD(StatesGroup):
    USDTUSD = State()