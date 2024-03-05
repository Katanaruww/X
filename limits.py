import asyncio

limits = {
    "RUB": 10000,
    "USD": 500,
    "IDR": 100000,
    "USDT": 500,
    "BTC": 0.0001,
    "LTC": 0.01
}


async def limits_currency_pairs(value):
    return limits[value]


asyncio.run(limits_currency_pairs("USD"))
