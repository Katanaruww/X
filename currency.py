import aiohttp
import asyncio
import logging
import json

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s", encoding="UTF-8")
api = "bd729e895e84210bcfd8e985b7feb8226eefba79a5fb72d35ed0625adc074252"


async def get_pars(amount, val_in, val_out):
    try:
        async with aiohttp.ClientSession(trust_env=True) as session:
            url = f"https://min-api.cryptocompare.com/data/pricemulti?fsyms={val_in}&tsyms={val_out}&api_key={api}"
            async with session.get(url) as response:
                if response.status == 200:
                    content = json.loads(await response.text())
                    return content[val_in][val_out]
                else:
                    logging.warning(response)
    except Exception as e:
        logging.warning(e)
