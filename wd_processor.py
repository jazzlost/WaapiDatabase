

def process_event(events, datas):
    for event in events.get("return"):
        data = {}
        data.setdefault("EventId", event.get("id"))
        data.setdefault("EventName", event.get('name'))
        datas.append(data)


def process_action(actions, data):
    for action in actions.get("return"):
        data.setdefault("ActionId", action.get("id"))
        data.setdefault("ActionType", action.get("@ActionType"))
        data.setdefault("TargetId", action.get("@Target").get("id"))
        data.setdefault("TargetName", action.get("@Target").get("name"))


def process_target(targets, data):
    for target in targets.get("return"):
        data.setdefault("TargetsVolume", target.get("@Volume"))
        data.setdefault("TargetsPitch", target.get("@Pitch"))
        data.setdefault("TargetLPF", target.get("@Lowpass"))
        data.setdefault("TargetHPF", target.get("@Highpass"))
        data.setdefault("TargetUseMaxSoundInstance", target.get("@@UseMaxSoundPerInstance"))
        data.setdefault("TargetMaxSound", target.get("@@UseMaxSoundPerInstance"))
        if(target.get("@@ListenerRelativeRouting") is not False):
            data.setdefault("TargetUseRelativeRouting", target.get("@@ListenerRelativeRouting"))
            data.setdefault("Target3DSpatialization", target.get("@@3DSpatialization"))
        if(target.get("@@EnableAttenuation") is not False):
            data.setdefault("TargetAttenuation", target.get("@@Attenuation"))
        if(target.get("@SwitchGroupOrStateGroup") is not None):
            data.setdefault("TargetSwitchGroup", []).append(target.get("@SwitchGroupOrStateGroup"))


def process_switchgroup(switches, data):
    for switch in switches.get("return"):
        if(switch.get("@SwitchGroupOrStateGroup") is not None):
            data.setdefault("TargetSwitchGroup", []).append(switch.get("@SwitchGroupOrStateGroup"))


def process_stategroup(switchgroup, statesgroup, data):
    for state in statesgroup.get("return"):
        if state.get("type") == "StateGroup":
            data["TargetSwitchGroup"].remove(switchgroup)
            data.setdefault("TargetStateGroup", []).append(switchgroup)


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
        data.setdefault("id", atten.get("id"))
        data.setdefault("name", atten.get("name"))
        data.setdefault("MaxDistance", atten.get("@@RadiusMax"))
        data.setdefault("UseCone", atten.get("@@ConeUse"))

    atten_datas.append(data)