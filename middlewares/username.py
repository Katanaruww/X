from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Dict, Any, Callable, Awaitable
#rftghjk

class CancelHandler(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]) -> Any:

        if not event.from_user.username:
            await event.answer("RU:   У вас нет username. Пожалуйста, установите его в настройках Telegram.\n\nEN:   You don't have a username. Please install it in Telegram.")
        else:
            return await handler(event, data)
