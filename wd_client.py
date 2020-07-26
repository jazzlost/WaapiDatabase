import time
from waapi import EventHandler, connect

from wd_args import *
from wd_processor import *

class client(object):


    def __init__(self, url=None):
        self.url = url
        self.client = connect(url)
        self.event_datas = []
        self.target_datas = []
        self.switch_datas = []
        self.state_datas = []
        self.atten_datas = []

        self.datas = [self.event_datas, self.target_datas, self.switch_datas, self.state_datas, self.atten_datas]

    def __del__(self):
        self.disconnect()
    
    ############################################################################################
    def connect(self):
        while not self.client:
            print("Cannot connect, retrying in 1 second...")
            time.sleep(1)
            self.client = connect(self.url)

        while not self.client.is_connected():
            time.sleep(1)
            self.client.__connect()

    def disconnect(self):
        while self.client and self.client.is_connected():
            self.client.disconnect()
            print("Disconnected!")


    ############################################################################################
    def handle_project(self):
        
        myArgs = {
            "from": {
                "ofType": [
                    "Project"
                ]
            }
        }

        wwise_info = self.client.call("ak.wwise.core.getInfo")
        project_info = self.client.call("ak.wwise.core.object.get", **myArgs)
        # self.data.add_project_data(wwise_info)
        # self.data.add_project_data(project_info)
        # self.data.get_project_data()

    def handle_event(self):

        events = self.client.call("ak.wwise.core.object.get", get_event_args())
        process_event(events, self.event_datas)
        ##############################################################################################

        for data in self.event_datas:
            kwargs, option = get_action_args(data.get("Id"))
            actions = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
            process_action(actions, data)
        
        ##############################################################################################
        
        for data in self.event_datas:
            kwargs, option = get_target_args(data.get("Target").get("id"))
            targets = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
            process_target(targets, self.target_datas)

        ##############################################################################################

        for data in self.target_datas:
            kwargs, option = get_switchgroup_args(data.get("Id"))
            switchgroups = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
            if switchgroups is not None:
                process_switchgroup(switchgroups, data)

        ##############################################################################################
        
        for data in self.target_datas:
            if "TargetSwitchGroup" in data:
                for switchgroup in data.get("TargetSwitchGroup"):
                    kwargs, option = get_stategroup_args(switchgroup.get("id"))
                    stategroups = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
                    if stategroups is not None:
                        process_stategroup(switchgroup, stategroups, data)
                if len(data["TargetSwitchGroup"]) == 0:
                    del data["TargetSwitchGroup"]

        ##############################################################################################

        for data in self.target_datas:
            if "TargetSwitchGroup" in data:
                for switchgroup in data.get("TargetSwitchGroup"):
                    kwargs, option = get_children_args(switchgroup.get("id"))
                    switches = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
                    if switches is not None:
                        process_switch(switchgroup, switches, self.switch_datas)
            elif "TargetStateGroup" in data:
                for stategroup in data.get("TargetStateGroup"):
                    kwargs, option = get_children_args(stategroup.get("id"))
                    states = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
                    if states is not None:
                        process_state(stategroup, states, self.state_datas)

        ##############################################################################################
        for data in self.target_datas:
            if "TargetAttenuation" in data:
                atten = data.get("TargetAttenuation")
                kwargs, option = get_atten_args(atten.get("id"))
                attens = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
                if attens is not None:
                    process_atten(attens, self.atten_datas)



        print("pause")
        ##############################################################################################






