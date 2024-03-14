import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from func import sql_start
import config
from hand import router
from middlewares.antiflood import AntiFloodUsers
from middlewares.black_list import BlackListUsers
from middlewares.subscribe import Subscrube
#vbnm
async def main():
    bot = Bot(token=config.token[0], parse_mode=ParseMode.HTML)
    dp = Dispatcher(memory=MemoryStorage())
    # dp.message.middleware.register(Subscrube())
    dp.message.middleware.register(AntiFloodUsers())
    dp.message.middleware.register(BlackListUsers())

    dp.include_router(router)
    sql_start()
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                        format= "%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
                        encoding="UTF-8")
    asyncio.run(main())
