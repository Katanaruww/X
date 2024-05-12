import aiohttp
import asyncio
import logging
import json
import requests
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


async def get_pars2(val_in, val_out, amount):
    try:
        async with aiohttp.ClientSession(trust_env=True) as session:
            url = f"https://min-api.cryptocompare.com/data/pricemulti?fsyms={val_in}&tsyms={val_out}&api_key={api}"
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
                          "application/signed-exchange;v=b3;q=0.7",
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
            }

            req = requests.get(url=url, headers=headers)
            src = req.json()
            return float(src[val_in][val_out])*amount

    except Exception as e:
        logging.warning(e)