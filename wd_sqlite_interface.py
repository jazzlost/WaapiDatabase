################################ SQLite Interface ############################################
import sqlite3
import time
import datetime
import random

from wd_config import sql_tables
from wd_sqlite_utils import *


# Create database with path and name
def create_database(path, name):
    fullname = path + "/" + name + ".db"
    conn = sqlite3.connect(fullname)
    return conn


# Close database
def close_database(conn):
    cursor = conn.cursor()
    cursor.close()
    conn.close()


# Execute sql with close cursor
def safe_execute(sql, conn):
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()


# Create table
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


# Delete table
def delete_table(table_name, conn):
    sql = "DROP TABLE IF EXISTS " + str(table_name)
    safe_execute(sql, conn)


# Insert datas into table
# TODO: Make sure values num is equal to table's column num
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


# Query data from table
def query_data(sql, conn):
    if len(sql) > 0:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()


# Check if new id added(old id use update/new id use insert)
def is_new_id(table_name, data, conn):
    query_sql = "SELECT * FROM " + str(table_name) + " " + "WHERE Id = " + "'" + data.get("Id") + "'"
    query_datas = query_data(query_sql, conn)

    if len(query_datas) > 0:
        return False
    else:
        return True

# Get all ids from table, return as a set
def query_all_id(table_name, conn):
    query_sql = "SELECT Id FROM " + str(table_name)
    query_datas = query_data(query_sql, conn)

    return_datas = set()
    for id in query_datas:
        return_datas.add(id[0])
    
    return return_datas


# Diff waapi data with sql data and mark all modified columns
def diff_data(table_name, data, conn):

    # Mark all modified object
    query_sql = "SELECT * FROM " + str(table_name) + " " + "WHERE Id = " + "'" + data[0] + "'"
    query_datas = query_data(query_sql, conn)

    diff_property = {}

    for i in range(len(query_datas[0])):
        if data[i] != query_datas[0][i]:
            column = list(sql_tables[table_name].keys())[i]
            diff_property[column] = data[i]

    if len(diff_property) <= 0:
        return "", ""

    column_sql = ""
    for column, value in diff_property.items():
        column_sql += str(column) + " = " + "'" + str(value) + "'" + ","
    column_sql = remove_last_comma(column_sql)

    if len(column_sql) <= 0:
        return "", ""

    return column_sql, data[0]


# Update data
def update_data(table_name, column_sql, id, conn):
    if len(table_name) > 0 and len(column_sql) > 0 and len(id) > 0:
        sql = "UPDATE " + str(table_name) + " SET " + column_sql + " WHERE ID = " + "'" + id + "'"
        safe_execute(sql, conn)


# Delete data
def delete_data(table_name, data_ids, conn):
    # Query all ids of this table from Dababase
    database_ids = query_all_id(table_name, conn)
    # Find all deleted_ids by comparing two ids sets
    deleted_ids = [database_ids.difference(data_ids)]

    # Delete object from Database
    for id in deleted_ids[0]:
        if len(id) > 0:
            sql = "DELETE FROM " + str(table_name) + " " + "WHERE Id = " + "'" + id + "'"
            safe_execute(sql, conn)