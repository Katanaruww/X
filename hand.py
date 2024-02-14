import logging

from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import FSInputFile
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import types
from aiogram import F
from func import send_broadcast2, send_broadcast
import config
from inline_but import *
from routers import start_db, check_us
from inline_but import admin_but_send, admin_bc_fsm, admin_bc_fsm2

from func import get_user_value
# from func import start_menu, check_admin
router = Router()


class fsm(StatesGroup):
    adm_id = State()

class Form(StatesGroup):
    description1 = State()
    photo_adm = State()


class Form2(StatesGroup):
    description0 = State()
bot = Bot(config.token[0])


@router.message(Command("start"))
async def start_handler(msg: Message):
    try:
        await get_user_value(msg.from_user.id)
        check = await check_us(msg.chat.id)
        print(check)
        if check is not None:
            try:
                photo = FSInputFile("media/logo.png")
                await msg.answer_photo(
                    caption=f"<b>Добро пожаловать, <i>{msg.chat.first_name}</i></b>",
                    reply_markup=start_but().as_markup(), photo=photo)
            except Exception as err:
                logging.warning(err)
        else:
            await msg.answer("<b>тут будут правила</b>", reply_markup=rules().as_markup())
    except Exception as e:
        logging.exception(e)

@router.message(Command("rate"))
async def rate(msg: Message):
    pass
@router.message(Command("admin"))
async def admin(msg: Message):
    try:
        if msg.chat.id in config.admins:
            await msg.answer("<b><i>Админ-панель</i></b>", reply_markup=admin_but().as_markup())
        else:
            await msg.answer("<b>Ты не админ!</b>")
    except Exception as err:
        logging.exception(err)



@router.callback_query(lambda call: True)
async def cal(call, state: FSMContext):
    if call.data == "agree_rules":
        try:
            await start_db(call.message.chat.id, call.message.chat.username, call.message.chat.first_name)
            photo = FSInputFile("media/logo.png")
            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            await call.message.answer_photo(caption=f"<b>Добро пожаловать, <i>{call.message.chat.first_name}</i></b>",
                                            reply_markup=start_but().as_markup(), photo=photo)
        except Exception as err:
            logging.exception(err)
    elif call.data == "send":
        try:
            await call.message.edit_text(text="Выберите способ рассылки", reply_markup=admin_but_send().as_markup())
        except Exception as err:
            logging.exception(err)
    elif call.data == "send2":
        try:
            await call.message.answer(f'Введите текст рассылки')
            await state.set_state(Form2.description0)
        except Exception as err:
            logging.exception(err)
    elif call.data == "yes":
        await send_broadcast2(user_data['name'])
    elif call.data == "send1":
        try:
            await call.message.answer(f'Введите текст рассылки')
            await state.set_state(Form.description1)
        except Exception as err:
            logging.exception(err)
    elif call.data == "yes2":
        formatted_text = []
        [
            formatted_text.append(f"{value}")
            for key ,value in data.items()
        ]
        await send_broadcast(photo_url=photo_file_id, message_text=f"\n".join(formatted_text))

    ### АДМИНКА #### НИЖЕ НЕ ЛЕЗТЬ
    elif call.data == "adm_exc":
        await call.message.edit_text("<b>Админ-панель для обменника</b>", reply_markup=admin_exc().as_markup())

@router.message(Form2.description0)
async def get_userr(message: types.Message, state: FSMContext):
    try:
        await state.update_data(name=message.text)
        global user_data
        user_data = await state.get_data()
        await message.answer(
            text=f"Ваш текст:\n{user_data['name']}.\n\nОтправить сообщение пользователям?",reply_markup=admin_bc_fsm(
            ).as_markup())
        # Сброс состояния и сохранённых данных у пользователя
        await state.clear()
    except Exception as err:
        logging.exception(err)
        await message.answer(f'Сначала создайте сообщение')
@router.message(Form.description1)
async def get_adn(message: types.Message, state: FSMContext):
    try:
        await state.update_data(about=message.text)
        await message.answer(f'Отправьте фотографию')
        await state.set_state(Form.photo_adm)
    except Exception as err:
        logging.exception(err)
@router.message(Form.photo_adm, F.photo)
async def get_photo(message: types.Message, state: FSMContext):
    try:
        global photo_file_id
        photo_file_id = message.photo[-1].file_id
        global data
        data = await state.get_data()
        await state.clear()
        global formatted_text

        formatted_text = []
        [
            formatted_text.append(f"{key}: {value}")
            for key, value in data.items()
        ]
        await message.answer_photo(
            photo_file_id,
            "\n".join(formatted_text),reply_markup=admin_bc_fsm2(
            ).as_markup()

        )
    except Exception as err:
        logging.exception(err)

@router.message(Form.photo_adm, ~F.photo)
async def get_photo(message: types.Message, state: FSMContext):
    await message.answer(f'Отправь фотографию!')
@router.message(Form.description1, ~F.text)
async def get_trext(message: types.Message, state: FSMContext):
    await message.answer(f'Отправь текст!')