from wd_config import *


def process_event(events, datas):
    for event in events.get("return"):
        data = {}
        for key, value in event_config.items():
            data.setdefault(key, event.get(value))
        datas.append(data)


def process_action(actions, data):
    for action in actions.get("return"):
        for key, value in action_config.items():
            data.setdefault(key, action.get(value))


def process_target(targets, datas):
    for target in targets.get("return"):
        data = {}
        for key, value in target_config.items():
            data.setdefault(key, target.get(value))
        
        for condition_key, condition_value in target_condition_config.items():
            if(target.get(condition_key) is not False):
                for pair in condition_value:
                    for key, value in pair.items():
                        data.setdefault(key, target.get(value))
        
        for validation_key, validation_value in target_validation_config.items():
            if target.get(validation_value) is not None:
                data.setdefault(validation_key, []).append(target.get(validation_value))

        datas.append(data)


def process_switchgroup(switches, data):
    for switch in switches.get("return"):
        for key, value in switchgroup_config.items():
            if(switch.get(value) is not None):
                data.setdefault(key, []).append(switch.get(value))
            if "SwitchOrStateGroup" in data:
                for value in data["SwitchOrStateGroup"]:
                    data.setdefault(key, []).append(value)
                del data["SwitchOrStateGroup"]


def process_stategroup(switchgroup, statesgroup, data):
    for state in statesgroup.get("return"):
        for key, value in stategroup_config.items():    
            if state.get("type") == value:
                data["TargetSwitchGroup"].remove(switchgroup)
                data.setdefault(key, []).append(switchgroup)


def process_switch(switchgroup, switches, switch_datas):
    data = {"SwitchGroup": switchgroup, "SwitchState": []}
    for switch in switches.get("return"):
        data["SwitchState"].append(switch)

    switch_datas.append(data)


def process_state(stategroup, states, state_datas):
    data = {"StateGroup": stategroup, "State": []}
    for state in states.get("return"):
        data["State"].append(state)

    state_datas.append(data)


def process_atten(attens, atten_datas):
    data = {}
    for atten in attens.get("return"):
        for key, value in atten_config.items():
            data.setdefault(key, atten.get(value))

        atten_datas.append(data)
