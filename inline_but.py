from aiogram.utils.keyboard import InlineKeyboardBuilder

def admin_but():
    adm = InlineKeyboardBuilder()
    adm.button(text="Рассылка", callback_data="send")
    adm.adjust(1)
    return adm
def rules():
    rul = InlineKeyboardBuilder()
    rul.button(text="Согласен🟢", callback_data="agree_rules")
    rul.adjust(1)
    return rul


def start_but():
    st = InlineKeyboardBuilder()
    st.button(text="Сделка с Гарантом", callback_data="deals_garant")
    st.button(text="Обмен", callback_data="exch")
    st.button(text="Наш чат", url="google.com")
    st.button(text="Наш канал", url="google.com")
    st.button(text="Связь с админом", url="google.com")
    st.adjust(2, 2)
    return st
