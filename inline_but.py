from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import garant
def admin_but():
    adm = InlineKeyboardBuilder()
    adm.button(text="Админка обменника", callback_data="adm_exc")
    adm.button(text="Рассылка", callback_data="send")
    adm.adjust(1)
    return adm

def admin_exc():
    adm_exc = InlineKeyboardBuilder()
    adm_exc.button(text="Просмотр карт", callback_data="see_cards")
    adm_exc.button(text="Ввод карты", callback_data="add_cards")
    adm_exc.button(text="Назад🔙", callback_data="back_admin")
    adm_exc.adjust(1, 1, 1)
    return adm_exc
def rules():
    rul = InlineKeyboardBuilder()
    rul.button(text="Согласен🟢", callback_data="agree_rules")
    rul.adjust(1)
    return rul


def start_but():
    st = InlineKeyboardBuilder()
    st.button(text="Обмен", callback_data="exch")
    st.button(text="Сделка с Гарантом", url=f"{garant[0][1]}")
    st.button(text="Наш чат", url="google.com")
    st.button(text="Наш канал", url="google.com")
    st.button(text="Связь с админом", url="google.com")
    st.adjust(1, 1, 2)
    return st
def admin_but_send():
    adm = InlineKeyboardBuilder()
    adm.button(text="Рассылка с фотографией", callback_data="send1")
    adm.button(text="Рассылка без фотографии", callback_data="send2")
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
