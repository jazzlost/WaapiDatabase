##################################### Program Entrance #######################################################
import sys
import os
from wd_client import client as wdc
from wd_sqlite_interface import *
from wd_sqlite_utils import *
from wd_config import *


def main():
    # Get path and name argv
    if len(sys.argv) < 2:
        sql_database_path = os.getcwd()
        sql_database_name = "Waapi"
    else:
        sql_database_path = sys.argv[1]
        sql_database_name = sys.argv[2]

    sql_database_path = sql_database_path.replace('\\', '/')

    # Make WAMP client
    client = wdc()
    # Make WAMP connection
    client.connect()
    # Catch waapi datas
    client.catch_datas(sql_database_path)
    # Create database
    conn = create_database(sql_database_path, sql_database_name)
    # Create tables
    for key, value in sql_tables.items():
        create_table(key, value, conn)
    # Convert waapi data to sql data and insert/update them
    for i, datagroup in enumerate(client.datas):
        data_ids = set()
        for data in datagroup:
            if i == 1 or i == 2:
                sql_values = data_convert(data, True)
            else:
                sql_values = data_convert(data, False)

            table = list(sql_tables.keys())[i]
            if "Id" in data:
                data_ids.add(data["Id"])

            # Check was new object added
            if is_new_id(table, data, conn):
                insert_data(table, sql_values, conn)
            else:
            # Check was modification made and update Database
                column_diff, id_diff = diff_data(table, sql_values, conn)
                update_data(table, column_diff, id_diff, conn)
        # Check was old object deleted and remove from Database
        delete_data(table, data_ids, conn)
    # Close database
    close_database(conn)
    # Close WAMP connection
    client.disconnect()


if __name__ == "__main__":
    main()