import sqlite3
import time
import datetime
import random
from wd_config import sql_tables

from wd_sqlite_utils import *

def create_database(name):
    fullname = name + ".db"
    conn = sqlite3.connect(fullname)
    c = conn.cursor()
    return c, conn


def close_database(cursor, conn):
    cursor.close()
    conn.close()


def create_table(name, table, cursor, conn):
    if len(table) > 0:
        sql = ""
        column = ""
        for key, value in table.items():
            phrase = str(key) + " " + str(value) + ","
            column += phrase
        column = remove_last_comma(column)
        sql = "CREATE TABLE IF NOT EXISTS " + str(name) + "(" + column + ");"
        cursor.execute(sql)
        conn.commit()


def delete_table(table_name, cursor, conn):
    sql = "DROP TABLE IF EXISTS " + str(table_name)
    cursor.execute(sql)
    conn.commit()


# Make sure values num is equal to table's column num
def insert_data(table_name, values, cursor, conn):
    if len(table_name) > 0 and len(values) > 0:
        sql = ""
        sql_column = ""
        sql_value = ""
        
        for key in sql_tables.get(str(table_name)).keys():
            phrase = str(key) + ","
            sql_column += phrase
        sql_column = remove_last_comma(sql_column)

        for value in values:
            phrase = "'" + str(value) + "'" + ","
            sql_value += phrase
        sql_value = remove_last_comma(sql_value)

        if not columns_check(sql_value, sql_tables.get(table_name)):
            return

        sql = "INSERT INTO " + str(table_name) + "(" + sql_column + ")" + " VALUES " + "(" + sql_value + ");"
        cursor.execute(sql)
        conn.commit()


def query_columns(table_name, cursor):
    sql = "SELECT COUNT(*) FROM " + str(table_name)
    cursor.execute(sql)
    return cursor.fetchone()


def query_database(sql, cursor):
    if len(sql) > 0:
        cursor.execute(sql)
        return cursor.fetchall()


def update_database(table_name, data, cursor, conn):
    query_sql = "SELECT * FROM " + str(table_name) + " " + "WHERE Id = " + "'" + data[0] + "'"
    query_data = query_database(query_sql, cursor)

    update_property = {}

    for i in range(len(query_data[0])):
        if data[i] != query_data[0][i]:
            column = list(sql_tables[table_name].keys())[i]
            update_property[column] = data[i]

    column_sql = ""
    for column, value in update_property.items():
        column_sql += str(column) + " = " + "'" + str(value) + "'" + ","
    column_sql = remove_last_comma(column_sql)

    sql = "UPDATE " + str(table_name) + " SET " + column_sql + " WHERE ID = " + "'" + data[0] + "'"
    cursor.execute(sql)
    conn.commit()


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

# del_and_update()

# c.close()
# conn.close()