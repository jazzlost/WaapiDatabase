import time
from wd_client import client as wdc

from wd_sqlite_interface import *
from wd_config import *


def main():
    
    client = wdc()
    client.connect()

    client.handle_event()

    c, conn = create_database("waapi")
    for key, value in sql_tables.items():
        create_table(key, value, c)

    values = ["{123456-789-10111213-1415}", "Play_test", "{456456-56156-4565}", "Play", "{156156-4555645-1454154}"]

    insert_data("Event", values, c, conn)
    
    client.disconnect()

if __name__ == "__main__":
    main()