from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Dict, Any, Callable, Awaitable
from cachetools import TTLCache


class AntiFloodUsers(BaseMiddleware):

    def __init__(self, time_sleep: int = 2) -> None:
        self.limit = TTLCache(maxsize=10_000, ttl=time_sleep)

    async def __call__(
                self,
                handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                event: Message,
                data: Dict[str, Any]) -> Any:
                    if event.chat.id in self.limit:
                        return
                    else:
                        self.limit[event.chat.id] = None
                    return await handler(event, data)