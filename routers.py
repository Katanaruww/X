import sqlite3

import config

conn = sqlite3.connect(config.name_db[0], check_same_thread=False)
curs = conn.cursor()


async def start_db(user_id, f_name, l_name):
    curs.execute("INSERT INTO users (id_us, tag, name) VALUES (?, ?, ?)", (user_id, f_name, l_name))
    conn.commit()


async def check_us(us_id):
    try:
        row = curs.execute("SELECT * FROM users WHERE id_us = ?", (us_id,)).fetchone()
        return row
    except:
        pass  # logging в файлы
