import asyncio

limits = {
    "RUB": [1000, 10],
    "USD": [500, 0.1],
    "IDR": [100000, 100],
    "USDT": [500, 0.1],
    "BTC": [0.0001, 0.00001],
    "LTC": [0.01, 0.001]
}


async def limits_currency_pairs(value):
    return limits[value]
