from routers import conn
from auto.check_pay import check_sum
import asyncio
import traceback

async def close_deals(id_d):
    print("не проверенно", id_d)

async def auto_check(id_deals, name_bank):
    answer = False
    deal = conn.execute("SELECT * FROM deals_onl WHERE id_call = ?", (id_deals, )).fetchone()
    print(deal[5]) #отдаете
    try:
        for a in range(5):
            should_wait = True
            sum_deals = await check_sum(name_bank)
            for r in range(len(sum_deals)):
                print(sum_deals[r][0], deal[5])
                if sum_deals[r][0] + 1 == deal[5] or sum_deals[r][0] - 1 == deal[5] or sum_deals[r][0] == deal[5]:
                    answer = True
                    should_wait = False
                    break

            if should_wait:
                await asyncio.sleep(2)
            else:
                print("мы продолжаем")
                break
        else:
            for sum_deal in await check_sum(name_bank):
                if sum_deal[0] + 1 == deal[5] or sum_deal[0] - 1 == deal[5] or sum_deal[0] == deal[5]:
                    answer = True
                else:
                    answer = False

    except Exception as err:
        print(err)
        print(traceback.print_exc())
        return answer
    return answer
