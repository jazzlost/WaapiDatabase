import time
from wd_client import client as wdc

from wd_sqlite_interface import *
from wd_sqlite_utils import *
from wd_config import *


def main():
    
    client = wdc()
    client.connect()

    client.handle_event()

    c, conn = create_database("waapi")
    for key, value in sql_tables.items():
        create_table(key, value, c)

    for i, datagroup in enumerate(client.datas):
        for data in datagroup:
            sql_values = data_convert(data)
            # insert_data(i, sql_values, c, conn)
    
    client.disconnect()

if __name__ == "__main__":
    main()