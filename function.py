import aiohttp
from bs4 import BeautifulSoup
import asyncio
import logging
import types
import requests
from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import FSInputFile
from aiogram.types import Message

import config
from inline_but import *
from routers import start_db, check_us



import asyncio
router = Router()
bot = Bot(config.token[0])
# async def fetch_currency(url, headers):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url, headers=headers) as response:  # Отправляем асинхронный GET-запрос
#             src = await response.text()  # Получаем текст ответа
#             soup = BeautifulSoup(src, "lxml")
#             new = soup.find_all(class_="DFlfde SwHCTb")  # Ищем нужные элементы
#             for i in new:
#                 global curs
#                 curs = i.text  # Выводим результат
#
# # URL и заголовки остаются теми же
# url = "https://www.google.com/search?q=1+%D1%80%D1%83%D0%B1%D0%BB%D1%8C+%D0%B2+idr&oq=1+%D1%80%D1%83%D0%B1&gs_lcrp=EgZjaHJvbWUqCAgAEEUYJxg7MggIABBFGCcYOzIGCAEQRRg5MgoIAhAAGLEDGIAEMgcIAxAAGIAEMgcIBBAAGIAEMgcIBRAAGIAEMgcIBhAAGIAEMgYIBxBFGD2oAgCwAgA&sourceid=chrome&ie=UTF-8"
# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
#               "application/signed-exchange;v=b3;q=0.7",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
# }
#
# # Запускаем асинхронную функцию
#
# asyncio.run(fetch_currency(url, headers))


async def get_pars(message: Message):
    lists = []
    url = "https://www.google.com/search?q=1+%D1%80%D1%83%D0%B1%D0%BB%D1%8C+%D0%B2+idr&oq=1+%D1%80%D1%83%D0%B1&gs_lcrp=EgZjaHJvbWUqCAgAEEUYJxg7MggIABBFGCcYOzIGCAEQRRg5MgoIAhAAGLEDGIAEMgcIAxAAGIAEMgcIBBAAGIAEMgcIBRAAGIAEMgcIBhAAGIAEMgYIBxBFGD2oAgCwAgA&sourceid=chrome&ie=UTF-8"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }

    req = requests.get(url, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    new = soup.find_all(class_="DFlfde SwHCTb")
    for _ in new:
        lists.append(_.text)
    with open("pars.txt", "a") as file:
        file.write(f"{lists[0]}")
    with open("pars.txt", "r") as file:
        cursss = file.read()
        print(cursss.replace(',', '.'))
        await message.answer(f"Здравствуйте, готовы сделать обмен при личной встрече, доставка до двери!\n"
              f"➡️Мы предлагаем самые выгодные условия по сделке на Бали, если Вы нашли более выгодный "
              f"курс, присылайте нам скрины, мы создадим для Вас  более выгодные условия по обмену✔\n\n"
              f"⚠️актуальный курс на сегодня:\n"
              f"✅10.000 ₽ - 50.000₽ - "
              f"{round(float(cursss.replace(',', '.')) - (float(cursss.replace(',', '.')) * 0.055), 2)} IDR\n"
              f"✅50.000 ₽ - 100.000₽ - "
              f"{round(float(cursss.replace(',', '.')) - (float(cursss.replace(',', '.')) * 0.05), 2)} IDR\n"
              f"✅100.000 ₽ -300.000₽ - "
              f"{round(float(cursss.replace(',', '.')) - (float(cursss.replace(',', '.')) * 0.045), 2)} IDR\n"
              f"✅300.000 ₽ -500.000₽ - "
              f"{round(float(cursss.replace(',', '.')) - (float(cursss.replace(',', '.')) * 0.04), 2)} IDR\n"
              f"✅500.000 ₽ -1.000.000₽- "
              f"{round(float(cursss.replace(',', '.')) - (float(cursss.replace(',', '.')) * 0.035), 2)} IDR\n")
    with open("pars.txt", "w") as file:
        pass