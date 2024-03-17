from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Dict, Any, Callable, Awaitable
from func import ban_users_us2, check_bans2
import logging
#dfghjk
class BlackListUsers2(BaseMiddleware):

    async def __call__(
                self,
                handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                event: Message,
                data: Dict[str, Any]) -> Any:
            row = await check_bans2()
            if event.chat.id in row:
                await ban_users_us2(event, event.chat.id)
            else:
                return await handler(event, data)