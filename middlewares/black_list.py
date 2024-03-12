from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Dict, Any, Callable, Awaitable
from func import ban_users_us, check_bans
import logging

class BlackListUsers(BaseMiddleware):

    async def __call__(
                self,
                handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                event: Message,
                data: Dict[str, Any]) -> Any:
            row = await check_bans()
            if event.chat.username in row:
                await ban_users_us(event, event.chat.username)
            else:
                return await handler(event, data)