from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Dict, Any, Callable, Awaitable
from cachetools import TTLCache
from inline_but import sub
#edrfghjk
class Subscrube(BaseMiddleware):

    async def __call__(
                self,
                handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                event: Message,
                data: Dict[str, Any]) -> Any:

                    chat_member = await event.bot.get_chat_member("@lucky_bali_group",
                                                                  user_id=event.from_user.id)

                    if chat_member.status == "left":
                        await event.answer(
                            "Подпишитесь на канал, чтобы использовать функционал бота!",
                            reply_markup=sub().as_markup()
                        )
                    else:
                        return await handler(event, data)