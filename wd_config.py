import json
import os
import sys

class configurer(object):

    def __init__(self, file):
        config = {}
        try:
            with open(file) as f:
                config = json.load(f)
        except FileNotFoundError:
            print("WaapiDatabase:Error:No Valid config json file Exist!")
            sys.exit(0)

        self.WaapiConfig = config.get("WaapiConfig")
        self.SqliteConfig = config.get("SqliteConfig")
        self.ParserConfig = config.get("ParserConfig")


config_path = ""

if len(sys.argv) < 3:
    config_path = os.getcwd() + "/waapi_config.json"
else:
    config_path = sys.argv[3] + "/waapi_config.json"

# Create global config object
g_config = configurer(config_path)

################################ Waapi Config ############################################

try:
    waapi_config = g_config.WaapiConfig

    invalid_id = waapi_config.get("invalid_id")

    event_config = waapi_config.get("event_config")

    action_config = waapi_config.get("action_config")

    # Dict properties for target
    target_config = waapi_config.get("target_config")

    # List properties for target
    target_list_config = waapi_config.get("target_list_config")

    switchgroup_config = waapi_config.get("switchgroup_config")

    stategroup_config = waapi_config.get("stategroup_config")

    atten_config = waapi_config.get("atten_config")

    rtpc_config = waapi_config.get("rtpc_config")

    ################################ SQLite Config ############################################

    sql_tables = g_config.SqliteConfig.get("sql_tables")

    sql_project_table = sql_tables.get("sql_project_table")

    sql_event_table = sql_tables.get("sql_event_table")

    sql_target_table = sql_tables.get("sql_target_table")

    sql_switch_table = sql_tables.get("sql_switch_table")

    sql_state_table = sql_tables.get("sql_state_table")

    sql_atten_table = sql_tables.get("sql_atten_table")

    sql_rtpc_table = sql_tables.get("sql_rtpc_table")


    ################################ Parser Config ############################################

    parser_config = g_config.ParserConfig

    container_tags = parser_config.get("container_tags")

    wwu_root = parser_config.get("wwu_root")

except AttributeError:
    print("WaapiDatabase:Error:Config file load failed!")
