################################ Waapi Config ############################################

event_config = {
   "Id": "id",
   "Name": "name"
}

action_config = {
    "ActionId": "id",
    "ActionType": "@ActionType",
    "Target": "@Target"
}

# Dict properties for target
target_config = {
    "Id": "id",
    "Name": "name",
    "Volume": "@Volume",
    "Pitch": "@Pitch",
    "LPF": "@Lowpass",
    "HPF": "@Highpass",
    "UseMaxSoundInstance": "@@UseMaxSoundPerInstance",
    "MaxSound": "@@UseMaxSoundPerInstance",
    "UseListenerRelativeRoute": "@@ListenerRelativeRouting",
    "Spatialization3D": "@@3DSpatialization",
    "Attenuation": "@@Attenuation"
}

# List properties for target
target_list_config = {
    "SwitchOrStateGroup": "@SwitchGroupOrStateGroup"
}

switchgroup_config = {
    "SwitchGroup": "@SwitchGroupOrStateGroup"
}

stategroup_config = {
    "StateGroup": "StateGroup"
}

atten_config = {
    "Id": "id",
    "Name": "name",
    "MaxDistance": "@@RadiusMax",
    "UseCone": "@@ConeUse"
}

rtpc_config = {
    "Id": "id",
    "Name": "name",
    "UseBuildInParam": "@BindToBuiltInParam",
    "DefaultValue": "@InitialValue",
    "Max": "@Max",
    "Min": "@Min"
}

################################ SQLite Config ############################################

sql_project_table = {
    "Id": "VARCHAR PRIMARY KEY NOT NULL UNIQUE",
    "Name": "VARCHAR",
    "Version": "VARCHAR"
}

sql_event_table = {
    "Id": "VARCHAR PRIMARY KEY NOT NULL UNIQUE",
    "Name": "VARCHAR",
    "ActionId": "VARCHAR",
    "ActionType": "INT",
    "TargetId": "VARCHAR"
}

sql_target_table = {
    "Id": "VARCHAR PRIMARY KEY NOT NULL UNIQUE",
    "Name": "VARCHAR",
    "Volume": "REAL DEFAULT 0.0",
    "Pitch": "INT DEFAULT 0",
    "LPF": "INT DEFAULT 0",
    "HPF": "INT DEFAULT 0",
    "UseMaxSoundInstance": "INT DEFAULT 0",
    "MaxSound": "INT DEFAULT 50",
    "UseListenerRelativeRoute": "INT DEFAULT 0",
    "Spatialization3D": "VARCHAR",
    "AttenId": "VARCHAR",
    "SwitchGroupId": "VARCHAR",
    "StateGroupId": "VARCHAR"
}

sql_switch_table = {
    "Id": "VARCHAR PRIMARY KEY NOT NULL UNIQUE",
    "Name": "VARCHAR",
    "SwitchId": "VARCHAR",
    "SwitchName": "VARCHAR"
}

sql_state_table = {
    "Id": "VARCHAR PRIMARY KEY NOT NULL UNIQUE",
    "Name": "VARCHAR",
    "StateId": "VARCHAR",
    "StateName": "VARCHAR"
}

sql_atten_table = {
    "Id": "VARCHAR PRIMARY KEY NOT NULL UNIQUE",
    "Name": "VARCHAR",
    "MaxDistance": "INT",
    "UseCone": "INT"
}

sql_rtpc_table = {
    "Id": "VARCHAR PRIMARY KEY NOT NULL UNIQUE",
    "Name": "VARCHAR",
    "UseBuildInParam": "INT",
    "DefaultValue": "REAL",
    "MaxValue": "REAL",
    "MinValue": "REAL"
}

sql_tables = {
    "Project": sql_project_table,
    "Event": sql_event_table,
    "Target": sql_target_table,
    "Switch": sql_switch_table,
    "State": sql_state_table,
    "Attenuation": sql_atten_table,
    "RTPC": sql_rtpc_table
}