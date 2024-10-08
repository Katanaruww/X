from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import garant
from translate import _
from routers import check_lang_smail
import aiogram
import asyncio


### ТО, ЧТО ВИДЕТ КЛИЕНТ ###
def start_but(lang):
    st = InlineKeyboardBuilder()
    st.button(text=f"{_('Обмен', lang)}", callback_data="exch")
    st.button(text=f"{_('Гарант сделок', lang)}", url=f"{garant[0][1]}")
    st.button(text=f"{_('Наш чат', lang)}", url="google.com")
    st.button(text=f"{_('Наш канал', lang)}", url="google.com")
    st.button(text=f"{_('Связь с админом', lang)}", url="google.com")
    st.button(text=f"{_('Личный кабинет', lang)}", callback_data="lk")
    st.button(text=f"{_("Актуальный курс", lang)}", callback_data="act_cursik")
    st.button(text=f"{_('Настройки', lang)}⚙", callback_data="setting")
    st.adjust(1, 1, 2, 1)
    return st

def get_geo(lang):
    st = InlineKeyboardBuilder()
    st.button(text=f"{_('Чангу', lang[0])}🏖", callback_data="Changu")
    st.button(text=f"{_('Семеньяк', lang[0])}🏖", callback_data="Semen")
    st.button(text=f"{_('Убуд', lang[0])}🏖", callback_data="Ubud")
    st.button(text=f"{_('Отправить геопозицию', lang[0])}📍", callback_data="Geo")
    st.button(text=f"{_('Отмена', lang[0])}🔴", callback_data="dell_gps")

    st.adjust(1, 1, 1, 1)
    return st
def rules(lang):
    rul = InlineKeyboardBuilder()
    rul.button(text=f"{_('Согласен', lang)}🟢", callback_data="agree_rules")
    rul.adjust(1)
    return rul

def get_curiers(id):
    rul = InlineKeyboardBuilder()
    rul.button(text=f"Принять", callback_data=f"pri_{id}")
    rul.adjust(1)
    return rul

def finish_curiers(id, lang):
    rul = InlineKeyboardBuilder()
    rul.button(text=f"{_("Завершить заказ", lang=lang[0])}", callback_data=f"finish_{id}")
    rul.adjust(1)
    return rul
def inline_geo(lang):
    rul = InlineKeyboardBuilder()
    rul.button(text=f"{_('Да', lang[0])}🟢", callback_data="yesgeo")
    rul.button(text=f"{_('Нет', lang[0])}🔴", callback_data="nogeo")
    rul.adjust(2)
    return rul
def kura(lang, idddd):
    rul = InlineKeyboardBuilder()
    rul.button(text=f"{_('Связь с курьером', lang[0])}👤", url=f"https://t.me/{idddd}")
    rul.adjust(2)
    return rul
def otviz(lang, idddd):
    rul = InlineKeyboardBuilder()
    rul.button(text=f"{_('Оставить отзыв', lang[0])}📢", callback_data=f"otzivi_{idddd}")
    rul.button(text=f"{_('Отмена', lang[0])}🔴", callback_data=f"exitnaxui")
    rul.adjust(2)
    return rul

def otviz2(idddd):
    rul = InlineKeyboardBuilder()
    rul.button(text=f"1⭐️", callback_data=f"ete_1_{idddd}")
    rul.button(text=f"2⭐️", callback_data=f"ete_2_{idddd}")
    rul.button(text=f"3⭐️", callback_data=f"ete_3_{idddd}")
    rul.button(text=f"4⭐️", callback_data=f"ete_4_{idddd}")
    rul.button(text=f"5⭐️", callback_data=f"ete_5_{idddd}")
    rul.adjust(5)
    return rul
def i_cur(lang, ids):
    rul = InlineKeyboardBuilder()
    rul.button(text=f"{_('Подтвердить', lang[0])}🟢", callback_data=f"conf_{ids}")
    rul.button(text=f"{_('Отказ', lang[0])}🔴", callback_data=f"noconf_{ids}")
    rul.adjust(2)
    return rul

def beznal(lang):
    rul = InlineKeyboardBuilder()
    rul.button(text=f"{_('Наличный расчёт', lang[0])}💵", callback_data=f"nal")
    rul.button(text=f"{_('Безналичный расчёт', lang[0])}💳", callback_data=f"beznal")
    rul.button(text=f"{_('Отмена', lang[0])}🔴", callback_data="dell_geo")
    rul.adjust(2)
    return rul
def in_gps(lang):
    rul = InlineKeyboardBuilder()
    rul.button(text=f"{_('Да', lang[0])}🟢", callback_data="yesgps")
    rul.button(text=f"{_('Нет', lang[0])}🔴", callback_data="nogps")
    rul.adjust(2)
    return rul

def dell_gps000(lang):
    rul = InlineKeyboardBuilder()
    rul.button(text=f"{_('Отмена', lang[0])}🔴", callback_data="dell_geo")
    return rul
def lang_btn():
    lang = InlineKeyboardBuilder()
    lang.button(text="Русский", callback_data="lang_RU")
    lang.button(text="English", callback_data="lang_EN")
    lang.adjust(2)
    return lang


def setting_btn(call, lang):
    sett = InlineKeyboardBuilder()
    sett.button(text=f"{_('Смена языка', lang)} | {check_lang_smail(call.message.chat.id)[1]}",
                callback_data=f"change_{check_lang_smail(call.message.chat.id)[0]}")
    sett.button(text=f"{_('Назад', lang)}🔙", callback_data="back_start")
    sett.adjust(1)
    return sett


def exc_btn_start(lang):
    exc = InlineKeyboardBuilder()
    exc.button(text=f"{_('Сделка онлайн', lang)}", callback_data="type_give")
    exc.button(text=f"{_('Доставка налички', lang)}", callback_data="offline_deals")  ### для данила
    exc.button(text=f"{_('Назад', lang)}🔙", callback_data="back_start")
    exc.adjust(2, 1)
    return exc


### ОНЛАЙН СДЕЛКИ ###

def exc_type_onl_btn(call_id, lang, type):
    exc_o = InlineKeyboardBuilder()
    exc_o.button(text="RUB", callback_data=f"{type}_RUB_{call_id}")
    exc_o.button(text="USD", callback_data=f"{type}_USD_{call_id}")
    exc_o.button(text="IDR", callback_data=f"{type}_IDR_{call_id}")
    exc_o.button(text="USDT", callback_data=f"{type}_USDT_{call_id}")
    exc_o.button(text="BTC", callback_data=f"{type}_BTC_{call_id}")
    exc_o.button(text="LTC", callback_data=f"{type}_LTC_{call_id}")
    exc_o.button(text=f"{_('Отмена', lang)}⭕", callback_data=f"cancel-deal_{call_id}")
    exc_o.adjust(3, 3, 1)
    return exc_o


def exc_btn_cancel(call_id, lang):
    exc = InlineKeyboardBuilder()
    exc.button(text=f"{_('Отмена', lang)}⭕", callback_data=f"cancel-deal_{call_id}")
    exc.adjust(2, 1)
    return exc

def olesia222(lang):
    exc = InlineKeyboardBuilder()
    exc.button(text=f"{_('Назад', lang[0])}⭕", callback_data=f"otmenabbb")
    exc.adjust(1)
    return exc

def continue_add_deal(call_id, lang):
    con_ad_d = InlineKeyboardBuilder()
    con_ad_d.button(text=f"{_('Продолжить', lang)}🟢", callback_data=f"continue-deals_{call_id}")
    con_ad_d.button(text=f"{_('Отмена', lang)}⭕", callback_data=f"cancel-deal_{call_id}")
    con_ad_d.adjust(1, 1)
    return con_ad_d


def accept_deals(call_id, lang):
    acc_d = InlineKeyboardBuilder()
    acc_d.button(text=f"{_('Я оплатил(а)', lang)}🟢", callback_data=f"accept_deals_{call_id}")
    acc_d.button(text=f"{_('Отмена', lang)}⭕", callback_data=f"cancel-deal_{call_id}")
    acc_d.adjust(1, 1)
    return acc_d

def help_oper(link_oper, lang, st=0):
    heo = InlineKeyboardBuilder()
    if st == 0:
        heo.button(text=f"{_('Написать оператору', lang)}", url=f"https://t.me/{link_oper}")
    elif st == 1:
        heo.button(text=f"{_('Написать оператору', lang)}", url=f"https://t.me/{link_oper}")
        #heo.button(text=f"{_('Оставить отзыв', lang)}", callback_data=f"rec-feedback_{}")
    heo.adjust(1)
    return heo

def final_button(id_deals, link_us):
    fib = InlineKeyboardBuilder()
    fib.button(text="Оплачено😊", callback_data=f"final_{id_deals}")
    fib.button(text="Написать пользователю", url=f"https://t.me/{link_us}")
    fib.button(text="Отменить сделку📛", callback_data=f"canfinal_{id_deals}")
    fib.adjust(1, 1, 1)
    return fib
### ОНЛАЙН СДЕЛКА ###
"""MYZONE"""


def setting_rasilka(lang):
    sett = InlineKeyboardBuilder()
    sett.button(text=f"{_('Главное меню', lang[0])}🔙", callback_data="back_start")
    sett.adjust(1)
    return sett


def crypto_valets(lang):
    sett = InlineKeyboardBuilder()
    sett.button(text=f"RUB|IDR", callback_data="RUB|IDR")
    sett.button(text=f"IDR|RUB", callback_data="RUB|IDR")

    sett.button(text=f"USDT|IDR", callback_data="USDT|IDR")
    sett.button(text=f"IDR|USDT", callback_data="USD|USDT")

    sett.button(text=f"USD|IDR", callback_data="USD|IDR")
    sett.button(text=f"IDR|USDT", callback_data="USD|USDT")

    sett.button(text=f"USD|USDT", callback_data="USD|USDT")
    sett.button(text=f"USDT|USD", callback_data="USDT|USD")
    # sdfghyjk

    sett.button(text=f"{_('Как происходит сделка?', lang[0])}💸", callback_data="deal")
    sett.button(text=f"{_('Главное меню', lang[0])}🔙", callback_data="back_start")

    sett.adjust(2, 2, 2, 2, 1, 1)
    return sett

def dell_state(lang):
    adm_exc_add = InlineKeyboardBuilder()
    adm_exc_add.button(text=f"{_(text='Отмена', lang=lang[0])}⭕️", callback_data=f"back_state")
    return adm_exc_add

def dell_state_admin():
    adm_exc_add = InlineKeyboardBuilder()
    adm_exc_add.button(text="Выйти⭕️", callback_data=f"back_naxuisuka")
    return adm_exc_add
def add_cur_offline(lang):
    adm_exc_add = InlineKeyboardBuilder()
    adm_exc_add.button(text=f"{_(text='Начать обмен', lang=lang[0])}", callback_data=f"start_offline")
    adm_exc_add.button(text=f"{_('Как происходит сделка?', lang[0])}💸", callback_data="deal")
    adm_exc_add.button(text=f"{_('Отмена', lang[0])}⭕️", callback_data="back_start")
    adm_exc_add.adjust(1,1,1)
    return adm_exc_add


def get_offline(lang):
    adm_exc_add = InlineKeyboardBuilder()
    adm_exc_add.button(text=f"{_(text='Продолжить', lang=lang[0])}🟢", callback_data=f"get")
    adm_exc_add.button(text=f"{_('Отмена', lang[0])}🚫", callback_data="delleate")


    adm_exc_add.adjust(1,1,1)
    return adm_exc_add





def oflline(lang):
    adm_exc_add = InlineKeyboardBuilder()
    adm_exc_add.button(text="RUB", callback_data=f"RUB1")
    adm_exc_add.button(text="IDR", callback_data=f"IDR1")
    adm_exc_add.button(text="USD", callback_data=f"USD1")
    adm_exc_add.button(text="USDT", callback_data=f"USDT1")
    adm_exc_add.button(text="BTC", callback_data=f"BTC1")
    adm_exc_add.button(text="LTC", callback_data=f"LTC1")
    adm_exc_add.button(text=f"{_(text='Отмена', lang=lang[0])}⭕️", callback_data=f"back_state")
    adm_exc_add.adjust(3, 3)
    return adm_exc_add

def oflline2(lang):
    adm_exc_add = InlineKeyboardBuilder()
    adm_exc_add.button(text="RUB", callback_data=f"RUB1")
    adm_exc_add.button(text="IDR", callback_data=f"IDR1")
    adm_exc_add.button(text="USD", callback_data=f"USD1")
    adm_exc_add.button(text="USDT", callback_data=f"USDT1")
    adm_exc_add.button(text="BTC", callback_data=f"BTC1")
    adm_exc_add.button(text="LTC", callback_data=f"LTC1")
    adm_exc_add.adjust(3, 3)
    return adm_exc_add
"""MYZONE"""


### АДМИН ПАНЕЛЬ ###
def admin_but_send():
    adm = InlineKeyboardBuilder()
    adm.button(text="Рассылка с фотографией", callback_data="send1")
    adm.button(text="Рассылка без фотографии", callback_data="send2")
    adm.adjust(1)
    return adm


def sub():
    sub = InlineKeyboardBuilder()
    sub.button(text="Подпишись!", url="https://t.me/lucky_bali_group")
    return sub

def admin_but():
    adm = InlineKeyboardBuilder()
    adm.button(text="Админка обменника", callback_data="adm_exc")
    adm.button(text="Рассылка", callback_data="send")
    adm.button(text="Чёрный список", callback_data="black_list")
    adm.button(text="Изменить курс", callback_data="edit_curs")
    adm.adjust(1)
    return adm

def admin_curs():
    adm = InlineKeyboardBuilder()
    adm.button(text="(RUB 🔄 IDR) or (IDR 🔄 RUB)", callback_data="RUBIDR123")

    adm.button(text="(RUB 🔄 USD(USDT)) or (USD(USDT) 🔄 RUB)", callback_data="RUBUSD123")

    adm.button(text="(IDR 🔄 USD(USDT)) or (USD(USDT) 🔄 IDR)", callback_data="IDRUSD123")

    adm.button(text="(BTC 🔄 RUB) or (RUB 🔄 BTC)", callback_data="BTCRUB123")

    adm.button(text="(BTC 🔄 IDR) or (IDR 🔄 BTC)", callback_data="BTCIDR123")

    adm.button(text="(LTC 🔄 IDR) or (IDR 🔄 LTC)", callback_data="LTCIDR123")

    adm.button(text="(LTC 🔄 RUB) or (RUB 🔄 LTC)", callback_data="LTCRUB123")

    adm.button(text="(BTC 🔄 LTC) or (LTC 🔄 BTC)", callback_data="LTCBTC123")

    adm.button(text="(BTC 🔄 USDT(USD)) or (USDT(USD)) 🔄 BTC)", callback_data="BTCUSD123")

    adm.button(text="(LTC 🔄 USDT(USD)) or (USD(USDT)) 🔄 LTC)", callback_data="LTCUSD123")


    adm.adjust(1)
    return adm

def admin_but_blaack_list():
    adm = InlineKeyboardBuilder()
    adm.button(text="Бан по username", callback_data="adm_usr")
    adm.button(text="Бан по id", callback_data="adm_id")
    return adm


def admin_bc_fsm():
    adm = InlineKeyboardBuilder()
    adm.button(text="Да✅", callback_data="yes")
    adm.button(text="Нет❌", callback_data="no")
    adm.adjust(1)
    return adm


def ban():
    adm = InlineKeyboardBuilder()
    adm.button(text="Да✅", callback_data="yes3")
    adm.button(text="Нет❌", callback_data="no3")
    adm.adjust(1)
    return adm


def admin_bc_fsm2():
    adm = InlineKeyboardBuilder()
    adm.button(text="Да✅", callback_data="yes2")
    adm.button(text="Нет❌", callback_data="no2")
    adm.adjust(1)
    return adm


def admin_exc():
    adm_exc = InlineKeyboardBuilder()
    adm_exc.button(text="Просмотр карт", callback_data="see_cards")
    adm_exc.button(text="Ввод карты", callback_data="add_cards")
    adm_exc.button(text="Назад🔙", callback_data="back_admin")
    adm_exc.adjust(1, 1, 1)
    return adm_exc


def admin_exc_add_card(call_id, typ):
    adm_exc_add = InlineKeyboardBuilder()
    adm_exc_add.button(text="RUB", callback_data=f"{typ}-cards_RUB_{call_id}")
    adm_exc_add.button(text="IDR", callback_data=f"{typ}-cards_IDR_{call_id}")
    adm_exc_add.button(text="USD", callback_data=f"{typ}-cards_USD_{call_id}")
    adm_exc_add.button(text="USDT", callback_data=f"{typ}-cards_USDT_{call_id}")
    adm_exc_add.button(text="BTC", callback_data=f"{typ}-cards_BTC_{call_id}")
    adm_exc_add.button(text="LTC", callback_data=f"{typ}-cards_LTC_{call_id}")
    adm_exc_add.button(text="Назад🔙", callback_data="back_admin")
    adm_exc_add.adjust(3, 3, 1)
    return adm_exc_add


def admin_exc_rub_add_card(type_d, t="card", call_id="None", other=0, lang="RU"):
    adm_e_r_add = InlineKeyboardBuilder()
    adm_e_r_add.button(text=f"{_('Сбербанк', lang)}", callback_data=f"{type_d}-RUB-cards_Сбербанк_{call_id}_{other}")
    adm_e_r_add.button(text=f"{_('Т-Банк', lang)}", callback_data=f"{type_d}-RUB-cards_Тинькофф_{call_id}_{other}")
    adm_e_r_add.button(text=f"{_('Карта', lang)}", callback_data=f"{type_d}-RUB-cards_Карта_{call_id}_{other}")
    adm_e_r_add.button(text=f"{_('СБП', lang)}", callback_data=f"{type_d}-RUB-cards_СБП_{call_id}_{other}")
    adm_e_r_add.button(text=f"{_('Отмена', lang)}⭕️", callback_data=f"cancel-{t}_{call_id}_{other}")
    adm_e_r_add.adjust(1, 1, 1, 1, 1)
    return adm_e_r_add


def adm_exc_cancel_card(call_id):
    adm_e_c = InlineKeyboardBuilder()
    adm_e_c.button(text="Отмена⭕️", callback_data=f"cancel-card_{call_id}")
    adm_e_c.adjust(1)
    return adm_e_c


def delete_card_button(call_id):
    del_c_b = InlineKeyboardBuilder()
    del_c_b.button(text="Удалить🗑", callback_data=f"cancel-card_{call_id}")
    del_c_b.button(text="Назад🔙", callback_data=f"back_admin")
    del_c_b.adjust(1, 1)
    return del_c_b

