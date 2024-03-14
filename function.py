import aiohttp
from bs4 import BeautifulSoup
import asyncio
import logging
import types

from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import FSInputFile
from aiogram.types import Message

import config
from inline_but import *
from routers import start_db, check_us

import lxml


import asyncio
router = Router()
bot = Bot(config.token[0])
#edsfghjk
logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                        format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s", encoding="UTF-8")
async def fetch_currency(url, headers):
    # Создаем объект TCPConnector с параметром ssl=False для отключения проверки SSL
    connector = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url, headers=headers) as response:  # Отправляем асинхронный GET-запрос
            src = await response.text()  # Получаем текст ответа
            soup = BeautifulSoup(src, "lxml")
            new = soup.find_all(class_="DFlfde SwHCTb")  # Ищем нужные элементы
            for i in new:
                global curs
                curs = i.text  # Выводим результат


# URL и заголовки остаются теми же
url = "https://www.google.com/search?q=1+%D1%80%D1%83%D0%B1%D0%BB%D1%8C+%D0%B2+idr&oq=1+%D1%80%D1%83%D0%B1&gs_lcrp=EgZjaHJvbWUqCAgAEEUYJxg7MggIABBFGCcYOzIGCAEQRRg5MgoIAhAAGLEDGIAEMgcIAxAAGIAEMgcIBBAAGIAEMgcIBRAAGIAEMgcIBhAAGIAEMgYIBxBFGD2oAgCwAgA&sourceid=chrome&ie=UTF-8"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
}

# Запускаем асинхронную функцию
asyncio.run(fetch_currency(url, headers))

async def get_pars(message: Message):
    await message.answer(f"Здравствуйте, готовы сделать обмен при личной встрече, доставка до двери!\n"
                         f"➡️Мы предлагаем самые выгодные условия по сделке на Бали, если Вы нашли более выгодный "
                         f"курс, присылайте нам скрины, мы создадим для Вас  более выгодные условия по обмену✔\n\n"
                         f"⚠️актуальный курс на сегодня:\n"
                         f"✅10.000 ₽ - 50.000₽ - "
                         f"{round(float(curs.replace(',', '.')) - float(curs.replace(',', '.')) * 0.055, 1)} IDR\n"
                         f"✅50.000 ₽ - 100.000₽ - "
                         f"{round(float(curs.replace(',', '.')) - float(curs.replace(',', '.')) * 0.05, 1)} IDR\n"
                         f"✅100.000 ₽ -300.000₽ - "
                         f"{round(float(curs.replace(',', '.')) - float(curs.replace(',', '.')) * 0.045, 1)} IDR\n"
                         f"✅300.000 ₽ -500.000₽ - "
                         f"{round(float(curs.replace(',', '.')) - float(curs.replace(',', '.')) * 0.04, 1)} IDR\n"
                         f"✅500.000 ₽ -1.000.000₽- "
                         f"{round(float(curs.replace(',', '.')) - float(curs.replace(',', '.')) * 0.035, 1)} IDR\n")