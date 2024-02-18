from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import garant
from translate import _
                ### ТО, ЧТО ВИДЕТ КЛИЕНТ ###
def start_but(lang):
    st = InlineKeyboardBuilder()
    st.button(text=f"{_('Обмен', lang)}", callback_data="exch")
    st.button(text=f"{_('Гарант сделок', lang)}", url=f"{garant[0][1]}")
    st.button(text=f"{_('Наш чат', lang)}", url="google.com")
    st.button(text=f"{_('Наш канал', lang)}", url="google.com")
    st.button(text=f"{_('Связь с админом', lang)}", url="google.com")
    st.adjust(1, 1, 2)
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
