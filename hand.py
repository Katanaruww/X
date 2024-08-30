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
                     add_rekv_cards, print_deals)
from inline_but import admin_but_send, admin_bc_fsm, admin_bc_fsm2, ban, add_cur_offline
from function import get_pars
from func import (get_user_value, replace_language, start_c, deals_online_start,
                  deals_online_type_add, deals_online_cancel, get_messa, deals_add_curr,
                  deals_add_curr_finish,
                  ban_users_us, check_bans, get_black_list, transaction_con, continue_in_deals, choose_pay_method,
                  send_deals, get_pars2, accept_in_deals, get_average_rating, final_deals, cancel_final_deals, add_values, add_values2, add_values3, add_values4, add_values5, add_values6, add_values7, add_values8, add_values10, add_values9)
from cards import (add_currency_card, add_start_card, cancel_add_card, add_type_pay_exc_admin, get_start_card,
                   get_list_card, print_list_card, see_card, activate_card)
from func import get_cur, get_cur2, get_messs, get_cb, send_reviews
from aiogram import Bot, Dispatcher, types
from limits import limits_currency_pairs
import check_address
import datetime
from dop_func.func_float import format_number
from aiogram.enums.parse_mode import ParseMode
import traceback
from currre import get_pars5
router = Router()

bot = Bot(token="6990593953:AAFNKnRYT7Rqke31xTTucDBtnz0N94GHSH8")
# Диспетчер
dp = Dispatcher()

class Direction1(StatesGroup):
    price1 = State()
    price2 = State()
    price3 = State()
    price4 = State()
    price5 = State()
class Direction2(StatesGroup):
    price1 = State()
    price2 = State()
    price3 = State()
    price4 = State()
    price5 = State()
class USDT(StatesGroup):
    price1 = State()
class Direction3(StatesGroup):
    price1 = State()
    price2 = State()
    price3 = State()
    price4 = State()
    price5 = State()

class BTCLTC(StatesGroup):
    price1 = State()
class BTCRUB(StatesGroup):
    price1 = State()
class BTCIDR(StatesGroup):
    price1 = State()
class LTCRUB(StatesGroup):
    price1 = State()
class LTCIDR(StatesGroup):
    price1 = State()
class BTCUSD(StatesGroup):
    price1 = State()
class LTCUSD(StatesGroup):
    price1 = State()
class ActCurs(StatesGroup):
    choosing_currency = State()
    currency1 = State()
    choosing_currency2 = State()
    rate = State()
    gps = State()
    geo = State()
    time = State()
    yesorno = State()
    yesornogps = State()
    nalbeznal = State()
    nalbeznal2 = State()

class fsm(StatesGroup):
    adm_id = State()
    set_amount = State()
    call_id = State()
    min_am = State()
    call_id_cards = State()
    rekv = State()
    rekv_us = State()
    reason = State()
    id_deal = State()


class DealState(StatesGroup):
    choosing_currency = State()
    currency1 = State()
    choosing_currency2 = State()
    rate = State()
    gps = State()
    geo = State()
    time = State()
    yesorno = State()
    yesornogps = State()
    nalbeznal = State()
    nalbeznal2 = State()

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

# Словарь для хранения задач сброса состояния для каждого пользователя
reset_tasks = {}

async def reset_user_state(user_id: int, state: FSMContext):
    await asyncio.sleep(300)  # 5 минут
    current_state = await state.get_state()
    if current_state is not None:
        await state.clear()
    # Удаляем задачу из словаря после выполнения
    reset_tasks.pop(user_id, None)
async def create_reset_task(user_id: int, state: FSMContext):
    # Отменяем предыдущую задачу сброса, если она существует
    if user_id in reset_tasks:
        reset_tasks[user_id].cancel()
    # Создаем новую задачу сброса состояния
    reset_tasks[user_id] = asyncio.create_task(reset_user_state(user_id, state))
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



@router.callback_query(DealState.yesorno, lambda call: call.data)
async def swertyhbubh(call, state: FSMContext):
    try:
        global ggg
        lang = await check_lang(call.message.chat.id)
        await state.update_data(nameban=call.data)
        laaaag = await get_pars2(curs, curs2, int(su))
        ban_user = await state.get_data()
        ggg = str(ban_user["nameban"])
        current_time = datetime.datetime.now()
        if ggg in {"yesgeo"}:
            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

            await call.message.answer(
                f"<b>{_('Ваша заявка успешно сохранена\nВ скором времени с вами свяжется курьер!', lang[0])}</b>")
            await bot.send_message(chat_id=-1002244398985,
                                   text=f"<b>New application!\n\nID - {call.from_user.id}\nUsername - {call.from_user.username}\n{_("Обмениваете - ", lang[0])} {su} {curs} 💳\n{_("Получаете - ", lang[0])} {format_number(float(laaaag), curs2)} {curs2} 💳\n\n{_("Ваш район - ", lang[0])} {_(f"{geo}", lang[0])} 🏠\n\nСalculation - {_(f"{ifbez}", lang[0])}\n\nTime deals - {current_time} 🧭</b>",parse_mode=ParseMode.HTML,
                                   reply_markup=get_curiers(call.from_user.id).as_markup())
            await state.clear()
            if call.from_user.id in reset_tasks:
                reset_tasks[call.from_user.id].cancel()
                reset_tasks.pop(call.from_user.id)
        if ggg in {"nogeo"}:
            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            await call.message.answer(f"<b>{_("Ваша заявка успешно отменена", lang[0])}</b>")
            await state.clear()
            if call.from_user.id in reset_tasks:
                reset_tasks[call.from_user.id].cancel()
                reset_tasks.pop(call.from_user.id)
        if ggg in {"yesgps"}:
            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            await call.message.answer(
                f"<b>{_('Ваша заявка успешно сохранена\nВ скором времени с вами свяжется курьер!', lang[0])}</b>")
            await bot.send_message(chat_id=-1002244398985,
                                   text=f"<b>New application!\n\nID - {call.from_user.id}\nUsername - {call.from_user.username}\n{_("Обмениваете - ", lang[0])} {su} {curs} 💳\n{_("Получаете - ", lang[0])} {format_number(float(laaaag), curs2)} {curs2} 💳\n\n{_("Ваш район - ", lang[0])}<code>{f"{cu1} {cu2}"}</code> 🏠\n\nСalculation - {_(f"{ifbez}", lang[0])}\n\nTime deals - {current_time} 🧭</b>",parse_mode=ParseMode.HTML,
                                   reply_markup=get_curiers(call.from_user.id).as_markup())
            await state.clear()
            if call.from_user.id in reset_tasks:
                reset_tasks[call.from_user.id].cancel()
                reset_tasks.pop(call.from_user.id)
        if ggg in {"nogps"}:
            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            await call.message.answer(f"<b>{_("Ваша заявка успешно отменена", lang[0])}</b>")
            await state.clear()
            if call.from_user.id in reset_tasks:
                reset_tasks[call.from_user.id].cancel()
                reset_tasks.pop(call.from_user.id)
        else:
            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

            lang = await check_lang(call.message.chat.id)
            await call.message.answer(f"<b>{_('Выберите интересующие направление для вас:', lang[0])}</b>",
                                         reply_markup=add_cur_offline(lang).as_markup())
            await state.clear()

    except Exception as e:
        print(f"Произошла ошибка: {e}")

locations = {}

#
# @router.message(DealState.gps, F.location)
# async def location_handler(message: types.Message, state: FSMContext):
#     try:
#         global cu1
#         global cu2
#         global rai1
#         global rai2
#         global currens2
#         global currens3
#         latitude = message.location.latitude
#         longitude = message.location.longitude
#         locations['latitude'] = latitude
#         locations['longitude'] = longitude
#         act_cur = await get_pars2(curs, curs2, int(1))
#         cu1 = str(locations['latitude'])
#         cu2 = str(locations['longitude'])
#         await state.update_data(name=str(cu1))
#         await state.update_data(name2=str(cu2))
#         llllll = await get_pars2(curs, curs2, int(su))
#         lang = await check_lang(message.chat.id)
#         currens2 = await state.get_data()
#         currens3 = await state.get_data()
#         rai1 = currens2["name"]
#         rai2 = currens3["name2"]
#         # await message.answer(str(rai1))
#         # await message.answer(str(rai2))
#         await message.answer(
#             f"<b>{_(f'Отлично!\nПроверьте свои данные для оформления заявки', lang[0])}</b>\n<b><i>{_("Обмениваете - ", lang[0])} {su} {curs} 💳</i></b>\n<b><i>{_("Получаете - ", lang[0])} {format_number(float(llllll), curs2)} {curs2} 💳 </i></b>\n<b><i>{_("Актуальный курс", lang[0])} - {format_number(act_cur, curs2)} 💵</i></b>\n<i><b>{_("Расчёт", lang[0])}: {_(f"{ifbez}", lang[0])}💰</b></i>\n<b><i>{_("Ваш район - ", lang[0])} {f"{cu1} {cu2}"} 🏠</i></b>",
#             reply_markup=in_gps(lang).as_markup())
#         await state.set_state(DealState.yesorno)
#         await create_reset_task(message.from_user.id, state)
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")
@router.message(DealState.gps, F.location)
async def location_handler(message: types.Message, state: FSMContext):
    try:
        global cu1
        global cu2
        global rai1
        global rai2
        global currens2
        global currens3
        latitude = message.location.latitude
        longitude = message.location.longitude
        locations['latitude'] = latitude
        locations['longitude'] = longitude
        act_cur = await get_pars2(curs, curs2, int(1))
        cu1 = str(locations['latitude'])
        cu2 = str(locations['longitude'])
        await state.update_data(name=str(cu1))
        await state.update_data(name2=str(cu2))
        llllll = await get_pars2(curs, curs2, int(su))
        lang = await check_lang(message.chat.id)
        currens2 = await state.get_data()
        currens3 = await state.get_data()
        rai1 = currens2["name"]
        rai2 = currens3["name2"]

        await message.answer(
            f"<b>{_(f'Отлично!\nПроверьте свои данные для оформления заявки', lang[0])}</b>\n<b><i>{_("Обмениваете - ", lang[0])} {su} {curs} 💳</i></b>\n<b><i>{_("Получаете - ", lang[0])} {format_number(float(llllll), curs2)} {curs2} 💳 </i></b>\n<b><i>{_("Актуальный курс", lang[0])} - {format_number(act_cur, curs2)} 💵</i></b>\n<i><b>{_("Расчёт", lang[0])}: {_(f"{ifbez}", lang[0])}💰</b></i>\n<b><i>{_("Ваш район - ", lang[0])} {f"{cu1} {cu2}"} 🏠</i></b>",
            reply_markup=in_gps(lang).as_markup())

        await state.set_state(DealState.yesorno)
        await create_reset_task(message.from_user.id, state)
    except Exception as e:
        print(f"Произошла ошибка: {e}")


@router.message(DealState.gps, F.text)
async def text_handler(message: types.Message):
    lang = await check_lang(message.chat.id)

    await message.answer(f"<b>{_("Пожалуйста, отправьте своё местоположение, а не текст.", lang[0])}</b>", parse_mode=ParseMode.HTML)


@router.message(DealState.gps, F.photo)
async def photo_handler(message: types.Message):
    lang = await check_lang(message.chat.id)

    await message.answer(f"<b>{_("Пожалуйста, отправьте своё местоположение, а не фотографию.", lang[0])}<b>", parse_mode=ParseMode.HTML)


# @router.message(DealState.gps)
# async def default_handler(message: types.Message):
#     await message.answer("Пожалуйста, отправьте своё местоположение.")


@router.callback_query(DealState.geo, lambda call: call.data)
async def swertyhbubh(call, state: FSMContext):
    try:
        global geo
        lang = await check_lang(call.message.chat.id)
        await state.update_data(nameban=call.data)
        ban_user = await state.get_data()
        geo = str(ban_user["nameban"])
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        llllll = await get_pars2(curs, curs2, int(su))
        currency = await get_cur2(amount=currens["name"], val_in=curs, val_out=curs2, call=call, state=state)
        act_cur = await get_pars2(curs, curs2, int(1))
        if geo in {"Changu"}:
            geo = "Чангу"
            # await call.message.answer(text=currency, reply_markup=get_offline(lang).as_markup())
            await call.message.answer(
                f"<b>{_(f'Отлично!\nПроверьте свои данные для оформления заявки', lang[0])}</b>\n<b><i>{_("Обмениваете - ", lang[0])} {su} {curs} 💳</i></b>\n<b><i>{_("Получаете - ", lang[0])} {format_number(llllll, curs2)} {curs2} 💳 </i></b>\n<b><i>{_("Актуальный курс", lang[0])} - {format_number(act_cur, curs2)} 💵</i></b>\n<b><i>{_("Расчёт", lang[0])} - {_(f"{ifbez}", lang[0])}💰</i></b>\n<b><i>{_("Ваш район - ", lang[0])} {_(f"{geo}", lang[0])} 🏠</i></b>",
                reply_markup=inline_geo(lang).as_markup())
            await state.set_state(DealState.yesorno)
            await create_reset_task(call.from_user.id, state)
        if geo in {"Semen"}:
            geo = "Сменьяк"
            await call.message.answer(
                f"<b>{_(f'Отлично!\nПроверьте свои данные для оформления заявки', lang[0])}</b>\n<b><i>{_("Обмениваете - ", lang[0])} {su} {curs} 💳</i></b>\n<b><i>{_("Получаете - ", lang[0])} {format_number(llllll, curs2)} {curs2} 💳 </i></b>\n<b><i>{_("Актуальный курс", lang[0])} - {format_number(act_cur, curs2)} 💵</i></b>\n<b><i>{_("Расчёт", lang[0])} - {_(f"{ifbez}", lang[0])}💰</i></b>\n<b><i>{_("Ваш район - ", lang[0])} {_(f"{geo}", lang[0])} 🏠</i></b>",
                reply_markup=inline_geo(lang).as_markup())
            await state.set_state(DealState.yesorno)
            await create_reset_task(call.from_user.id, state)
        if geo in {"Ubud"}:
            geo = "Убуд"
            await call.message.answer(
                f"<b>{_(f'Отлично!\nПроверьте свои данные для оформления заявки\n', lang[0])}</b>\n<b><i>{_("Обмениваете - ", lang[0])} {su} {curs} 💳</i></b>\n<b><i>{_("Получаете - ", lang[0])} {format_number(llllll, curs2)} {curs2} 💳 </i></b>\n<b><i>{_("Актуальный курс", lang[0])} - {format_number(act_cur, curs2)} 💵</i></b>\n<b><i>{_("Расчёт", lang[0])} - {_(f"{ifbez}", lang[0])}💰</i></b>\n<b><i>{_("Ваш район - ", lang[0])} {_(f"{geo}", lang[0])} 🏠</i></b>",
                reply_markup=inline_geo(lang).as_markup())
            await state.set_state(DealState.yesorno)
            await create_reset_task(call.from_user.id, state)
        if geo in {"Geo"}:
            await call.message.answer(f"<b>{_('Отправьте свою геопозицию', lang[0])}</b>",
                                      reply_markup=dell_gps000(lang).as_markup())
            await state.set_state(DealState.gps)
            await create_reset_task(call.from_user.id, state)
        if geo in {"dell_gps"}:
            # await call.message.answer(f"<b>{_(text='Сделка отменена', lang=lang[0])}</b>🚫")
            await get_cb(call, state)
            # await state.clear()
        else:
            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

            lang = await check_lang(call.message.chat.id)
            await call.message.answer(f"<b>{_('Выберите интересующие направление для вас:', lang[0])}</b>",
                                      reply_markup=add_cur_offline(lang).as_markup())
            await state.clear()
    except Exception as e:
        print(f"Произошла ошибка: {e}")

@router.callback_query(DealState.nalbeznal, lambda call: call.data)
async def nalnal(call, state: FSMContext):
    try:
        global ifbez
        await state.update_data(nameban=call.data)
        ban_user = await state.get_data()
        ifbez = str(ban_user["nameban"])
        lang = await check_lang(call.message.chat.id)
        if ifbez in {"nal"}:
            ifbez = "Наличный расчёт"
            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            await call.message.answer(f'{_(text="В каком районе вы находитесь?", lang=lang[0])}',
                                      reply_markup=get_geo(lang).as_markup())
            await state.set_state(DealState.geo)
            await create_reset_task(call.from_user.id, state)
        if ifbez in {"beznal"}:
            ifbez = "Безналичный расчёт"
            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            await call.message.answer(f'{_(text="В каком районе вы находитесь?", lang=lang[0])}',
                                      reply_markup=get_geo(lang).as_markup())
            await state.set_state(DealState.geo)
            await create_reset_task(call.from_user.id, state)
        if ifbez in {"dell_geo"}:
            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            await get_cb(call, state)

    except Exception as err:
        logging.exception(err)


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

        if ifcur in {"RUB1", "IDR1", "USD1", "USDT1", "BTC1", "LTC1"}:
            if curs2 == curs:
                await call.message.edit_text(
                    f'<b><i>{_(text="Невозможно обменять одинаковою валюту!", lang=lang[0])}</i></b>')
                await state.clear()
                return  # Завершаем функцию, если валюты одинаковые

            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            currency = await get_cur2(amount=currens["name"], val_in=curs, val_out=curs2, call=call, state=state)

            if currency:
                await call.message.answer(f'{currency}\n\n{_(text="Выберете действие", lang=lang[0])}:', reply_markup=beznal(lang).as_markup())

                await state.set_state(DealState.nalbeznal)
                await create_reset_task(call.from_user.id, state)
            else:

                await state.clear()
        else:
            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

            lang = await check_lang(call.message.chat.id)
            await call.message.answer(f"<b>{_('Выберите интересующие направление для вас:', lang[0])}</b>",
                                         reply_markup=add_cur_offline(lang).as_markup())
            await state.clear()
    except Exception as err:
        logging.exception(err)
        await state.clear()

@router.callback_query(ActCurs.choosing_currency2, lambda call: call.data)
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

        if ifcur in {"RUB1", "IDR1", "USD1", "USDT1", "BTC1", "LTC1"}:
            if curs2 == curs:
                await call.message.edit_text(
                    f'<b><i>{_(text="Невозможно обменять одинаковою валюту!", lang=lang[0])}</i></b>')
                await state.clear()
                return  # Завершаем функцию, если валюты одинаковые

            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            await get_pars5(curs, curs2, 1, call)
            await state.clear()

        else:
            await start_c(call)
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
        if off in {"RUB1", "IDR1", "USD1", "USDT1", "BTC1", "LTC1"}:
            currency = await get_cur(curs, call)
            # await call.message.edit_text(currency)
            if currency == True:
                await get_messs(curs, call)
                await state.set_state(DealState.currency1)
                await create_reset_task(call.from_user.id, state)
            if currency == False:
                await call.message.edit_text(f"{_(text='Повторите попытку', lang=lang[0])}")
        else:
            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

            lang = await check_lang(call.message.chat.id)
            await call.message.answer(f"<b>{_('Выберите интересующие направление для вас:', lang[0])}</b>",
                                         reply_markup=add_cur_offline(lang).as_markup())
            await state.clear()
    except Exception as e:
        print(f"Произошла ошибка: {e}")

@router.callback_query(ActCurs.choosing_currency, lambda call: call.data)
async def swertyhbubh(call, state: FSMContext):
    try:
        global curs
        lang = await check_lang(call.message.chat.id)
        await state.update_data(nameban=call.data)
        ban_user = await state.get_data()
        curs = str(ban_user["nameban"]).replace("1", "")
        off = str(ban_user["nameban"])
        if off in {"RUB1", "IDR1", "USD1", "USDT1", "BTC1", "LTC1"}:
            currency = await get_cur(curs, call)
            # await call.message.edit_text(currency)
            if currency == True:
                await call.message.edit_text(
                    f"<b>{_('Выберите интересующие направление для обмена на - ', lang[0])} {curs}</b>",
                    reply_markup=oflline2(lang).as_markup())
                await state.set_state(ActCurs.choosing_currency2)
                await create_reset_task(call.from_user.id, state)
            if currency == False:
                await call.message.edit_text(f"{_(text='Повторите попытку', lang=lang[0])}")
        else:
            await start_c(call)
            await state.clear()
    except Exception as e:
        print(f"Произошла ошибка: {e}")






@router.message(DealState.currency1)
async def zrextcyvgubhi(message: types.Message, state: FSMContext):
    try:
        global name
        global su
        lang = await check_lang(message.chat.id)

        # Проверяем, состоит ли сообщение только из цифр
        try:
            amount = float(message.text)
        except ValueError:
            await message.answer(f"{_(text='Пожалуйста, введите сумму чисел (только цифры).', lang=lang[0])}")
            return

        global currens
        await state.update_data(name=message.text)
        currens = await state.get_data()
        su = currens["name"]
        name = await limits_currency_pairs(f"{curs}")

        if float(su) < float(name[0]):
            await message.answer(
                f'<b><i>{_(text="Вы ввели не правильное значение. Минимальное значение - ", lang=lang[0])} {name[0]}</i></b>')
            await state.set_state(DealState.currency1)
        else:
            await message.answer(
                f"<b>{_('Выберите интересующие направление для обмена на - ', lang[0])} {curs}</b>",
                reply_markup=oflline2(lang).as_markup())
            await state.set_state(DealState.choosing_currency2)
            await create_reset_task(message.from_user.id, state)
    except Exception as err:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

        await message.answer(f"{_(text='Произошла ошибка. Пожалуйста, попробуйте снова.', lang=lang[0])}")
        await state.clear()
        logging.exception(err)
@router.message(Direction2.price5)
async def swertyhbubh(message: types.Message, state: FSMContext):
    try:
        global price_number_5
        await state.update_data(nameban=message.text)
        ban_user = await state.get_data()
        price_number_5 = str(ban_user["nameban"])
        await add_values3(price_number_1, price_number_2, price_number_3, price_number_4, price_number_5)
        await message.answer("Курс успешно изменен!")
        await state.clear()
    except Exception as e:
        print(f"Произошла ошибка: {e}")
@router.message(Direction2.price4)
async def swertyhbubh(message: types.Message, state: FSMContext):
    try:
        global price_number_4
        await state.update_data(nameban=message.text)
        ban_user = await state.get_data()
        price_number_4 = str(ban_user["nameban"])
        await message.answer("Введите для значения 100,000,000 IDR - 300,000,000 IDR", reply_markup=dell_state_admin().as_markup())
        await state.set_state(Direction2.price5)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
@router.message(Direction2.price3)
async def swertyhbubh(message: types.Message, state: FSMContext):
    try:
        global price_number_3
        await state.update_data(nameban=message.text)
        ban_user = await state.get_data()
        price_number_3 = str(ban_user["nameban"])
        await message.answer("Введите для значения 50,000,000 IDR - 100,000,000 IDR ", reply_markup=dell_state_admin().as_markup())
        await state.set_state(Direction2.price4)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
@router.message(Direction2.price2)
async def swertyhbubh(message: types.Message, state: FSMContext):
    try:
        global price_number_2
        await state.update_data(nameban=message.text)
        ban_user = await state.get_data()
        price_number_2 = str(ban_user["nameban"])
        await message.answer("Введите для значения 30,000,000 IDR - 50,000,000 IDR ", reply_markup=dell_state_admin().as_markup())
        await state.set_state(Direction2.price3)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
@router.message(Direction2.price1)
async def swertyhbubh(message: types.Message, state: FSMContext):
    try:
        global price_number_1
        await state.update_data(nameban=message.text)
        ban_user = await state.get_data()
        price_number_1 = str(ban_user["nameban"])
        await state.set_state(Direction2.price2)


        await message.answer("Введите для значения 10,000,000 IDR - 30,000,000 IDR", reply_markup=dell_state_admin().as_markup())
    except Exception as e:
        print(f"Произошла ошибка: {e}")
@router.message(Direction1.price5)
async def swertyhbubh(message: types.Message, state: FSMContext):
    try:
        global price_number_5
        await state.update_data(nameban=message.text)
        ban_user = await state.get_data()
        price_number_5 = str(ban_user["nameban"])
        await add_values(price_number_1, price_number_2, price_number_3, price_number_4, price_number_5)
        await message.answer("Курс успешно изменен!")
        await state.clear()
    except Exception as e:
        print(f"Произошла ошибка: {e}")
@router.message(Direction1.price4)
async def swertyhbubh(message: types.Message, state: FSMContext):
    try:
        global price_number_4
        await state.update_data(nameban=message.text)
        ban_user = await state.get_data()
        price_number_4 = str(ban_user["nameban"])
        await message.answer("Введите для второго значения 500.000 ₽ - 1.000.000 ₽", reply_markup=dell_state_admin().as_markup())
        await state.set_state(Direction1.price5)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
@router.message(Direction1.price3)
async def swertyhbubh(message: types.Message, state: FSMContext):
    try:
        global price_number_3
        await state.update_data(nameban=message.text)
        ban_user = await state.get_data()
        price_number_3 = str(ban_user["nameban"])
        await message.answer("Введите для второго значения 300.000 ₽ - 500.000 ₽", reply_markup=dell_state_admin().as_markup())
        await state.set_state(Direction1.price4)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
@router.message(Direction1.price2)
async def swertyhbubh(message: types.Message, state: FSMContext):
    try:
        global price_number_2
        await state.update_data(nameban=message.text)
        ban_user = await state.get_data()
        price_number_2 = str(ban_user["nameban"])
        await message.answer("Введите для второго значения 100.000 ₽ - 300.000 ₽", reply_markup=dell_state_admin().as_markup())
        await state.set_state(Direction1.price3)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
@router.message(Direction1.price1)
async def swertyhbubh(message: types.Message, state: FSMContext):
    # try:
        global price_number_1
        await state.update_data(nameban=message.text)
        ban_user = await state.get_data()
        price_number_1 = str(ban_user["nameban"])
        await state.set_state(Direction1.price2)


        await message.answer("Введите для второго значения 50.000 ₽ - 100.000 ₽", reply_markup=dell_state_admin().as_markup())
    # except Exception as e:
    #     print(f"Произошла ошибка: {e}")
@router.message(USDT.price1)
async def swertyhbubh(message: types.Message, state: FSMContext):
    try:
        global price_number_2
        await state.update_data(nameban=message.text)
        ban_user = await state.get_data()
        price_number_2 = str(ban_user["nameban"])
        await add_values2(str(price_number_2))
        await state.clear()
        await message.answer(f'Курс изменен!')
    except Exception as e:
        print(f"Произошла ошибка: {e}")
@router.message(BTCRUB.price1)
async def swertyhbubh(message: types.Message, state: FSMContext):
    try:
        global price_number_2
        await state.update_data(nameban=message.text)
        ban_user = await state.get_data()
        price_number_2 = str(ban_user["nameban"])
        await add_values4(str(price_number_2))
        await state.clear()
        await message.answer(f'Курс изменен!')
    except Exception as e:
        print(f"Произошла ошибка: {e}")

@router.message(BTCIDR.price1)
async def swertyhbubh(message: types.Message, state: FSMContext):
    try:
        global price_number_2
        await state.update_data(nameban=message.text)
        ban_user = await state.get_data()
        price_number_2 = str(ban_user["nameban"])
        await add_values5(str(price_number_2))
        await state.clear()
        await message.answer(f'Курс изменен!')
    except Exception as e:
        print(f"Произошла ошибка: {e}")

@router.message(LTCRUB.price1)
async def swertyhbubh(message: types.Message, state: FSMContext):
    try:
        global price_number_2
        await state.update_data(nameban=message.text)
        ban_user = await state.get_data()
        price_number_2 = str(ban_user["nameban"])
        await add_values7(str(price_number_2))
        await state.clear()
        await message.answer(f'Курс изменен!')
    except Exception as e:
        print(f"Произошла ошибка: {e}")

@router.message(LTCIDR.price1)
async def swertyhbubh(message: types.Message, state: FSMContext):
    try:
        global price_number_2
        await state.update_data(nameban=message.text)
        ban_user = await state.get_data()
        price_number_2 = str(ban_user["nameban"])
        await add_values6(str(price_number_2))
        await state.clear()
        await message.answer(f'Курс изменен!')
    except Exception as e:
        print(f"Произошла ошибка: {e}")

@router.message(BTCLTC.price1)
async def swertyhbubh(message: types.Message, state: FSMContext):
    try:
        global price_number_2
        await state.update_data(nameban=message.text)
        ban_user = await state.get_data()
        price_number_2 = str(ban_user["nameban"])
        await add_values8(str(price_number_2))
        await state.clear()
        await message.answer(f'Курс изменен!')
    except Exception as e:
        print(f"Произошла ошибка: {e}")

@router.message(BTCUSD.price1)
async def swertyhbubh(message: types.Message, state: FSMContext):
    try:
        global price_number_2
        await state.update_data(nameban=message.text)
        ban_user = await state.get_data()
        price_number_2 = str(ban_user["nameban"])
        await add_values9(str(price_number_2))
        await state.clear()
        await message.answer(f'Курс изменен!')
    except Exception as e:
        print(f"Произошла ошибка: {e}")

@router.message(LTCUSD.price1)
async def swertyhbubh(message: types.Message, state: FSMContext):
    try:
        global price_number_2
        await state.update_data(nameban=message.text)
        ban_user = await state.get_data()
        price_number_2 = str(ban_user["nameban"])
        await add_values10(str(price_number_2))
        await state.clear()
        await message.answer(f'Курс изменен!')
    except Exception as e:
        print(f"Произошла ошибка: {e}")

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


@router.callback_query(lambda call: call.data and call.data.startswith("pri_"))
async def card(call: types.CallbackQuery, state: FSMContext):
    try:
        global text_id
        global ids
        text_id = str(call.data).replace("pri_", "")
        ids = call.from_user.id
        lang1 = await check_lang(str(text_id))
        lang2 = await check_lang(str(ids))
        average_rating = await get_average_rating(text_id, str(text_id))
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_message(chat_id=int(text_id),
                               text=f"<b>{_("Ваша заявка принята!\nВаш курьер: ", lang1[0])}  <code>@{call.from_user.username}</code>👤 \n {call.from_user.first_name}👤\n\n{_("Рейтинг курьера", lang1[0])}: {average_rating} ⭐️\n{_("Свяжитесь с ним для дальнейших действий", lang1[0])}📞</b>", parse_mode=ParseMode.HTML, reply_markup=kura(lang1, call.from_user.username).as_markup())
        await bot.send_message(chat_id=int(ids), text=f"<b>{_("Завершить заказ?", lang2[0])}</b>\n\n<b>{_("Завершать строго после выполнения!", lang2[0])}</b>",parse_mode=ParseMode.HTML,
                               reply_markup=finish_curiers(str(text_id), lang2).as_markup())
        await bot.send_message(chat_id=-1002244398985,
                               text=f"<b>Курьер - {call.from_user.username} принял заказ!!!</b>", parse_mode=ParseMode.HTML)
    except Exception as e:
        logging.exception(e)


@router.callback_query(lambda call: call.data and call.data.startswith("finish_"))
async def card(call, state: FSMContext):
    try:
        text = str(call.data).replace("finish_", "")
        lang = await check_lang(int(text))
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_message(chat_id=int(text), text=f"<b>{_("Курьер завершает заказ?\nПодтвердить выполнение?", lang[0])} ✔️</b>",parse_mode=ParseMode.HTML,
                               reply_markup=i_cur(lang, ids).as_markup())

    except Exception as e:
        logging.exception(e)


@router.callback_query(lambda call: call.data and call.data.startswith("conf_"))
async def card(call, state: FSMContext):
    try:
        current_time = datetime.datetime.now()
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        text = str(call.data).replace("finish_", "")
        idss = text.replace("conf_", "")
        laaaag = await get_pars2(curs, curs2, int(su))
        lang = await check_lang(int(text_id))
        lang808 = await check_lang(int(idss))
        await send_deals(call.from_user.username, call.from_user.id, curs, curs2, ifbez, str(su),
                         str(round(float(laaaag))),
                         geo, current_time)
        await bot.send_message(chat_id=int(idss), text=f"{_("Обмен прошёл успешно!", lang808[0])}🙂")
        await bot.send_message(chat_id=int(text_id), text=f"<b>{_("Обмен успешно завершен", lang[0])}🟢\n\n{_("Хотите ли оставить отзывы?", lang[0])}📣</b>",parse_mode=ParseMode.HTML, reply_markup=otviz(lang, idss).as_markup())

    except Exception as e:
        logging.exception(e)

@router.callback_query(lambda call: call.data and call.data.startswith("otzivi_"))
async def otziv(call, state: FSMContext):
    try:
        global curid
        curid = str(call.data).replace("otzivi_", "")
        lang = await check_lang(call.from_user.id)
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await call.message.answer(f"{_("Выберите качество работы курьера:", lang[0])}", reply_markup=otviz2(curid).as_markup())

    except Exception as e:
        logging.exception(e)


@router.callback_query(lambda call: call.data and call.data.startswith("ete_"))
async def otziv(call, state: FSMContext):
    try:
        curidd = str(call.data).replace("ete_", "")
        numer = str(curidd).replace(f"_{curid}", "")
        iddds = str(curidd).replace(f"{numer}_", "")
        lang = await check_lang(call.from_user.id)
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await send_reviews(str(iddds), str(numer))
        await call.message.answer(f"<b>{_("Спасибо за отзыв", lang[0])}☺️</b>", parse_mode=ParseMode.HTML)

    except Exception as e:
        logging.exception(e)
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


@router.callback_query(lambda call: call.data and call.data.startswith("accept_deals_"))
async def lang(call):
    try:
        await accept_in_deals(call)
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
@router.callback_query(lambda call: call.data and call.data.startswith("final_"))
async def final(call, state: FSMContext):
    try:
        print(call.message)
        await final_deals(call)
    except Exception as e:
        traceback.print_exc()
        logging.exception(e)
@router.callback_query(lambda call: call.data and call.data.startswith("canfinal_"))
async def final(call, state: FSMContext):
    try:
        row = await cancel_final_deals(call)
        await state.update_data(id_deal=row)
        await state.set_state(fsm.reason)
    except Exception as e:
        traceback.print_exc()
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
            await create_reset_task(call.from_user.id, state)
        except Exception as err:
            logging.exception(err)

    elif call.data == "deal":
        try:
            await get_messa(call)
        except Exception as err:
            logging.exception(err)
    elif call.data == "back_state":
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

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

    elif call.data == "edit_curs":
        try:
            await call.message.edit_text("Выберите направление", reply_markup=admin_curs().as_markup())
        except Exception as err:
            logging.exception(err)
    elif call.data == "RUBIDR123":
        try:
            await call.message.edit_text("Введите первое значение для 10.000 ₽ - 50.000 ₽", reply_markup=dell_state_admin().as_markup())
            await state.set_state(Direction1.price1)
        except Exception as err:
            logging.exception(err)

    elif call.data == "RUBUSD123":
        try:
            await call.message.edit_text("Введите значение для (RUB 🔄 USD(USDT)) or (USD(USDT) 🔄 RUB)", reply_markup=dell_state_admin().as_markup())
            await state.set_state(USDT.price1)
        except Exception as err:
            logging.exception(err)

    elif call.data == "IDRUSD123":
        try:
            await call.message.edit_text("Введите значение для 2,000,000 IDR - 10,000,000 IDR", reply_markup=dell_state_admin().as_markup())
            await state.set_state(Direction2.price1)

        except Exception as err:
            logging.exception(err)




    elif call.data == "BTCRUB123":
        try:
            await call.message.edit_text("Введите значение для курса BTC на RUB", reply_markup=dell_state_admin().as_markup())
            await state.set_state(BTCRUB.price1)

        except Exception as err:
            logging.exception(err)
    elif call.data == "BTCIDR123":
        try:
            await call.message.edit_text("Введите значение для курса BTC на IDR", reply_markup=dell_state_admin().as_markup())
            await state.set_state(BTCIDR.price1)

        except Exception as err:
            logging.exception(err)

    elif call.data == "LTCIDR123":
        try:
            await call.message.edit_text("Введите значение для курса LTC на IDR", reply_markup=dell_state_admin().as_markup())
            await state.set_state(LTCIDR.price1)

        except Exception as err:
            logging.exception(err)
    elif call.data == "LTCRUB123":
        try:
            await call.message.edit_text("Введите значение для курса LTC на RUB", reply_markup=dell_state_admin().as_markup())
            await state.set_state(LTCRUB.price1)

        except Exception as err:
            logging.exception(err)

    elif call.data == "LTCBTC123":
        try:
            await call.message.edit_text("Введите значение для курса BTC на LTC", reply_markup=dell_state_admin().as_markup())
            await state.set_state(BTCLTC.price1)

        except Exception as err:
            logging.exception(err)

    elif call.data == "BTCUSD123":
        try:
            await call.message.edit_text("Введите значение для курса BTC на USD(USDT)", reply_markup=dell_state_admin().as_markup())
            await state.set_state(BTCUSD.price1)

        except Exception as err:
            logging.exception(err)

    elif call.data == "LTCUSD123":
        try:
            await call.message.edit_text("Введите значение для курса LTC на USD(USDT)", reply_markup=dell_state_admin().as_markup())
            await state.set_state(LTCUSD.price1)

        except Exception as err:
            logging.exception(err)

    elif call.data == "act_cursik":
        try:
            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            lang = await check_lang(call.message.chat.id)
            await call.message.answer(f"<b>{_('Выберите интересующие направление для вас:', lang[0])}</b>",
                                         reply_markup=oflline(lang).as_markup())
            await state.set_state(ActCurs.choosing_currency)
        except Exception as err:
            logging.exception(err)

    elif call.data == "otmenabbb":
        try:
            await start_c(call)
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
    elif call.data == "lk":
        try:
            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            photo = FSInputFile("media/logo.png")
            lang = await check_lang(call.message.chat.id)
            await call.message.answer_photo(
                caption=f"<b>{_('Личный кабинет', lang[0])}\n{_("Завершенные сделки курьером - ", lang[0])}</b>",
                reply_markup=setting_rasilka(lang).as_markup(), photo=photo)
        except Exception as err:
            logging.warning(err)
    elif call.data == "exitnaxui":
        try:
            await start_c(call)
        except Exception as err:
            logging.exception(err)
    elif call.data == "back_naxuisuka":
        try:
            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            await state.clear()
            await call.message.answer("Отменено!")
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
        print(message.text)
        data = await state.get_data()
        amount_get = float(data["set_amount"])
        call_id = data["call_id"]
        lang = await check_lang(message.chat.id)
        row = await print_deals(call_id=call_id)
        min_am = data["min_am"]
        messag = ""
        if amount_get >= min_am:
            messag += (f"<b>{_('Очень хорошо', lang[0])}!</b>\n"
                       f"<i>{_('Введите реквизиты, на который вам отправить средства', lang[0])}:</i>\n\n")
            messag += f"<b>{check_address.data[row[3]]}</b>"
            await message.answer(messag, reply_markup=exc_btn_cancel(call_id, lang[0]).as_markup())
            await state.set_state(fsm.rekv_us)
        else:
            await message.answer(f"<b>Нахуй пошел! Русским языком сказали же минимум {min_am}</b>")
    except Exception as e:
        logging.exception(e)


@router.message(fsm.rekv_us)
async def setrt(message: types.Message, state: FSMContext):
    try:
        await state.update_data(rekv_us=message.text)
        data = await state.get_data()
        amount_get = float(data["set_amount"])
        lang = await check_lang(message.chat.id)
        call_id = data["call_id"]
        rekv_user_get = data["rekv_us"]
        row = await print_deals(call_id=call_id)
        check_ad = await check_address.check_address(row[3], rekv_user_get)
        if check_ad == 200:
            await add_amount_deals_onl(call_id, amount_get, rekv_user_get)
            await transaction_con(message, call_id)
            await state.clear()
        else:
            await message.answer("Введите реквизиты правильно!",
                                 reply_markup=exc_btn_cancel(call_id, lang[0]).as_markup())
    except Exception as e:
        logging.exception(e)


@router.message(fsm.rekv)
async def setrt(message: types.Message, state: FSMContext):
    try:
        await state.update_data(rekv=message.text)
        data = await state.get_data()
        rekv_get = data["rekv"]
        call_id = data["call_id_cards"]
        await add_rekv_cards(rekv_get, call_id)
        await message.answer(f"<b>Успешно!</b>\n"
                             f"<i>Добавим еще реквизит?</i>", reply_markup=admin_exc().as_markup())
        await state.clear()
        await state.set_state(fsm.set_amount)
    except Exception as e:
        logging.exception(e)

@router.message(fsm.reason)
async def setrt(message: types.Message, state: FSMContext):
    try:
        await state.update_data(reason=message.text)
        data = await state.get_data()
        reason_get = data["reason"]
        id_deal_get = data["id_deal"]
        print(id_deal_get)
        deal_info = await print_deals(id_deal_get)
        user = await check_us(deal_info[1])
        lang = await check_lang(user[1])
        await message.answer(f"<b>Сделка №{deal_info[0]} отменена🔴</b>\n\n"
                             f"<i>Причина: {reason_get}</i>")
        await bot.send_message(deal_info[1], f"<b>Сделка №{deal_info[0]} отменена🔴</b>\n\n"
                             f"<i>Причина: {reason_get}</i>", parse_mode="HTML",  reply_markup=help_oper(deal_info[10], lang[0]).as_markup())
        await state.clear()
    except Exception as e:
        logging.exception(e)