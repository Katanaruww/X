from bs4 import BeautifulSoup
import requests


def get_pars_rub(val_in, val_out):
    list = []
    url = f"https://www.google.ru/search?q={val_in}+to+{val_out}&newwindow=1&sca_esv=c5f02fd2b2be415a&source=hp&ei=h43mZf67D5q-wPAPoo-KoAU&iflsig=ANes7DEAAAAAZeabl7UX2AjGWK2_InJukhwoa096Q1dv&udm=&ved=0ahUKEwi-m7Sok9yEAxUaHxAIHaKHAlQQ4dUDCA0&uact=5&oq=idr+to+rub&gs_lp=Egdnd3Mtd2l6IgppZHIgdG8gcnViMhAQABiABBixAxiDARhGGIICMgUQABiABDIFEAAYgAQyCBAAGBYYHhgKMggQABgWGB4YCjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB5IjR1Q_wdY8xpwAHgAkAEAmAHTAaABqA6qAQYwLjEwLjG4AQPIAQD4AQGYAgugAtIOqAIKwgIQEAAYAxiPARjlAhjqAhiMA8ICExAuGAMYjwEY5QIY1AIY6gIYjAPCAhAQLhgDGI8BGOUCGOoCGIwDwgILEAAYgAQYsQMYgwHCAggQABiABBixA8ICFBAuGIAEGIoFGLEDGIMBGMcBGNEDwgIREC4YgAQYsQMYgwEYxwEY0QPCAgsQLhiABBjHARivAcICCBAuGIAEGLEDwgILEC4YgAQYsQMYgwGYA9wBkgcGMC4xMC4xoAekkgE&sclient=gws-wiz"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
    }

    req = requests.get(url, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    new = soup.find_all(class_="a61j6")
    if new:
        print(new[0].get("value"))


get_pars_rub("RUB", "USDT")
