def format_number(num):
    str_num = "{:.10f}".format(num)
    formatted_num = str_num.rstrip('0').rstrip('.') if '.' in str_num else str_num
    return formatted_num