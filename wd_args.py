

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


def get_switchgroup_args(target_id):
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


def get_stategroup_args(switchgroup_id):
    return {
        "from": {
            "id": [switchgroup_id]
        }
    }, {
        "return": ["type"]
    }


def get_children_args(children_id):
    return {
        "from": {
            "id": [children_id]
        },
        "transform": [
            {"select": ["children"]}
        ]
    }, {
        "return": ["id", "name"]
    }


def get_atten_args(atten_id):
    return {
        "from": {
            "id": [atten_id]
        }
    }, {
        "return": ["id", "name", "@@RadiusMax", "@@ConeUse"]
    }