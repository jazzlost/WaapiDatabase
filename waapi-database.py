import sys
from wd_client import client as wdc
from wd_sqlite_interface import *
from wd_sqlite_utils import *
from wd_config import *


def main():

    # if len(sys.argv) < 2:
    #     return

    # sql_database_path = sys.argv[1]
    # if len(sys.argv) > 2:
    #     sql_database_name = sys.argv[2]
    # else:
        # sql_database_name = "waapi"

    sql_database_name = "waapi"
    sql_database_path = "./"

    client = wdc()
    client.connect()

    client.catch_datas()

    conn = create_database(sql_database_path, sql_database_name)

    # for table in sql_tables.keys():
    #     delete_table(table, conn)

    for key, value in sql_tables.items():
        create_table(key, value, conn)

    for i, datagroup in enumerate(client.datas):
        for data in datagroup:
            if i == 0 or i == 1:
                sql_values = data_convert(data, True)
            else:
                sql_values = data_convert(data, False)

            table = list(sql_tables.keys())[i]

            if is_new_id(table, data, conn):
                insert_data(table, sql_values, conn)
            else:
                column_diff, id_diff = diff_data(table, sql_values, conn)
                update_data(table, column_diff, id_diff, conn)

    close_database(conn)

    client.disconnect()

if __name__ == "__main__":
    main()