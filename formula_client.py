import time
from waapi import EventHandler, connect
from formula_data import formula_data as fdata
from formula_config import formula_properties_dict as fpdict
from formula_config import formula_expression as my_expression

from wd_args import *
from wd_processor import *

class formula_client(object):


    def __init__(self, url=None):
        self.url = url
        self.client = connect(url)
        self.data = fdata()
        self.res_obj = False
        self.exp = lambda x: x
        self.fplist = []
        for name in fpdict.keys():
            self.fplist.append(name)
        self.datas = []
        self.switch_datas = []

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
        self.data.add_project_data(wwise_info)
        self.data.add_project_data(project_info)
        self.data.get_project_data()

    def handle_event(self):

        events = self.client.call("ak.wwise.core.object.get", get_event_args())
        process_event(events, self.datas)
        ##############################################################################################

        for data in self.datas:
            kwargs, option = get_action_args(data.get("EventId"))
            actions = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
            process_action(actions, data)
        
        ##############################################################################################
        
        for data in self.datas:
            kwargs, option = get_target_args(data.get("TargetId"))
            targets = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
            process_target(targets, data)

        ##############################################################################################

        for data in self.datas:
            kwargs, option = get_switchgroup_args(data.get("TargetId"))
            switchgroups = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
            if switchgroups is not None:
                process_switchgroup(switchgroups, data)

        ##############################################################################################
        
        for data in self.datas:
            if "TargetSwitchGroup" in data:
                for switchgroup in data.get("TargetSwitchGroup"):
                    kwargs, option = get_stategroup_args(switchgroup.get("id"))
                    stategroups = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
                    if stategroups is not None:
                        process_stategroup(switchgroup, stategroups, data)
                if len(data["TargetSwitchGroup"]) == 0:
                    del data["TargetSwitchGroup"]
        
        for data in self.datas:
            if "TargetSwitchGroup" in data:
                for switchgroup in data.get("TargetSwitchGroup"):
                    kwargs, option = get_switch_args(switchgroup.get("id"))
                    switches = self.client.call("ak.wwise.core.object.get", **kwargs, options=option)
                    if switches is not None:
                        process_switch(switchgroup, switches, self.switch_datas)


        print("pause")
        ##############################################################################################

    def handle_property(self):
        print("Please select property to formula:")
        for i, p in enumerate(self.fplist):
            print(i+1,".", p)
        print("\n")

        selection = input("Please input the property index: ")
        if(selection.isdigit()):
            if(int(selection) < len(self.fplist)+1):
                self.selected_property = fpdict[self.fplist[int(selection)-1]]
                print("Your selection is: %s" % self.fplist[int(selection)-1])


    def handle_object(self):

        def sel_changed(**kwargs):
            self.data.add_object_data(kwargs)
            self.res_obj = self.data.get_object_data(self.selected_property)

        print("Please select objects in Wwise: \n")
        kwargs = self.data.get_object_args(self.selected_property)
        self.object_event = self.client.subscribe("ak.wwise.ui.selectionChanged", sel_changed, **kwargs)

    
    def end_handle_object(self):
        self.client.unsubscribe(self.object_event)


    ############################################################################################

    def _set_property(self, property, id, value):

        myArgs = {
            "property": property,
            "object": id,
            "value": value
        }
        self.client.call("ak.wwise.core.object.setProperty", **myArgs)

    def _get_property(self, property, id):
        
        myArgs = {
            "property": property,
            "object": id,
        }
        
        response = self.client.call("ak.wwise.core.object.getPropertyInfo", **myArgs)
        self.data.add_property_data(response)
        self.data.get_property_data()

    def set_properties(self):
        for i, id in enumerate(self.data.object_Ids):
            self._set_property(self.selected_property.replace("@", ""), id, my_expression(self.data.object_values[i]))

