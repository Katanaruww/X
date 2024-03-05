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
        "Что хотите получить" : "What you want to get",
        "Назад" : "Back",
        "Отмена" : "Cancel",
        "Главное меню" : "Main menu",
        "Как происходит сделка?": "How does the deal work?",
        "Выберите интересующие направление для вас:": "Select the direction you are interested in:",
        "Доставка курьером производится по этапу:": "Delivery by courier is carried out according to the following stages:",
        "Создаём заявку в боте.": "We create a request in the bot.",
        "С вами связывается курьер.": "The courier will contact you.",
        "Встречаетесь с курьером.": "Meet with the courier.",
        "Проверяем и получаем средства.": "We check and receive funds.",
        "Отлично! Теперь введите сумму в" : "Oh, great! Now enter the amount in",
        "которую хотите обменять на": "that you want to trade for",
        "Минимальная сумма": "Minimum amount"
    }
}


def _(text, lang="RU"):
    if lang == "RU":
        return text
    else:
        global translates
        return translates[lang][text]
