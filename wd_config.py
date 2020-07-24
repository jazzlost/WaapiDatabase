
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
    "EventId": "TEXT",
    "EventName": "TEXT",
    "ActionId": "TEXT",
    "ActionType": "TEXT",
    "TargetId": "TEXT"
}

spl_target_table = {
    "TargetId": "TEXT",
    "TargetsVolume": "REAL",
    "TargetPitch": "INTEGER",
    "TargetLPF": "INTEGER",
    "TargetHPF": "INTEGER",
    "TargetUseMaxSoundInstance": "INTEGER",
    "TargetMaxSound": "INTEGER",
    "TargetListenerRelativeRoute": "INTEGER",
    "Target3DSpatialization": "TEXT",
    "TargetAttenId": "TEXT",
    "TargetSwitchOrStateGroup": "TEXT"
}

sql_switch_table = {
    "SwitchGroupId": "TEXT",
    "Switch": "TEXT"
}

sql_state_table = {
    "StateGroupId": "TEXT",
    "State": "TEXT"
}

sql_atten_table = {
    "AttenId": "TEXT",
    "AttenName": "TEXT",
    "MaxDistance": "INTEGER",
    "UseCone": "INTEGER"
}

sql_tables = [
    sql_event_table,
    spl_target_table,
    sql_switch_table,
    sql_state_table,
    sql_atten_table
]

