import sqlite3
import time
import datetime
import random

def create_database():
    conn = sqlite3.connect("waapi.db")
    c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS waapiTable(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')


def data_entry():
    c.execute("INSERT INTO waapiTable VALUES(123456, '2020-07-10','python', 4)")
    conn.commit()
    c.close()
    conn.close()


def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'python'
    value = random.randrange(0, 10)
    c.execute("INSERT INTO waapiTable(unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)", (unix, date, keyword, value))
    conn.commit()


def read_from_db():
    c.execute('SELECT * FROM waapiTable where value > 3')
    for row in c.fetchall():
        print(row)


def graph_data():
    c.execute('SELECT unix, value FROM waapiTable')
    dates = []
    values = []
    for row in c.fetchall():
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-')
    plt.show()
        

def del_and_update():
    c.execute('SELECT * FROM waapiTable')
    [print(row) for row in c.fetchall()]

    c.execute('UPDATE waapiTable SET value = 99 WHERE value = 8')
    conn.commit()

    c.execute('DELETE FROM waapiTable WHERE value = 99')
    conn.commit()


# create_table()
# data_entry()

# for i in range(10):
#     dynamic_data_entry()
#     time.sleep(1)

# read_from_db()
# graph_data()

del_and_update()

c.close()
conn.close()