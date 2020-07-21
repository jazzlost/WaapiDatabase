
################################Config############################################

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
    "TargetsVolume": "@Volume",
    "TargetsPitch": "@Pitch",
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