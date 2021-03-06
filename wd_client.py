##################################### WAMP Client #######################################################
import time
from waapi import EventHandler, connect
from wd_args import *
from wd_processor import *
from wd_parser import *

class client(object):

    def __init__(self, url=None):
        # Connect url default is 127.0.0.1:8080
        self.url = url
        # WAMP client
        self.client = connect(url)
        # All datas of project properties
        self.project_datas = []
        # All datas of events properties
        self.event_datas = []
        # All datas of event related target(containers or audio sources) properties
        self.target_datas = []
        # All datas of switches' porperties
        self.switch_datas = []
        # All datas of states' porperties
        self.state_datas = []
        # All datas of attenuations' properties
        self.atten_datas = []
        # All datas of RTPCs' properties
        self.rtpc_datas = []
        # Datas list object to hold all datas
        self.datas = [self.project_datas, self.event_datas, self.target_datas, self.switch_datas, self.state_datas, self.atten_datas, self.rtpc_datas]

    def __del__(self):
        self.disconnect()

    ##################################### WAMP connection #######################################################
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


    ################################### Waapi data catcher #########################################################
    def catch_datas(self, project_root):

        ################################### Catch project data  #########################################################
        kwargs = get_project_args()
        wwise_info = self.client.call("ak.wwise.core.getInfo")
        project_info = self.client.call("ak.wwise.core.object.get", **kwargs)
        process_project(wwise_info, project_info, self.project_datas)

        #################################### Catch all events' data ##########################################################
        events = self.client.call("ak.wwise.core.object.get", get_event_args())
        process_event(events, self.event_datas)
        
        # If multiple events ref same target, we only record one to catch target datas
        target_id = set()

        #################################### Catch event's action ##########################################################
        for data in self.event_datas:
            kwargs, option = get_action_args(data.get("Id"))
            actions = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
            if len(actions["return"]) > 0:
                process_action(actions, data)
                for t in data.get("Target"):
                    if t is not None:
                        target_id.add(t.get("id"))
            process_none(data, "event_datas")

        #################################### Catch event related target(containers or audio sources) datas ##########################################################
        for id in target_id:
            kwargs, option = get_target_args(id)
            targets = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
            if targets is not None:
                process_target(targets, self.target_datas)

        # Waapi do not support to get rtpc ref, we get it from .wwu
        fill_rtpc_ids(project_root, target_id, self.target_datas)
        ##################################### Catch event related switch and state group datas #########################################################
        for data in self.target_datas:
            kwargs, option = get_switchgroup_args(data.get("Id"))
            switchgroups = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
            if switchgroups is not None:
                process_switchgroup(switchgroups, data)
            ##################################### Catch switch group related switch state datas #########################################################
            if "SwitchGroup" in data:
                for switchgroup in data.get("SwitchGroup"):
                    if switchgroup is not None:
                        kwargs, option = get_children_args(switchgroup.get("id"))
                        switches = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
                        if switches is not None:
                            process_switch(switchgroup, switches, self.switch_datas)
            
                    ##################################### Get state gourp from switch group datas #########################################################
                        kwargs, option = get_stategroup_args(switchgroup.get("id"))
                        stategroups = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
                        if stategroups is not None:
                            process_stategroup(switchgroup, stategroups, data, self.switch_datas)

            ##################################### Catch state group related state datas #########################################################
            if "StateGroup" in data:
                for stategroup in data.get("StateGroup"):
                    kwargs, option = get_children_args(stategroup.get("id"))
                    states = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
                    if states is not None:
                        process_state(stategroup, states, self.state_datas)

            ##################################### Catch attenuation datas #########################################################
            if "Attenuation" in data:
                atten = data.get("Attenuation")
                if atten is not None:
                    kwargs, option = get_atten_args(atten.get("id"))
                    attens = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
                    if attens is not None:
                        process_atten(attens, self.atten_datas)

        ##################################### Catch RTPC datas #########################################################
        rtpc_kwagrs, rtpc_option = get_rtpc_args()
        rtpcs = self.client.call("ak.wwise.core.object.get", **rtpc_kwagrs, options=rtpc_option)
        process_rtpc(rtpcs, self.rtpc_datas)

        ##################################### Fill no data properties with None #########################################################
        for data in self.target_datas:
            process_none(data, "target_datas")

        ##############################################################################################
        print("Finished data catching")






