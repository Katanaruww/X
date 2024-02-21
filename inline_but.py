from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import garant
from translate import _
from routers import check_lang_smail
import aiogram
                ### ТО, ЧТО ВИДЕТ КЛИЕНТ ###
def start_but(lang):
    st = InlineKeyboardBuilder()
    st.button(text=f"{_('Обмен', lang)}", callback_data="exch")
    st.button(text=f"{_('Гарант сделок', lang)}", url=f"{garant[0][1]}")
    st.button(text=f"{_('Наш чат', lang)}", url="google.com")
    st.button(text=f"{_('Наш канал', lang)}", url="google.com")
    st.button(text=f"{_('Связь с админом', lang)}", url="google.com")
    st.button(text=f"{_('Настройки', lang)}⚙", callback_data="setting")
    st.adjust(1, 1, 2, 1)
    return st


def rules(lang):
    rul = InlineKeyboardBuilder()
    rul.button(text=f"{_('Согласен', lang)}🟢", callback_data="agree_rules")
    rul.adjust(1)
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
    exc.button(text=f"{_('Сделка онлайн', lang)}", callback_data="online_deals")
    exc.button(text=f"{_('Доставка налички', lang)}", callback_data="offline_deals") ### для данила
    exc.button(text=f"{_('Назад', lang)}🔙", callback_data="back_start")
    exc.adjust(2, 1)
    return exc

def exc_type_onl_btn(call, lang):
    exc_t = InlineKeyboardBuilder()
    exc_t.button(text=f"{_('Покупка валюты', lang)}📈", callback_data=f"type_{call.message.chat.id}_pay")
    exc_t.button(text=f"{_('Продажа валюты', lang)}📉", callback_data=f"type_{call.message.chat.id}_sale")
    exc_t.button(text=f"{_('Назад', lang)}🔙", callback_data="back_start")
    exc_t.adjust(1, 1, 1)
    return exc_t

def exc_online_cancel(call, lang):
    exc_o = InlineKeyboardBuilder()
    exc_o.button(text=f"{_('Отмена', lang)}", callback_data=f"cancel-deal_{call.message.chat.id}")
    exc_o.adjust(1)
    return exc_o

"""MYZONE"""


def setting_rasilka(lang):
    sett = InlineKeyboardBuilder()
    sett.button(text=f"{_('Главное меню', lang[0])}🔙", callback_data="back_start")
    sett.adjust(1)
    return sett

def crypto_valets(lang):
    sett = InlineKeyboardBuilder()
    sett.button(text=f"RUB/IDR", callback_data="RUB/IDR")
    sett.button(text=f"IDR/RUB", callback_data="RUB/IDR")

    sett.button(text=f"USDT/IDR", callback_data="USDT/IDR")
    sett.button(text=f"IDR/USDT", callback_data="USD/USDT")

    sett.button(text=f"USD/IDR", callback_data="USD/IDR")
    sett.button(text=f"IDR/USDT", callback_data="USD/USDT")


    sett.button(text=f"USD/USDT", callback_data="USD/USDT")
    sett.button(text=f"USDT/USD", callback_data="USDT/USD")
    sett.button(text=f"{_('Главное меню', lang[0])}🔙", callback_data="back_start")
    sett.adjust(2)
    return sett


"""MYZONE"""

                ### АДМИН ПАНЕЛЬ ###
def admin_but_send():
    adm = InlineKeyboardBuilder()
    adm.button(text="Рассылка с фотографией", callback_data="send1")
    adm.button(text="Рассылка без фотографии", callback_data="send2")
    adm.adjust(1)
    return adm


def admin_but():
    adm = InlineKeyboardBuilder()
    adm.button(text="Админка обменника", callback_data="adm_exc")
    adm.button(text="Рассылка", callback_data="send")
    adm.adjust(1)
    return adm

def admin_bc_fsm():
    adm = InlineKeyboardBuilder()
    adm.button(text="Да✅", callback_data="yes")
    adm.button(text="Нет❌", callback_data="no")
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

