import sqlite3
import time
import datetime
import random
from wd_config import sql_tables

from wd_sqlite_utils import *

def create_database(name):
    fullname = name + ".db"
    conn = sqlite3.connect(fullname)
    return conn


def close_database(conn):
    cursor = conn.cursor()
    cursor.close()
    conn.close()


def safe_execute(sql, conn):
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()


def create_table(name, table, conn):
    if len(table) > 0:
        sql = ""
        column = ""
        for key, value in table.items():
            phrase = str(key) + " " + str(value) + ","
            column += phrase
        column = remove_last_comma(column)
        sql = "CREATE TABLE IF NOT EXISTS " + str(name) + "(" + column + ");"
        safe_execute(sql, conn)


def delete_table(table_name, conn):
    sql = "DROP TABLE IF EXISTS " + str(table_name)
    safe_execute(sql, conn)


# Make sure values num is equal to table's column num
def insert_data(table_name, values, conn):
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
        safe_execute(sql, conn)


def query_data(sql, conn):
    if len(sql) > 0:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()


def diff_data(table_name, data, conn):
    query_sql = "SELECT * FROM " + str(table_name) + " " + "WHERE Id = " + "'" + data[0] + "'"
    query_datas = query_data(query_sql, conn)

    diff_property = {}

    for i in range(len(query_datas[0])):
        if data[i] != query_datas[0][i]:
            column = list(sql_tables[table_name].keys())[i]
            diff_property[column] = data[i]

    column_sql = ""
    for column, value in diff_property.items():
        column_sql += str(column) + " = " + "'" + str(value) + "'" + ","
    column_sql = remove_last_comma(column_sql)

    return column_sql


def update_data(table_name, column_sql, id, conn):
    sql = "UPDATE " + str(table_name) + " SET " + column_sql + " WHERE ID = " + "'" + id + "'"
    safe_execute(sql, conn)


def delete_data(table_name, Id, conn):
    sql = "DELETE FROM " + str(table_name) + " " + "WHERE Id = " + "'" + Id + "'"
    safe_execute(sql, conn)


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