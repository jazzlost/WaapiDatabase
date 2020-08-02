##################################### Save Waapi Catched Datas Into Datas Object #######################################################
from wd_config import *

# Project data processing
def process_project(wwise_info, project_info, datas):
    data = {}
    version = wwise_info.get("version").get("displayName")
    data["Version"] = version
    for p in project_info.get("return"):
        data["Id"] = p.get("id")
        data["Name"] = p.get("name")
    datas.append(data)


# Event data processing
def process_event(events, datas):
    for event in events.get("return"):
        data = {}
        for key, value in event_config.items():
            data.setdefault(key, event.get(value))
        datas.append(data)


# Action data processing
def process_action(actions, data):
    for action in actions.get("return"):
        for key, value in action_config.items():
            data.setdefault(key, []).append(action.get(value))


# Target data processing
def process_target(targets, datas):
    for target in targets.get("return"):
        data = {}
        # Dict object data
        for key, value in target_config.items():
            data.setdefault(key, target.get(value))
        # List object data
        for key, value in target_list_config.items():
            if target.get(value) is not None:
                data.setdefault(key, []).append(target.get(value))

        datas.append(data)


# Switch group data processing
def process_switchgroup(switches, data):
    for switch in switches.get("return"):
        for key, value in switchgroup_config.items():
            if(switch.get(value) is not None):
                data.setdefault(key, []).append(switch.get(value))
            if "SwitchOrStateGroup" in data:
                for value in data["SwitchOrStateGroup"]:
                    data.setdefault(key, []).append(value)
                del data["SwitchOrStateGroup"]


# State group data processing
def process_stategroup(switchgroup, statesgroup, data, switch_datas):
    for state in statesgroup.get("return"):
        for key, value in stategroup_config.items():    
            if state.get("type") == value:
                data["SwitchGroup"].remove(switchgroup)
                data.setdefault(key, []).append(switchgroup)
                for data in switch_datas:
                    if switchgroup["id"] == data["Id"]:
                        switch_datas.remove(data)


# Switches data processing
def process_switch(switchgroup, switches, switch_datas):
    data = {"Id": switchgroup["id"], "Name": switchgroup["name"], "SwitchState": []}
    for switch in switches.get("return"):
        data["SwitchState"].append(switch)

    switch_datas.append(data)


# States data processing
def process_state(stategroup, states, state_datas):
    data = {"Id": stategroup["id"], "Name": stategroup["name"], "State": []}
    for state in states.get("return"):
        data["State"].append(state)

    state_datas.append(data)


# Attenuation data processing
def process_atten(attens, atten_datas):
    data = {}
    for atten in attens.get("return"):
        for key, value in atten_config.items():
            data.setdefault(key, atten.get(value))

        atten_datas.append(data)


# RTPC data processing
def process_rtpc(rtpcs, rtpc_datas):
    for rtpc in rtpcs.get("return"):
        data = {}
        for key, value in rtpc_config.items():
            data.setdefault(key, rtpc.get(value))
        rtpc_datas.append(data)


# Process no properties' data as None
def process_none(data, datas_name):
    if len(datas_name) == 0:
        return

    # Event Datas
    if datas_name == "event_datas":
        props = list(event_config.keys())
        props += list(action_config.keys())
        for key in props:
            if key not in data:
                data[key] = None
    # Target_datas
    elif datas_name == "target_datas":
        props = list(target_config.keys())
        for key in props:
            if key not in data:
                data[key] = None

        if "SwitchGroup" not in data:
            data["SwitchGroup"] = None
        elif len(data["SwitchGroup"]) == 0:
            data["SwitchGroup"] = None

        if "StateGroup" not in data:
            data["StateGroup"] = None
        elif len(data["StateGroup"]) == 0:
            data["StateGroup"] = None
