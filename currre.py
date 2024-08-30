import aiohttp
import asyncio
import logging
import json
import requests
from aiogram import types
from func import (get_values_from_column, get_values_from_column2, get_values_from_column3, get_values_from_column4, get_values_from_column6, get_values_from_column5, get_values_from_column7 ,get_values_from_column8, get_values_from_column9, get_values_from_column10)
from inline_but import *
from routers import check_lang
api = "bd729e895e84210bcfd8e985b7feb8226eefba79a5fb72d35ed0625adc074252"

async def get_pars5(val_in, val_out, amount, call: types.CallbackQuery):
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
            lang = await check_lang(call.message.chat.id)
            print(val_in, "1")
            print(val_out, "2")
            if val_in == "RUB" and val_out == "IDR":
                c1_values = await get_values_from_column('c1')
                c2_values = await get_values_from_column('c2')
                c3_values = await get_values_from_column('c3')
                c4_values = await get_values_from_column('c4')
                c5_values = await get_values_from_column('c5')

                values1 = (float(src[val_in][val_out]) * amount) + (((float(src[val_in][val_out]) * amount) / 100) * int(c1_values[-1]))
                values2 = (float(src[val_in][val_out]) * amount) + (((float(src[val_in][val_out]) * amount) / 100) * int(c2_values[-1]))
                values3 = (float(src[val_in][val_out]) * amount) + (((float(src[val_in][val_out]) * amount) / 100) * int(c3_values[-1]))
                values4 = (float(src[val_in][val_out]) * amount) + (((float(src[val_in][val_out]) * amount) / 100) * int(c4_values[-1]))
                values5 = (float(src[val_in][val_out]) * amount) + (((float(src[val_in][val_out]) * amount) / 100) * int(c5_values[-1]))

                await call.message.answer(f"RUB 🔄 IDR\n✅10.000 ₽ - 50.000 ₽ - {str(round(values1, 2))} IDR\n✅50.000 ₽ - 100.000 ₽ - {str(round(values2, 2))} IDR\n✅100.000 ₽ - 300.000 ₽ - {str(round(values3, 2))} IDR\n✅300.000 ₽ - 500.000 ₽ - {str(round(values4, 2))} IDR\n✅500.000 ₽ - 1.000.000 ₽ - {str(round(values5, 2))} IDR", reply_markup=olesia222(lang).as_markup())
            if val_in == "IDR" and val_out == "RUB":
                c1_values = await get_values_from_column('c1')
                c2_values = await get_values_from_column('c2')
                c3_values = await get_values_from_column('c3')
                c4_values = await get_values_from_column('c4')
                c5_values = await get_values_from_column('c5')

                values1 = (float(src[val_in][val_out]) * amount) + (((float(src[val_in][val_out]) * amount) / 100) * int(c1_values[-1]))
                values2 = (float(src[val_in][val_out]) * amount) + (((float(src[val_in][val_out]) * amount) / 100) * int(c2_values[-1]))
                values3 = (float(src[val_in][val_out]) * amount) + (((float(src[val_in][val_out]) * amount) / 100) * int(c3_values[-1]))
                values4 = (float(src[val_in][val_out]) * amount) + (((float(src[val_in][val_out]) * amount) / 100) * int(c4_values[-1]))
                values5 = (float(src[val_in][val_out]) * amount) + (((float(src[val_in][val_out]) * amount) / 100) * int(c5_values[-1]))

                await call.message.answer(f"IDR 🔄 RUB\n✅2,000,000 IDR - 10,000,000 IDR - {str(round(values1, 4))} ₽\n✅10,000,000 IDR - 30,000,000 IDR  - {str(round(values2, 4))} ₽\n✅30,000,000 IDR - 50,000,000 IDR  - {str(round(values3, 4))} ₽\n✅50,000,000 IDR - 100,000,000 IDR  - {str(round(values4, 4))} ₽\n✅100,000,000 IDR - 300,000,000 IDR - {str(round(values5, 4))} ₽", reply_markup=olesia222(lang).as_markup())
            if val_in == "RUB" and (val_out == "USDT" or val_out == "USD"):
                c1 = await get_values_from_column2("c1")
                await call.message.answer(f"RUB 🔄 USD(USDT)\n{str(round((float(src[val_in][val_out]) * amount) + (((float(src[val_in][val_out]) * amount) / 100) * int(c1[-1])), 2))}$", reply_markup=olesia222(lang).as_markup())
            if (val_in == "USDT" or val_in == "USD") and val_out == "RUB":
                c2 = await get_values_from_column2("c1")
                await call.message.answer(f"USD(USDT) 🔄 RUB\n{str(round((float(src[val_in][val_out]) * amount) + (((float(src[val_in][val_out]) * amount) / 100) * int(c2[-1])), 2))}₽", reply_markup=olesia222(lang).as_markup())
            if val_in == "IDR" and (val_out == "USDT" or val_out == "USD"):
                c1_values = await get_values_from_column3('c1')
                c2_values = await get_values_from_column3('c2')
                c3_values = await get_values_from_column3('c3')
                c4_values = await get_values_from_column3('c4')
                c5_values = await get_values_from_column3('c5')

                values1 = (float(src[val_in][val_out]) * amount) + (
                            ((float(src[val_in][val_out]) * amount) / 100) * int(c1_values[-1]))

                values2 = (float(src[val_in][val_out]) * amount) + (
                            ((float(src[val_in][val_out]) * amount) / 100) * int(c2_values[-1]))

                values3 = (float(src[val_in][val_out]) * amount) + (
                            ((float(src[val_in][val_out]) * amount) / 100) * int(c3_values[-1]))

                values4 = (float(src[val_in][val_out]) * amount) + (
                            ((float(src[val_in][val_out]) * amount) / 100) * int(c4_values[-1]))

                values5 = (float(src[val_in][val_out]) * amount) + (
                            ((float(src[val_in][val_out]) * amount) / 100) * int(c5_values[-1]))
                await call.message.answer(
                    f"IDR 🔄 USD(USDT)\n✅2,000,000 IDR - 10,000,000 IDR - {(f'{values1:.6f}')} $\n✅10,000,000 IDR - 30,000,000 IDR  - {(f'{values2:.6f}')} $\n✅30,000,000 IDR - 50,000,000 IDR  - {(f'{values3:.6f}')} $\n✅50,000,000 IDR - 100,000,000 IDR  - {(f'{values4:.6f}')} $\n✅100,000,000 IDR - 300,000,000 IDR - {(f'{values5:.6f}')} $",
                    reply_markup=olesia222(lang).as_markup())

            if (val_in == "USDT" or val_in == "USD") and val_out == "IDR":
                c1_values = await get_values_from_column3('c1')
                c2_values = await get_values_from_column3('c2')
                c3_values = await get_values_from_column3('c3')
                c4_values = await get_values_from_column3('c4')
                c5_values = await get_values_from_column3('c5')

                values1 = (float(src[val_in][val_out]) * amount) + (
                            ((float(src[val_in][val_out]) * amount) / 100) * int(c1_values[-1]))

                values2 = (float(src[val_in][val_out]) * amount) + (
                            ((float(src[val_in][val_out]) * amount) / 100) * int(c2_values[-1]))

                values3 = (float(src[val_in][val_out]) * amount) + (
                            ((float(src[val_in][val_out]) * amount) / 100) * int(c3_values[-1]))

                values4 = (float(src[val_in][val_out]) * amount) + (
                            ((float(src[val_in][val_out]) * amount) / 100) * int(c4_values[-1]))

                values5 = (float(src[val_in][val_out]) * amount) + (
                            ((float(src[val_in][val_out]) * amount) / 100) * int(c5_values[-1]))
                await call.message.answer(
                    f"(USD(USDT) 🔄 IDR)\n✅200 $ - 500 $ - {(f'{values1:.2f}')} IDR\n✅500 $ - 1.000 $   - {(f'{values2:.2f}')} IDR\n✅1.000 $ - 5.000 $  - {(f'{values3:.2f}')} IDR\n✅5.000 $ - 10.000 $  - {(f'{values4:.2f}')} IDR\n✅10.000 $ - 50.000 $ - {(f'{values5:.2f}')} IDR",
                    reply_markup=olesia222(lang).as_markup())
            if val_in == "BTC" and val_out == "RUB":
                c1_values = await get_values_from_column4('c1')
                print(c1_values)
                values1 = (float(src[val_in][val_out]) * amount) + (
                        ((float(src[val_in][val_out]) * amount) / 100) * int(c1_values[-1]))
                print(values1)
                await call.message.answer(f"BTC 🔄 RUB\n{(f'{values1:.2f}')}", reply_markup=olesia222(lang).as_markup())


            if val_in == "RUB" and val_out == "BTC":
                c1_values = await get_values_from_column4('c1')
                values1 = (float(src[val_in][val_out]) * amount) + (
                        ((float(src[val_in][val_out]) * amount) / 100) * int(c1_values[-1]))
                await call.message.answer(f"RUB 🔄 BTC\n{(f'{values1:.9f}')}₽", reply_markup=olesia222(lang).as_markup())



            if val_in == "BTC" and val_out == "IDR":
                c1_values = await get_values_from_column5('c1')
                values1 = (float(src[val_in][val_out]) * amount) + (
                        ((float(src[val_in][val_out]) * amount) / 100) * int(c1_values[-1]))
                await call.message.answer(f"BTC 🔄 IDR\n{(f'{values1:.2f}')}", reply_markup=olesia222(lang).as_markup())

            if val_in == "IDR" and val_out == "BTC":
                c1_values = await get_values_from_column5('c1')
                values1 = (float(src[val_in][val_out]) * amount) + (
                        ((float(src[val_in][val_out]) * amount) / 100) * int(c1_values[-1]))
                await call.message.answer(f"IDR 🔄 BTC\n{(f'{values1:.9f}')} BTC",
                                          reply_markup=olesia222(lang).as_markup())

            if val_in == "LTC" and val_out == "IDR":
                c1_values = await get_values_from_column6('c1')
                values1 = (float(src[val_in][val_out]) * amount) + (
                        ((float(src[val_in][val_out]) * amount) / 100) * int(c1_values[-1]))
                await call.message.answer(f"LTC 🔄 IDR\n{(f'{values1:.2f}')}", reply_markup=olesia222(lang).as_markup())

            if val_in == "IDR" and val_out == "LTC":
                c1_values = await get_values_from_column6('c1')
                values1 = (float(src[val_in][val_out]) * amount) + (
                        ((float(src[val_in][val_out]) * amount) / 100) * int(c1_values[-1]))
                await call.message.answer(f"IDR 🔄 LTC\n{(f'{values1:.9f}')}",
                                          reply_markup=olesia222(lang).as_markup())

            if val_in == "LTC" and val_out == "RUB":
                c1_values = await get_values_from_column7('c1')
                values1 = (float(src[val_in][val_out]) * amount) + (
                        ((float(src[val_in][val_out]) * amount) / 100) * int(c1_values[-1]))
                await call.message.answer(f"LTC 🔄 RUB\n{(f'{values1:.2f}')}",reply_markup=olesia222(lang).as_markup())

            if val_in == "RUB" and val_out == "LTC":
                c1_values = await get_values_from_column7('c1')
                values1 = (float(src[val_in][val_out]) * amount) + (
                        ((float(src[val_in][val_out]) * amount) / 100) * int(c1_values[-1]))
                await call.message.answer(f"RUB 🔄 LTC\n{(f'{values1:.9f}')}",
                                          reply_markup=olesia222(lang).as_markup())

            if val_in == "BTС" and val_out == "LTC":
                c1_values = await get_values_from_column8('c1')
                values1 = (float(src[val_in][val_out]) * amount) + (
                        ((float(src[val_in][val_out]) * amount) / 100) * int(c1_values[-1]))
                await call.message.answer(f"(BTC 🔄 LTC)\n{(f'{values1:.9f}')} LTC",
                                          reply_markup=olesia222(lang).as_markup())

            if val_in == "LTC" and val_out == "BTC":
                c1_values = await get_values_from_column8('c1')
                values1 = (float(src[val_in][val_out]) * amount) + (
                        ((float(src[val_in][val_out]) * amount) / 100) * int(c1_values[-1]))
                await call.message.answer(f"(LTC 🔄 BTC)\n{(f'{values1:.9f}')} BTC",
                                          reply_markup=olesia222(lang).as_markup())

            if val_in == "BTС" and val_out == "LTC":
                c1_values = await get_values_from_column8('c1')
                values1 = (float(src[val_in][val_out]) * amount) + (
                        ((float(src[val_in][val_out]) * amount) / 100) * int(c1_values[-1]))
                await call.message.answer(f"(BTC 🔄 LTC)\n{(f'{values1:.9f}')} LTC",
                                          reply_markup=olesia222(lang).as_markup())
                #USDT BTC
            if (val_in == "USDT" or val_in == "USD") and val_out == "BTC":
                c1_values = await get_values_from_column9('c1')
                values1 = (float(src[val_in][val_out]) * amount) + (
                        ((float(src[val_in][val_out]) * amount) / 100) * int(c1_values[-1]))
                await call.message.answer(f"(USD(USDT) 🔄 BTC\n{(f'{values1:.9f}')} BTC",
                                          reply_markup=olesia222(lang).as_markup())

            if val_in == "BTC" and (val_out == "USD" or val_out == "USDT"):
                c1_values = await get_values_from_column9('c1')
                values1 = (float(src[val_in][val_out]) * amount) + (
                        ((float(src[val_in][val_out]) * amount) / 100) * int(c1_values[-1]))
                await call.message.answer(f"(BTC 🔄 USD(USDT))\n{(f'{values1:.2f}')} USD(USDT)",
                                          reply_markup=olesia222(lang).as_markup())
                #USDT LTC
            if (val_in == "USDT" or val_in == "USD") and val_out == "LTC":
                c1_values = await get_values_from_column10('c1')
                values1 = (float(src[val_in][val_out]) * amount) + (
                        ((float(src[val_in][val_out]) * amount) / 100) * int(c1_values[-1]))
                await call.message.answer(f"(USD(USDT) 🔄 LTC)\n{(f'{values1:.9f}')} LTC",
                                          reply_markup=olesia222(lang).as_markup())

            if val_in == "LTC" and (val_out == "USD" or val_out == "USDT"):
                c1_values = await get_values_from_column10('c1')
                values1 = (float(src[val_in][val_out]) * amount) + (
                        ((float(src[val_in][val_out]) * amount) / 100) * int(c1_values[-1]))
                await call.message.answer(f"(LTC 🔄 USD(USDT))\n{(f'{values1:.2f}')} USD(USDT)",
                                          reply_markup=olesia222(lang).as_markup())
    except Exception as e:
        logging.warning(e)
