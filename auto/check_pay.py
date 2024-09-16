from routers import conn
import re
import asyncio


async def check_sberbank(test):
    sum = []
    for i in range(len(test)):
        if test[i][1] == "push":
            if test[i][2] == "СберБанк":
                if "Баланс" in test[i][4] and "Зачисление" in test[i][3] or "Перевод от" in test[i][3] or "Зачислен" in \
                        test[i][3]:
                    match = re.search(r"(?:\+?\s?|\b)(\d[\d\.\s,]*)(?:\s?(?:р|₽))", test[i][4])
                    if match:
                        amount_str = match.group(0).replace("+", "").replace(" ", "").replace("р", "").replace("₽", "")
                        amount = int(amount_str.replace('\xa0', ''))

                        lists = [int(amount), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Ошибка: сумма платежа не найдена пуш сбер", test[i][4])
            else:
                pass
        elif test[i][1] == "sms":
            if test[i][2] == "900":
                if 'Перевод' in test[i][4] or 'зачисление' in test[i][4] and "Баланс" in test[i][4]:
                    match = re.search(r'(\d{1,3}(?:\s\d{3})*|\d+)(?=р)', test[i][4])
                    if match:
                        amount_str = match.group().replace(" ", "").replace(",", ".")
                        amount = int(amount_str.replace('\xa0', ''))
                        lists = [amount, test[i][0]]
                        sum.append(lists)
                    else:
                        print("Ошибка: сумма платежа не найдена смс сбер", test[i][4])
            else:
                pass
        else:
            pass
    return sum


async def check_tinkoff(test):
    sum = []
    for i in range(len(test)):
        if test[i][1] == 'push':
            if test[i][2] == "Т-Банк":
                if "Пополнение" in test[i][4]:
                    match = re.search(r"\b(\d[\d\s]*)\s*₽?\s*,\s*счет\b", test[i][4])
                    if match:
                        amount_str = match.group(1).replace('\xa0', '')  # Удаление неразрывного пробела
                        amount = int(amount_str)
                        lists = [int(amount), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Ошибка: сумма платежа не найдена пуш тинька", test[i][4])
            else:
                pass
        elif test[i][1] == 'sms':
            if test[i][2] == "Tinkoff":
                if 'Пополнение' in test[i][4]:
                    match = re.search(r"(\d{1,4}(?:,\d{3})*(?:\.\d{2})?) RUB", test[i][4])
                    if match:
                        amount_str = match.group(1).replace('\xa0', '')  # Удаление неразрывного пробела
                        amount = int(amount_str)
                        lists = [int(amount), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Ошибка: сумма платежа не найдена смс тинька", test[i][4])
            else:
                pass
    return sum


async def check_alphabank(test):
    sum = []
    for i in range(len(test)):
        if test[i][1] == "push":
            if test[i][2] == "Альфа-Банк":
                if "Поступление" in test[i][3]:
                    match = re.search(r"\+?(\d[\d\s,]*)\s*₽?\.\s*Поступление", test[i][3])
                    if match:
                        amount = match.group(1).replace(' ', '').replace(',', '.').replace("\xa0", "")
                        lists = [int(amount), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Ошибка: сумма платежа не найдена", test[i][2])
            else:
                pass
        if test[i][1] == "sms":
            if test[i][2] == "Alfa-Bank":
                if "Пополнение" in test[i][4]:
                    match = re.search(r'на\s((\d+\s*)+)\sRUR', test[i][4])
                    if match:
                        amount = match.group(1).replace(' ', '').replace(',', '.').replace("\xa0", "")
                        lists = [int(amount), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Ошибка: сумма платежа не найдена", test[i][2])
            else:
                pass
    return sum


async def check_qiwi(test):
    sum = []
    for i in range(len(test)):
        if test[i][2] == "QIWI":
            if "Пополнение" in test[i][3]:
                match = re.search(r"\d{3,}(?:[.,]\d{2})\b", test[i][4].replace('\xa0', ' '))
                if match:
                    amount_str = match.group(0).replace(",", ".")
                    amount = amount_str
                    lists = [int(float(amount)), test[i][0]]
                    sum.append(lists)
                else:
                    print("Ошибка: сумма платежа не найдена киви", test[i][4])
            else:
                pass
        else:
            pass
    return sum


async def check_vtb(test):
    sum = []
    for i in range(len(test)):
        if test[i][1] == "push":
            if test[i][2] == "ВТБ":
                if "Поступление" in test[i][4] or "Зачисление" in test[i][4]:
                    match = re.search(r"\d{1,3}(?:\s\d{3})*[\.,]?\d*\s*[pр]\s*", test[i][4].replace('\xa0', ' '))
                    if match:
                        amount_str = match.group(0).replace("p", "").replace("р", "").strip()
                        amount = amount_str.replace(",", ".").replace("\u202f", "").replace(" ", "")
                        lists = [int(float(amount)), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Ошибка: сумма платежа не найдена пуш втб", test[i][4])
                else:
                    pass
            else:
                pass
        elif test[i][1] == "sms":
            if test[i][2] == "VTB":
                if "Зачисление" in test[i][4]:
                    match = re.search(r"\d{1,}[.,]\d{2}р", test[i][4].replace('\xa0', ' '))
                    if match:
                        amount_str = match.group().replace(" ", "").replace(",", ".").replace("р", "")
                        amount = float(amount_str)
                        lists = [int(float(amount)), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Ошибка: сумма платежа не найдена смс втб")
                else:
                    pass
            else:
                pass
    return sum


async def check_rshb(test):
    sum = []
    for i in range(len(test)):
        if test[i][1] == "push":
            if test[i][2] == "RSHB":
                if "перевод" in test[i][4] or "Успешный перевод" in test[i][4]:
                    match = re.search(r"\b(\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})?)\s*[рR][uU]?[rR]?\b", test[i][4])
                    if match:
                        amount_str = match.group(1).replace('р', '').replace(',', '')
                        lists = [int(float(amount_str)), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Ошибка: сумма платежа не найдена пуш рсхб")
                else:
                    pass
            else:
                pass
        elif test[i][1] == "sms":
            if test[i][2] == "RSHB":
                if "перевод" in test[i][4]:
                    match = re.search(r'(?:перевод|Зачислено)\s+(\d+(?:,\d{3})*(?:\.\d{2})?)\s*(руб|р|₽)?',
                                      test[i][4].replace('\xa0', ' '))
                    if match:
                        amount_str = match.group(1).replace('р', '').replace(',', '')
                        lists = [int(float(amount_str)), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Ошибка: сумма платежа не найдена смс втб")
                else:
                    pass
            else:
                pass
    return sum


async def check_ural(test):
    sum = []
    for i in range(len(test)):
        if test[i][1] == "sms":
            if test[i][2] == "URALSIB":
                if "Postuplenie" or "POSTUPLENIE SREDSTV NA SCHET" in test[i][4]:
                    match = re.search(r'(\d+\.\d{2})\s+(RUB|RUR)', test[i][4].replace('\xa0', ' '))
                    if match:
                        amount_str = match.group(1).replace(",", ".")
                        amount = amount_str
                        lists = [int(float(amount)), test[i][0]]
                        sum.append(lists)

                    else:
                        print("Ошибка: сумма платежа не найдена уралсиб", test[i][4])
                else:
                    pass
        elif test[i][1] == "push":
            if test[i][2] == "Уралсиб":
                if "Postuplenie" in test[i][4] or "Perevod" in test[i][4]:
                    match = re.search(r"(\d+\.\d+)\s(?:RUB|RUR)", test[i][4].replace('\xa0', ' '))
                    if match:
                        print(match)
                        amount_str = match.group(1).replace(",", ".")
                        amount = amount_str
                        lists = [int(float(amount)), test[i][0]]
                        sum.append(lists)

                    else:
                        print("Ошибка: сумма платежа не найдена уралсиб", test[i][4])
                else:
                    pass
        else:
            pass
    return sum


async def check_pochta(test):
    sum = []
    for i in range(len(test)):
        if test[i][1] == "sms":
            if test[i][2] == "POCHTABANK":
                if "Popolnenie" in test[i][4]:
                    match = re.search(r'Popolnenie\s+(\d+\.\d{2})\s+RUB', test[i][4].replace('\xa0', ' '))
                    if match:
                        amount_str = match.group(1).replace(",", ".")
                        amount = amount_str
                        lists = [int(float(amount)), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Ошибка: сумма платежа не найдена почта банк", test[i][4])
                else:
                    pass
            else:
                pass
        if test[i][1] == "push":
            if test[i][2] == "Почта Банк":
                if "Пополнение" in test[i][4]:
                    match = re.search(
                        r'Пополнение (\d+\.\d{2}) RUB|Пополнение Сберегательный счет через СБП, сумма (\d+\.\d{2})р',
                        test[i][4].replace('\xa0', ' '))
                    if match:
                        amount_str = match.group(1) or match.group(2)
                        amount_str = amount_str.replace(",", ".")
                        amount = amount_str
                        lists = [int(float(amount)), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Ошибка: сумма платежа не найдена почта банк", test[i][4])
                else:
                    pass
            else:
                pass

    return sum


async def check_you(test):
    sum = []
    for i in range(len(test)):
        if test[i][1] == "push":
            if test[i][2] == "1960":
                pass
            else:
                pass
        elif test[i][1] == "sms":
            if test[i][2] == "1960" or "YouMoney":
                if "пополнен" in test[i][4]:
                    match = re.search(r"пополнен на (\d+)", test[i][4].replace('\xa0', ' '))
                    if match:
                        amount = int(match.group(1))
                        lists = [int(float(amount)), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Сумма платежа не найдена youmone", test[i][4])
                else:
                    pass
            else:
                pass
    return sum


async def check_kuban(test):
    sum = []
    for i in range(len(test)):
        if test[i][1] == "sms":
            if test[i][2] == "KubanKredit":
                if "Пополнение" in test[i][4]:
                    match = re.search(r'\b(\d+(?:\.\d+)?)[pр]\b', test[i][4].replace('\xa0', ' '))
                    if match:
                        amount = match.group(1)
                        lists = [int(float(amount)), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Сумма платежа не найдена")
                else:
                    pass
            else:
                pass
        elif test[i][1] == "push":
            if test[i][2] == "Кубань Кредит":
                if "Пополнение" in test[i][4] or "Получено" in test[i][4]:
                    match = re.search(r"(\d+\.?\d*)\s?[рp]", test[i][4].replace('\xa0', ' '))
                    if match:
                        amount = match.group(1)
                        lists = [int(float(amount)), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Сумма платежа не найдена")
                else:
                    pass
            else:
                pass
        else:
            pass
    return sum


async def check_home(test):
    sum = []
    for i in range(len(test)):
        if test[i][1] == "sms":
            if test[i][2] == "HomeBank":
                if "Popolnenie" or "Postuplenie" in test[i][4]:
                    match = re.search(r"(\d+\.\d{2}) RUR", test[i][4].replace('\xa0', ' '))
                    if match:
                        amount = match.group(1)
                        lists = [int(float(amount)), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Сумма платежа не найдена хоумкредит", test[i][4])
                else:
                    pass
            else:
                pass
        else:
            pass
    return sum


async def check_otkr(test):
    sum = []
    for i in range(len(test)):
        if test[i][1] == "sms":
            if test[i][2] == "OTKRITIE":
                if "Зачислено" in test[i][4]:
                    match = re.search(r"(\d+(?:\s\d+)*)\sр", test[i][4].replace('\xa0', ' '))
                    if match:
                        amount = match.group(1).replace(" ", "")
                        lists = [int(float(amount)), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Сумма платежа не найдена открытие смс", test[i][4])
                else:
                    pass
            else:
                pass
        else:
            pass
    return sum


async def check_rncb(test):
    sum = []
    for i in range(len(test)):
        if test[i][1] == "sms":
            if test[i][2] == "RNCB":
                if "Zachislenie" in test[i][4]:
                    match = re.search(r"summa:\s(\d+\.\d{2})\sRUR", test[i][4].replace('\xa0', ' '))
                    if match:
                        amount = match.group(1).replace(" ", "")
                        lists = [int(float(amount)), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Сумма платежа не найдена смс рнкб", test[i][4])
                else:
                    pass
            else:
                pass
        elif test[i][1] == "push":
            if test[i][2] == "РНКБ 24/7":
                if "Зачисление" or "Zachislen" in test[i][4]:
                    match = re.search(r"(\d+\.\d{2})\s?(RUR|руб\.)", test[i][4].replace('\xa0', ' '))
                    if match:
                        amount = match.group(1).replace(" ", "")
                        lists = [int(float(amount)), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Сумма платежа не найдена пуш рнкб", test[i][4])
                else:
                    pass
            else:
                pass
    return sum


async def check_sovcom(test):
    sum = []
    for i in range(len(test)):
        if test[i][1] == "sms":
            if test[i][2] == "Sovcombank":
                if "пополнена" or "пополнение" in test[i][4]:
                    match = re.search(r"(\d+|\d+\.\d+)\s?р\.", test[i][4].replace('\xa0', ' '))
                    if match:
                        amount = match.group(1).replace(" ", "")
                        lists = [int(float(amount)), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Сумма платежа не найдена")
                else:
                    pass
            else:
                pass
        elif test[i][1] == "push":
            if test[i][2] == "Халва-Совкомбанк":
                if "пополнена" or "пополнение" in test[i][4]:
                    match = re.search(r"\b(\d+(?:\.\d{2})?)\s*(?:р|руб)\b", test[i][4].replace('\xa0', ' '))
                    if match:
                        amount = match.group(1).replace(" ", "")
                        lists = [int(float(amount)), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Сумма платежа не найдена")
                else:
                    pass

            else:
                pass
        else:
            pass
    return sum


async def check_raif(test):
    sum = []
    for i in range(len(test)):
        if test[i][1] == "push":
            if test[i][2] == "Raiffeisen":
                if "Пришел перевод" or "пополнили" in test[i][3]:
                    match = re.search(r"\+ ([\d\s]+\.\d{2})", test[i][4].replace('\xa0', ' '))
                    if match:
                        amount = match.group(1).replace(" ", "")
                        lists = [int(float(amount)), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Сумма платежа не найдена пуш райфа", test[i][4])
                else:
                    pass
            else:
                pass
        else:
            pass
    return sum


async def check_mts(test):
    sum = []
    for i in range(len(test)):
        if test[i][1] == "push":
            if test[i][2] == "МТС Банк 2.0":
                if "Поступление" in test[i][4] or "Перевод" in test[i][4]:
                    match = re.search(r'(\d{1,3}(?:\s?\d{3})*)(?:,\d{2})? RUB|\b(\d{1,3}(?:\s?\d{3})*)р\b',
                                      test[i][4].replace('\xa0', ' '))
                    if match:
                        amount = match.group(1) or match.group(2)
                        if amount:  # Добавьте эту проверку
                            amount = amount.replace(" ", "")
                            lists = [int(amount), test[i][0]]
                            sum.append(lists)
                        else:
                            print("Сумма платежа не найдена")
                    else:
                        print("Сумма платежа не найдена")
                else:
                    pass
            else:
                pass
        if test[i][1] == "sms":
            if test[i][2] == "MTS-Bank":
                if "Поступление" in test[i][4]:
                    match = re.search(r'\b(\d+)р\b', test[i][4].replace('\xa0', ' '))
                    if match:
                        amount = match.group(1).replace(" ", "")
                        lists = [int(float(amount)), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Сумма платежа не найдена")
                else:
                    pass
            else:
                pass
        else:
            pass
    print(sum)
    return sum


async def check_ozon(test):
    sum = []
    for i in range(len(test)):
        if test[i][1] == "push":
            if test[i][2] == "Ozon Банк":
                if "Пополнение" in test[i][4]:
                    match = re.search(r'\bна\s+(\d[\d\s]*?)\s*₽', test[i][4].replace('\xa0', ' '))
                    if match:
                        amount = match.group(1)
                        if amount:  # Добавьте эту проверку
                            amount = amount.replace(" ", "")
                            lists = [int(amount), test[i][0]]
                            sum.append(lists)
                        else:
                            print("Сумма платежа не найдена")
                    else:
                        print("Сумма платежа не найдена")
                else:
                    pass
            else:
                pass
        if test[i][1] == "sms":
            pass
    return sum


async def check_megafon(test):
    sum = []
    for i in range(len(test)):
        if test[i][1] == "sms":
            if test[i][2] == "MegaFon":
                if "Платеж" in test[i][4]:
                    match = re.search(r'Платеж от \d{2}\.\d{2}\.\d{4} в \d{2}:\d{2} на (\d+) руб\. зачислен\.'
                                      , test[i][4].replace('\xa0', ' '))
                    if match:
                        amount = match.group(1)
                        lists = [int(float(amount)), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Сумма платежа не найдена")
                else:
                    pass
            else:
                pass
    return sum


async def check_you(test):
    sum = []
    for i in range(len(test)):
        if test[i][1] == "push":
            if test[i][2] == "ЮMoney":
                if "Пришли" in test[i][3]:
                    match = re.search(r'(\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})?)\s*₽', test[i][4].replace('\xa0', ' '))
                    if match:
                        amount = match.group(1).replace(",", ".")
                        lists = [int(float(amount)), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Сумма платежа не найдена")
            else:
                pass
        elif test[i][1] == "sms":
            if test[i][2] == "1960" or "YouMoney":
                if "пополнен" in test[i][4]:
                    match = re.search(r"пополнен на (\d+)", test[i][4].replace('\xa0', ' '))
                    if match:
                        amount = int(match.group(1))
                        lists = [int(float(amount)), test[i][0]]
                        sum.append(lists)
                    else:
                        print("Сумма платежа не найдена")
                else:
                    pass
            else:
                pass
    return sum




async def check_sum(name_bank):
    print(name_bank)
    if name_bank == "Сбербанк":
        test = conn.execute("SELECT * FROM banks WHERE name_bank = 'СберБанк' OR name_bank='900'").fetchall()
        return await check_sberbank(test)
    elif name_bank == "Тинькофф":
        test = conn.execute("SELECT * FROM banks").fetchall()
        return await check_tinkoff(test)
    elif name_bank == "Перевод на карту":
        test = conn.execute("SELECT * FROM banks").fetchall()
        return await check_ural(test) + await check_pochta(test) + await check_tinkoff(test) + await check_mts(
            test) + await check_alphabank(test) + await check_kuban(test) + await check_rncb(test) + await check_ozon(
            test)
    elif name_bank == "СБП":
        test = conn.execute("SELECT * FROM banks").fetchall()
        return await check_mts(test) + await check_pochta(test) + await check_ural(test) + await check_rshb(
            test) + await check_sberbank(test) + await check_tinkoff(test) + await check_alphabank(
            test) + await check_kuban(test) + await check_ozon(test)
    elif name_bank == "Мобильная связь":
        test = conn.execute("SELECT * FROM banks").fetchall()
        return await check_megafon(test)
    elif name_bank == "ЮMoney":
        test = conn.execute("SELECT * FROM banks").fetchall()
        return await check_you(test)
    else:
        print("Ошибка: неизвестный тип оплаты")
        return []
