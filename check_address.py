import asyncio

data = {
    "RUB": "Введите номер телефона через +7 и название банка или номер карты",
    "BTC": "Введите только адрес BTC нового (bc1) или старого формата (начало с 1 или 3)",
    "LTC": "Введите только адрес LTC",
    "USDT": "Введите только адрес в сети TRC-20",
    "USD": "Введите номер карты и банк",
    "IDR": "Введите номер карты и банк"
}


async def check_address(t_p, text):
    if t_p == "RUB":
        if len(text) == 16 or (len(text) >= 12 and text[:2] == "+7"):
            return 200
        else:
            return 500
    elif t_p == "BTC":
        if (27 <= len(text) <= 50) and (text[0] == "1" or text[0] == "3" or text[:3] == "bc1"):
            return 200
        else:
            return 500
    elif t_p == "LTC":
        if (len(text) <= 50) and (text[0] == "M" or text[0] == "3" or text[:3] == "ltc"):
            return 200
        else:
            return 500
    elif t_p == "USDT":
        if (len(text) <= 37) and (text[0] == "T"):
            return 200
        else:
            return 500
    elif t_p == "USD":
        pass
    elif t_p == "IDR":
        if len(text) >= 16:
            return 200
        else:
            return 500
