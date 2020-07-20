from pprint import pprint

class waapi_data(object):

    def __init__(self):
        self.project_data = []

    def get_object_args(self):
        return {}

    def add_project_data(self, *args):
        self.project_data.append(args)

    def get_project_data(self):
        pass

    def add_object_data(self, *args):
        self.object_data = ()
        self.object_data = args

    def get_object_data(self):
        pass

    def add_property_data(self, *args):
        self.property_data = args
    
    def get_property_data(self):
        pass

