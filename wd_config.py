
################################Waapi Config############################################

event_config = {
   "Id": "id",
   "Name": "name"
}

action_config = {
    "ActionId": "id",
    "ActionType": "@ActionType",
    "Target": "@Target"
}

target_config = {
    "Id": "id",
    "Name": "name",
    "Volume": "@Volume",
    "Pitch": "@Pitch",
    "LPF": "@Lowpass",
    "HPF": "@Highpass",
    "UseMaxSoundInstance": "@@UseMaxSoundPerInstance",
    "MaxSound": "@@UseMaxSoundPerInstance"
}

target_condition_config = {
    "@@ListenerRelativeRouting": [
        {"UseListenerRelativeRoute": "@@ListenerRelativeRouting"},
        {"Spatialization3D": "@@3DSpatialization"}
    ],
    "@@EnableAttenuation": [
        {"TargetAttenuation": "@@Attenuation"}
    ]
}

target_validation_config = {
    "SwitchOrStateGroup": "@SwitchGroupOrStateGroup"
}

switchgroup_config = {
    "TargetSwitchGroup": "@SwitchGroupOrStateGroup"
}

stategroup_config = {
    "TargetStateGroup": "StateGroup"
}

atten_config = {
    "Id": "id",
    "Name": "name",
    "MaxDistance": "@@RadiusMax",
    "UseCone": "@@ConeUse"
}

################################SQLite Config############################################

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
    "SwitchOrStateGroupId": "VARCHAR"
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

sql_tables = {
    "Event": sql_event_table,
    "Target": sql_target_table,
    "Switch": sql_switch_table,
    "State": sql_state_table,
    "Attenuation": sql_atten_table
}