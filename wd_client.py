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
        self.rtpc_datas = []

        self.datas = [self.event_datas, self.target_datas, self.switch_datas, self.state_datas, self.atten_datas, self.rtpc_datas]

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
    # def handle_project(self):
        
    #     myArgs = {
    #         "from": {
    #             "ofType": [
    #                 "Project"
    #             ]
    #         }
    #     }

    #     wwise_info = self.client.call("ak.wwise.core.getInfo")
    #     project_info = self.client.call("ak.wwise.core.object.get", **myArgs)
        # self.data.add_project_data(wwise_info)
        # self.data.add_project_data(project_info)
        # self.data.get_project_data()

    def handle_event(self):

        events = self.client.call("ak.wwise.core.object.get", get_event_args())
        process_event(events, self.event_datas)
        ##############################################################################################
        
        target_id = set()

        for data in self.event_datas:
            kwargs, option = get_action_args(data.get("Id"))
            actions = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
            if len(actions["return"]) > 0:
                process_action(actions, data)
                for t in data.get("Target"):
                    target_id.add(t.get("id"))
            process_none(data, "event_datas")

        for id in target_id:
            kwargs, option = get_target_args(id)
            targets = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
            if targets is not None:
                process_target(targets, self.target_datas)

        ##############################################################################################

        for data in self.target_datas:
            kwargs, option = get_switchgroup_args(data.get("Id"))
            switchgroups = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
            if switchgroups is not None:
                process_switchgroup(switchgroups, data)

            if "SwitchGroup" in data:
                for switchgroup in data.get("SwitchGroup"):
                    kwargs, option = get_children_args(switchgroup.get("id"))
                    switches = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
                    if switches is not None:
                        process_switch(switchgroup, switches, self.switch_datas)
            
                    kwargs, option = get_stategroup_args(switchgroup.get("id"))
                    stategroups = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
                    if stategroups is not None:
                        process_stategroup(switchgroup, stategroups, data, self.switch_datas)

            
            if "StateGroup" in data:
                for stategroup in data.get("StateGroup"):
                    kwargs, option = get_children_args(stategroup.get("id"))
                    states = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
                    if states is not None:
                        process_state(stategroup, states, self.state_datas)

            if "Attenuation" in data:
                atten = data.get("Attenuation")
                if atten is not None:
                    kwargs, option = get_atten_args(atten.get("id"))
                    attens = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
                    if attens is not None:
                        process_atten(attens, self.atten_datas)

        rtpc_kwagrs, rtpc_option = get_rtpc_args()
        rtpcs = self.client.call("ak.wwise.core.object.get", **rtpc_kwagrs, options=rtpc_option)
        process_rtpc(rtpcs, self.rtpc_datas)

        for data in self.target_datas:
            process_none(data, "target_datas")


        print("pause")
        ##############################################################################################






