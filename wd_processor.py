

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
            data.setdefault("TargetAttenId", target.get("@@Attenuation").get("id"))
            data.setdefault("TargetAttenName", target.get("@@Attenuation").get("name"))
        if(target.get("@SwitchGroupOrStateGroup") is not None):
            data.setdefault("TargetSwitchGroup", []).append(target.get("@SwitchGroupOrStateGroup"))

def process_switch(switches, data):
    for switch in switches.get("return"):
        if(switch.get("@SwitchGroupOrStateGroup") is not None):
            data.setdefault("TargetSwitchGroup", []).append(switch.get("@SwitchGroupOrStateGroup"))