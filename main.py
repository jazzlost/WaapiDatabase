import time
from wd_client import client as wdc

from wd_sqlite_interface import *
from wd_config import *


def main():
    
    client = wdc()
    client.connect()

    client.handle_event()

    c = create_database("waapi")
    for key, value in sql_tables.items():
        create_table(key, value, c)

    
    client.disconnect()


if __name__ == "__main__":
    main()