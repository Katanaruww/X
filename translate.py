translates = {
    "EN": {
        "Добро пожаловать": "Welcome",
        "Обмен" : "Exchange",
        "Гарант сделок" : "Guarantor",
        "Наш чат" : "Chat",
        "Наш канал" : "Channel",
        "Связь с админом" : "Admin",
        "Согласен" : "I agree",
        "Настройки" : "Setting",
        "Смена языка" : "Change of language",
        "Сделка онлайн": "Deal online",
        "Доставка налички" : "Cash delivery",
        "Покупка валюты" : "Purchase of currency",
        "Продажа валюты" : "Sale of currency",
        "Выберите действие" : "Select an action",
        "Что отдаете" : "What are you giving away",
        "Назад" : "Back",
        "Отмена" : "Cancel",
        "Главное меню" : "Main menu",
        "Как происходит сделка?": "How does the deal work?"
    }
}


def _(text, lang="RU"):
    if lang == "RU":
        return text
    else:
        global translates
        return translates[lang][text]
