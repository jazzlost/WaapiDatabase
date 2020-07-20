

def get_event_args():
    return {
        "from": {
            "ofType": [
                "Event"
            ]
        }
    }


def get_action_args(event_id):
    return {
        "from": {
            "id": [event_id]
        },
        "transform": [
            {"select": ["children"]}
        ]
    }, {
        "return": ["id", "@ActionType", "@Target"]
    }


def get_target_args(target_id):
    return {
        "from": {
            "id": [target_id]
        }
    }, {
        "return": ["@Volume", "@Pitch", "@Lowpass", "@Highpass", "@@ListenerRelativeRouting", 
                    "@@3DSpatialization", "@@EnableAttenuation", "@@Attenuation", "@@UseMaxSoundPerInstance", 
                    "@@MaxSoundPerInstance", "@SwitchGroupOrStateGroup"]
    }


def get_switch_args(target_id):
    return {
        "from": {
            "id": [target_id]
        },
        "transform": [
            {"select": ["descendants"]}
            # {"where": ["type:isIn", "SwitchContainer"]}
        ]
    }, {
        "return": ["type", "@SwitchGroupOrStateGroup"]
    }

def get_state_args(switch_id):
    return {
        "from": {
            "id": [switch_id]
        }
    }, {
        "return": ["type"]
    }
