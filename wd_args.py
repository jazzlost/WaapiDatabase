##################################### Waapi Call Arguments #######################################################
from wd_config import *


# Project call args
def get_project_args():
    return {
        "from": {
            "ofType": [
                "Project"
            ]
        }
    }


# Event call args
def get_event_args():
    return {
        "from": {
            "ofType": [
                "Event"
            ]
        }
    }


# Action call args
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


# Target call args
def get_target_args(target_id):
    ret_list = []
    # None list properties
    for value in target_config.values():
        ret_list.append(value)
    # List properties
    for value in target_list_config.values():
        ret_list.append(value)

    return {
        "from": {
            "id": [target_id]
        }
    }, {
        "return": ret_list
    }


# Switch group call args
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


# State group call args
def get_stategroup_args(switchgroup_id):
    return {
        "from": {
            "id": [switchgroup_id]
        }
    }, {
        "return": ["type"]
    }


# Attenuation args
def get_atten_args(atten_id):
    return {
        "from": {
            "id": [atten_id]
        }
    }, {
        "return": ["id", "name", "@@RadiusMax", "@@ConeUse"]
    }


# RTPC call args
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


# Get children objects' id & name args
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