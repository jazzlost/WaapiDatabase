from wd_config import *

def get_project_args():
    return {
        "from": {
            "ofType": [
                "Project"
            ]
        }
    }
def get_event_args():
    return {
        "from": {
            "ofType": [
                "Event"
            ]
        }
    }


def get_action_args(event_id):
    ret_list = []
    for value in action_config.values():
        ret_list.append(value)

    return {
        "from": {
            "id": [event_id]
        },
        "transform": [
            {"select": ["children"]}
        ]
    }, {
        "return": ret_list
    }


def get_target_args(target_id):
    ret_list = []
    for value in target_config.values():
        ret_list.append(value)

    # for key, value in target_condition_config.items():
    #     ret_list.append(key)
    #     for obj in value:
    #         for list_key, list_value in obj.items():
    #             ret_list.append(list_value)

    for value in target_list_config.values():
        ret_list.append(value)

    return {
        "from": {
            "id": [target_id]
        }
    }, {
        "return": ret_list
    }


def get_switchgroup_args(target_id):
    return {
        "from": {
            "id": [target_id]
        },
        "transform": [
            {"select": ["descendants"]}
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


def get_rtpc_args():
    return {
        "from": {
            "ofType": [
                "GameParameter"
                ]
            }
    }, {
        "return": ["id", "name", "@BindToBuiltInParam", "@InitialValue", "@Max", "@Min"]
    }