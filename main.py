import time
from wd_client import client as wdc

from wd_sqlite_interface import *
from wd_sqlite_utils import *
from wd_config import *


def main():
    
    client = wdc()
    client.connect()

    client.handle_event()

    # conn = create_database(sql_database_name)

    # for table in sql_tables.keys():
    #     delete_table(table, conn)
    
    # for key, value in sql_tables.items():
    #     create_table(key, value, conn)

    # for i, datagroup in enumerate(client.datas):
    #     for data in datagroup:
    #         if i == 0 or i == 1:
    #             sql_values = data_convert(data, True)
    #         else:
    #             sql_values = data_convert(data, False)
            
    #         table = list(sql_tables.keys())[i]
    #         insert_data(table, sql_values, conn)

    # value = ["{BE62A22-4503-4000-BF91-55F767088450}", "Play_Change", "{1F7CFB54-E9A0-408A-9524-D142401504A6}", 2, "{ECA4B107-100C-43B6-928E-DCEDCA7A4FC9}"]
    # update_data("Event", value, conn)

    # close_database(conn)
    
    client.disconnect()

if __name__ == "__main__":
    main()