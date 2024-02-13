import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config
from hand import router
from middlewares.middle import TechMidddle


async def main():
    bot = Bot(token=config.token[0], parse_mode=ParseMode.HTML)
    dp = Dispatcher(memory=MemoryStorage())
    # dp.message.middleware.register(TechMidddle())
    dp.include_router(router)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
