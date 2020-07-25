import time
from formula_client import formula_client as fc

from wd_sqlite_interface import *
from wd_config import *


def main():
    
    formula = fc()
    formula.connect()
    formula.handle_project()

    # formula.handle_event()


    c = create_database("waapi")
    for key, value in sql_tables.items():
        create_table(key, value, c)

    
    formula.disconnect()


if __name__ == "__main__":
    main()