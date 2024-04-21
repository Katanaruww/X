import logging
from translate import _
from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import FSInputFile
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import types
from aiogram import F
from func import send_broadcast2, send_broadcast, ban_us, ban_us2
import config
from inline_but import *
from routers import (start_db, check_us, add_lang, check_lang, db_rep_lang, add_amount_deals_onl, add_cards_start,
                     add_rekv_cards)
from inline_but import admin_but_send, admin_bc_fsm, admin_bc_fsm2, ban, add_cur_offline
from function import get_pars
from func import (get_user_value, replace_language, start_c, deals_online_start,
                  deals_online_type_add, deals_online_cancel, get_messa, deals_add_curr,
                  deals_add_curr_finish,
                  ban_users_us, check_bans, get_black_list, transaction_con, continue_in_deals, choose_pay_method)
from cards import (add_currency_card, add_start_card, cancel_add_card, add_type_pay_exc_admin, get_start_card,
                   get_list_card, print_list_card, see_card, activate_card)
from func import get_cur, get_cur2, get_messs, get_cb
from aiogram import Bot, Dispatcher, types
from limits import limits_currency_pairs
router = Router()

bot = Bot(token="6990593953:AAFNKnRYT7Rqke31xTTucDBtnz0N94GHSH8")
# Диспетчер
dp = Dispatcher()
class fsm(StatesGroup):
    adm_id = State()
    set_amount = State()
    call_id = State()
    min_am = State()
    call_id_cards = State()
    rekv = State()
    rekv_us = State()

class DealState(StatesGroup):
    choosing_currency = State()
    currency1 = State()
    choosing_currency2 = State()
    rate = State()
    gps = State()
    time = State()

class Form(StatesGroup):
    description1 = State()
    photo_adm = State()


class Form2(StatesGroup):
    description0 = State()

class Black_list(StatesGroup):
    black_user = State()

class Black_list2(StatesGroup):
    black_id = State()

bot = Bot(config.token[0])

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s", encoding="UTF-8")



@router.message(Command("start"))
async def start_handler(msg: Message):
    try:
        await get_user_value(msg.from_user.id)
        check = await check_us(msg.chat.id)
        if check is not None:
            try:
                photo = FSInputFile("media/logo.png")
                lang = await check_lang(msg.chat.id)
                await msg.answer_photo(
                    caption=f"<b>{_('Добро пожаловать', lang[0])}, <i>{msg.chat.first_name}</i></b>",
                    reply_markup=start_but(lang[0]).as_markup(), photo=photo)
            except Exception as err:
                logging.warning(err)
        else:
            await start_db(msg.chat.id, msg.chat.username, msg.chat.first_name)
            await msg.answer("<b>RU:</b> <i>Выберите язык</i>\n"
                             "<b>EN:</b> <i>Choose language</i>", reply_markup=lang_btn().as_markup())
    except Exception as e:
        logging.exception(e)

@router.message(Command("rate"))
async def rate(msg: Message):
    await get_pars(msg)


@router.callback_query(DealState.choosing_currency2, lambda call: call.data)
async def rextryftugiu(call, state: FSMContext):
    try:
        global curs2
        global currency
        lang = await check_lang(call.message.chat.id)
        await state.update_data(nameban=call.data)
        ban_user = await state.get_data()


        ifcur = str(ban_user["nameban"])
        curs2 = str(ban_user["nameban"]).replace("1", "")
        print(ifcur, curs2)


        if ifcur == "RUB1" or ifcur == "IDR1" or ifcur == "USD1" or ifcur == "USDT1" or ifcur == "BTC1" or ifcur == "LTC1":
            if curs2 == curs:

                await call.message.edit_text(f'<b><i>{_(text="Невозможно обменять одинаковою валюту!", lang=lang[0])}</i></b>')
                await state.clear()
                return  # Завершаем функцию, если валюты одинаковые

            currency = await get_cur2(amount=currens["name"], val_in=curs, val_out=curs2, call=call, state=state)

            if currency:

                await call.message.edit_text(currency)

                await state.clear()
            else:

                await state.clear()
        else:
            await state.clear()
    except Exception as err:
        logging.exception(err)
        await state.clear()


# ЭТО КОРОЧЕ ОТСЛЕЖАНИЕ КОЛЛБЕКА НАХУЙ
@router.callback_query(DealState.choosing_currency, lambda call: call.data)
async def swertyhbubh(call, state: FSMContext):
    try:
        global curs
        lang = await check_lang(call.message.chat.id)
        await state.update_data(nameban=call.data)
        ban_user = await state.get_data()
        curs = str(ban_user["nameban"]).replace("1", "")
        off = str(ban_user["nameban"])
        if off == "RUB1" or off == "IDR1" or off == "USD1" or off == "USDT1" or off == "BTC1" or off == "LTC1":
            currency = await get_cur(curs, call)
            await call.message.edit_text(currency)
            await get_messs(curs, call)
            await state.set_state(DealState.currency1)
        else:
            lang = await check_lang(call.message.chat.id)
            await call.message.edit_text(f"<b>{_('Выберите интересующие направление для вас:', lang[0])}</b>",
                                         reply_markup=add_cur_offline(lang).as_markup())
            await state.clear()
    except Exception as e:
        print(f"Произошла ошибка: {e}")




    except Exception as err:
        logging.exception(err)

@router.message(DealState.currency1)
async def zrextcyvgubhi(message: types.Message, state: FSMContext):
    try:
        global name
        lang = await check_lang(message.chat.id)
        # Проверяем, состоит ли сообщение только из цифр
        if float(message.text):
            global currens
            await state.update_data(name=message.text)
            currens = await state.get_data()

            name = await limits_currency_pairs(f"{curs}")
            if float(currens["name"]) < float(name[0]):
                await message.answer(
                    f'<b><i>{_(text="Вы ввели не правильное значение. Минимальное значение - ", lang=lang[0])} {name[0]}</i></b>')
                await state.set_data({})
                await state.clear()
            else:
                # await message.answer(
                #     f'<b><i>{_(text="Вы выбрали обмен на - ", lang=lang[0])} {curs}, {_(text="на сумму -", lang=lang[0])} {currens["name"]}</i></b>')
                # await message.answer(f'{_(text="Отлично! Двжемся дальше", lang=lang[0])}')
                await message.answer(
                    f"<b>{_('Выберите интересующие направление для обмена на - ', lang[0])} {curs}</b>",
                    reply_markup=oflline2(lang).as_markup())
                await state.set_state(DealState.choosing_currency2)
        else:
            await message.answer(f"{_(text='Пожалуйста, введите сумму чисел (только цифры).', lang=lang[0])}")
    except Exception as err:
        logging.exception(err)

# ЭТО КОРОЧЕ ПРОВЕРКА НАХУЙ
@router.message(DealState.currency1, ~F.text)
async def get_trext(message: types.Message, state: FSMContext):
    await message.answer(f'Отправь текст!')
    await state.clear()


@router.message(Command("admin"))
async def admin(msg: Message):
    try:
        if msg.chat.id in config.admins:
            await msg.answer("<b><i>Админ-панель</i></b>", reply_markup=admin_but().as_markup())
        else:
            await msg.answer("<b>Ты не админ!</b>")
    except Exception as err:
        logging.exception(err)


@router.callback_query(lambda call: call.data and call.data.startswith("lang_"))
async def lang(call):
    try:
        lang = call.data[5:]
        await add_lang(lang, call.message.chat.id)
        await call.message.edit_text(f"<b>тут будут правила</b>", reply_markup=rules(lang).as_markup())
    except Exception as e:
        logging.exception(e)


@router.callback_query(lambda call: call.data and call.data.startswith("change_"))
async def lang(call):
    await replace_language(call)

@router.callback_query(lambda call: call.data and call.data.startswith("type_"))
async def lang(call):
    try:
        await deals_online_type_add(call, "start")
    except Exception as e:
        logging.exception(e)

@router.callback_query(lambda call: call.data and call.data.startswith("cancel-deal_"))
async def lang(call):
    try:
        await deals_online_cancel(call)
    except Exception as e:
        logging.exception(e)


@router.callback_query(lambda call: call.data and call.data.startswith("print-RUB-cards_"))
async def lang(call):
    try:
        await choose_pay_method(call)
    except Exception as e:
        logging.exception(e)


@router.callback_query(lambda call: call.data and call.data.startswith("continue-deals_"))
async def lang(call):
    try:
        await continue_in_deals(call)
    except Exception as e:
        logging.exception(e)
@router.callback_query(lambda call: call.data and call.data.startswith("cancel-card_"))
async def lang(call):
    try:
        await cancel_add_card(call)
    except Exception as e:
        logging.exception(e)
@router.callback_query(lambda call: call.data and call.data.startswith("give_"))
async def lang(call):
    try:
        await deals_add_curr(call)
    except Exception as e:
        logging.exception(e)

@router.callback_query(lambda call: call.data and call.data.startswith("get_"))
async def lang(call, state: FSMContext):
    try:
        call_id = await deals_add_curr_finish(call, state)
        print(call_id)
        await state.update_data(min_am=call_id[1])
        await state.update_data(call_id=call_id[0])
        await state.set_state(fsm.set_amount)
    except Exception as e:
        logging.exception(e)


@router.callback_query(lambda call: call.data and call.data.startswith("get-cards_"))
async def car(call):
    try:
        await get_list_card(call)
    except Exception as e:
        logging.exception(e)
@router.callback_query(lambda call: call.data and call.data.startswith("add-cards_"))
async def card(call, state: FSMContext):
    try:
        call_id = await add_currency_card(call)
        await state.update_data(call_id_cards=call_id)
        await state.set_state(fsm.rekv)
    except Exception as e:
        logging.exception(e)


@router.callback_query(lambda call: call.data and call.data.startswith("add-RUB-cards_"))
async def card(call, state: FSMContext):
    try:
        print(call.data)
        call_id = await add_type_pay_exc_admin(call)
        await state.update_data(call_id_cards=call_id)
        await state.set_state(fsm.rekv)
    except Exception as e:
        logging.exception(e)


@router.callback_query(lambda call: call.data and call.data.startswith("get-RUB-cards_"))
async def card(call, state: FSMContext):
    try:
        type_v = call.data.split("-")[1]
        v = call.data.split("_")[1]
        print(v)
        await print_list_card(call, type_v, v)
    except Exception as e:
        logging.exception(e)


@router.callback_query(lambda call: call.data and call.data.startswith("see-card_"))
async def card(call, state: FSMContext):
    try:
        await see_card(call)
    except Exception as e:
        logging.exception(e)


@router.callback_query(lambda call: call.data and call.data.startswith("activate-card_"))
async def card(call, state: FSMContext):
    try:
        await activate_card(call)
    except Exception as e:
        logging.exception(e)
@router.callback_query(lambda call: True)
async def cal(call, state: FSMContext):
    if call.data == "agree_rules":
        try:
            await start_c(call)
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
            for key, value in data.items()
        ]
        await send_broadcast(photo_url=photo_file_id, message_text=f"\n".join(formatted_text))
    elif call.data == "setting":
        lang = await check_lang(call.message.chat.id)
        photo = FSInputFile("media/x.jpg")
        await call.message.edit_caption(
            caption=f"<b><i>{_('Настройки', lang[0])}</i></b>",
            reply_markup=setting_btn(call, lang[0]).as_markup(), photo=photo)
    elif call.data == "back_start":
        try:
            await start_c(call)
        except Exception as err:
            logging.exception(err)
    elif call.data == "no":
        try:
            await start_c(call)
        except Exception as err:
            logging.exception(err)
    elif call.data == "no2":
        try:
            await start_c(call)
        except Exception as err:
            logging.exception(err)
    # ПРОЦЕСС СОЗДАНИ ОФЛАЙН ЗАКАЗА
    elif call.data == "offline_deals":
        try:
            lang = await check_lang(call.message.chat.id)
            await call.message.edit_text(f"<b>{_('Выберите интересующие направление для вас:', lang[0])}</b>",
                                             reply_markup=add_cur_offline(lang).as_markup())

        except Exception as err:
            logging.exception(err)
    elif call.data == "start_offline":
        try:
            lang = await check_lang(call.message.chat.id)
            await call.message.edit_text(f"<b>{_('Выберите интересующие направление для вас:', lang[0])}</b>",
                                             reply_markup=oflline(lang).as_markup())
            await state.set_state(DealState.choosing_currency)
        except Exception as err:
            logging.exception(err)

    elif call.data == "deal":
        try:
            await get_messa(call)
        except Exception as err:
            logging.exception(err)
    elif call.data == "back_state":
        await get_cb(call=call, state=state)

    elif call.data == "adm_usr":
        try:
            await call.message.answer(f'Введите username пользователя для бана\nНапример: qwerty')
            await state.set_state(Black_list.black_user)
            await call.message.answer(f'Введи текст')
        except Exception as err:
            logging.exception(err)
    elif call.data == "black_list":
        try:
            await get_black_list(call)
        except Exception as err:
            logging.exception(err)
    elif call.data == "adm_id":
        try:
            await call.message.answer(f'Введите id пользователя для бана\nНапример: 123456')
            await state.set_state(Black_list2.black_id)
        except Exception as err:
            logging.exception(err)







    ## ПРОЦЕСС СОЗДАНИЯ СДЕЛКИ ####
    elif call.data == "exch":
        try:
            await deals_online_start(call)
        except Exception as err:
            logging.exception(err)
    elif call.data == "online_deals":
        try:
            await deals_online_type_add(call)
        except Exception as err:
            logging.exception(err)
    ### КОНЕЦ СОЗДАНИЯ СДЕЛКИ ###


    ### АДМИНКА #### НИЖЕ НЕ ЛЕЗТЬ
    elif call.data == "adm_exc" or call.data == "back_admin":
        await call.message.edit_text("<b>Админ-панель для обменника</b>", reply_markup=admin_exc().as_markup())
    elif call.data == "add_cards":
        try:
            await add_start_card(call)
        except Exception as err:
            logging.exception(err)
    elif call.data == "see_cards":
        try:
            await get_start_card(call)
        except Exception as err:
            logging.exception(err)





"""ЭТО ОФФЛАЙН НАХУЙ"""







"""ЭТО КОНЕЦ ОФФЛАЙН НАХУЙ"""

@router.message(Black_list2.black_id)
async def get_userr(message: types.Message, state: FSMContext):
    try:
        await state.update_data(nameban=message.text)
        ban_user = await state.get_data()
        await ban_us2(ban_user["nameban"])
        await message.answer(f'Юзер - {ban_user["nameban"]} успешно забанен')
    except Exception as err:
        logging.exception(err)


@router.message(Black_list.black_user)
async def get_userr(message: types.Message, state: FSMContext):
    try:
        await state.update_data(nameban=message.text)
        ban_user = await state.get_data()
        await ban_us(ban_user["nameban"])
        await message.answer(f'Юзер - {ban_user["nameban"]} успешно забанен')
    except Exception as err:
        logging.exception(err)

@router.message(Form2.description0)
async def get_userr(message: types.Message, state: FSMContext):
    try:
        await state.update_data(name=message.text)
        global user_data
        user_data = await state.get_data()
        await message.answer(
            text=f"Ваш текст:\n{user_data['name']}.\n\nОтправить сообщение пользователям?", reply_markup=admin_bc_fsm(
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
            "\n".join(formatted_text), reply_markup=admin_bc_fsm2(
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

@router.message(fsm.set_amount)
async def setrt(message: types.Message, state: FSMContext):
    try:
        await state.update_data(set_amount=message.text)
        data = await state.get_data()
        amount_get = round(float(data["set_amount"]))
        call_id = data["call_id"]
        lang = await check_lang(message.chat.id)
        min_am = data["min_am"]
        if amount_get >= min_am:
            await message.answer(f"<b>{_('Очень хорошо', lang[0])}!</b>\n"
                                 f"<i>{_('Введите реквизиты, на который вам отправить средства', lang[0])}:</i>",
                                 reply_markup=exc_btn_cancel(call_id, lang[0]).as_markup())
            await state.set_state(fsm.rekv_us)
        else:
            await state.clear()
            await message.answer(f"<b>Нахуй пошел! Русским языком сказали же минимум {min_am}</b>")
            await state.set_state(fsm.set_amount)
    except Exception as e:
        logging.exception(e)


@router.message(fsm.rekv_us)
async def setrt(message: types.Message, state: FSMContext):
    try:
        await state.update_data(rekv_us=message.text)
        data = await state.get_data()
        amount_get = round(float(data["set_amount"]))
        call_id = data["call_id"]
        rekv_user_get = data["rekv_us"]
        print(call_id, amount_get, rekv_user_get)
        await add_amount_deals_onl(call_id, amount_get, rekv_user_get)
        await transaction_con(message, call_id)
        await state.clear()
    except Exception as e:
        logging.exception(e)
@router.message(fsm.rekv)
async def setrt(message: types.Message, state: FSMContext):
    try:
        await state.update_data(rekv=message.text)
        data = await state.get_data()
        rekv_get = data["rekv"]
        call_id = data["call_id_cards"]
        print(rekv_get, call_id)

        await add_rekv_cards(rekv_get, call_id)
        await message.answer(f"<b>Успешно!</b>\n"
                             f"<i>Добавим еще реквизит?</i>", reply_markup=admin_exc().as_markup())
        await state.clear()
        await state.set_state(fsm.set_amount)
    except Exception as e:
        logging.exception(e)
