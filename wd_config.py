
################################Waapi Config############################################

event_config = {
   "EventId": "id",
   "EventName": "name"
}

action_config = {
    "ActionId": "id",
    "ActionType": "@ActionType",
    "Target": "@Target"
}

target_config = {
    "TargetVolume": "@Volume",
    "TargetPitch": "@Pitch",
    "TargetLPF": "@Lowpass",
    "TargetHPF": "@Highpass",
    "TargetUseMaxSoundInstance": "@@UseMaxSoundPerInstance",
    "TargetMaxSound": "@@UseMaxSoundPerInstance"
}

target_condition_config = {
    "@@ListenerRelativeRouting": [
        {"TargetUseRelativeRouting": "@@ListenerRelativeRouting"},
        {"Target3DSpatialization": "@@3DSpatialization"}
    ],
    "@@EnableAttenuation": [
        {"TargetAttenuation": "@@Attenuation"}
    ]
}

target_validation_config = {
    "TargetSwitchGroup": "@SwitchGroupOrStateGroup"
}

switchgroup_config = {
    "TargetSwitchGroup": "@SwitchGroupOrStateGroup"
}

stategroup_config = {
    "TargetStateGroup": "StateGroup"
}

atten_config = {
    "id": "id",
    "name": "name",
    "MaxDistance": "@@RadiusMax",
    "UseCone": "@@ConeUse"
}

################################SQLite Config############################################

sql_event_table = {
    "Id": "VARCHAR PRIMARY KEY NOT NULL UNIQUE",
    "Name": "VARCHAR",
    "ActionId": "VARCHAR",
    "ActionType": "VARCHAR",
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
    "SwitchOrStateGroup": "VARCHAR"
}

sql_switch_table = {
    "Id": "VARCHAR PRIMARY KEY NOT NULL UNIQUE",
    "Name": "VARCHAR",
    "Switch": "VARCHAR"
}

sql_state_table = {
    "Id": "VARCHAR PRIMARY KEY NOT NULL UNIQUE",
    "Name": "VARCHAR",
    "State": "VARCHAR"
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