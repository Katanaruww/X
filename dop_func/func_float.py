def format_number(num, value):
    precision = ost_def(value)
    str_num = "{:.{}f}".format(num, precision)
    formatted_num = str_num.rstrip('0').rstrip('.') if '.' in str_num else str_num
    return formatted_num

def ost_def(value):
    if value == "RUB" or value == "IDR" or value == "USD" or value == "USDT":
        x = 2
    if value == "LTC":
        x = 3
    if value == "BTC":
        x = 8
    return x