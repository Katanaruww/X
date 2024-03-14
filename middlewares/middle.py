from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Dict, Any, Callable, Awaitable
from routers import check_tech
#dfghjkl


# class CounterMiddleware(BaseMiddleware):
#     def __init__(self) -> None:
#         self.counter = 0
#
#     async def __call__(
#         self,
#         handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
#         event: Message,
#         data: Dict[str, Any]
#     ) -> Any:
#         self.counter += 1
#         data['counter'] = self.counter
#         return await handler(event, data)

class TechMidddle(BaseMiddleware):


    async def __call__(
                self,
                handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                msg: Message,
                data: Dict[str, Any]) -> Any:
            row = await check_tech()
            if row[1] == 1:
                await msg.answer("<b>Технический перерыв.\n"
                                 "Попробуйте позже:(</b>")





