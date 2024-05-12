import aiohttp
import asyncio
import logging
import json

api = "bd729e895e84210bcfd8e985b7feb8226eefba79a5fb72d35ed0625adc074252"


async def get_pars(amount, val_in, val_out):
    try:
        async with aiohttp.ClientSession(trust_env=True) as session:
            url = f"https://min-api.cryptocompare.com/data/pricemulti?fsyms={val_in}&tsyms={val_out}&api_key={api}"
            async with session.get(url) as response:
                if response.status == 200:
                    content = json.loads(await response.text())
                    print(content[val_in][val_out] * amount)
                else:
                    print("пиздарики")


    except Exception as e:
        logging.warning(e)


if __name__ == "__main__":
    asyncio.run(get_pars(0.001, "LTC", "RUB"))
