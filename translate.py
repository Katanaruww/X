translates = {
    "EN": {
        "Добро пожаловать": "Welcome",
        "Обмен" : "Exchange",
        "Гарант сделок" : "Guarantor",
        "Наш чат" : "Chat",
        "Наш канал" : "Channel",
        "Связь с админом" : "Admin",
        "Согласен" : "I agree",
    }
}


def _(text, lang="RU"):
    if lang == "RU":
        return text
    else:
        global translates
        return translates[lang][text]
