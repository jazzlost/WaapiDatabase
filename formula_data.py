from waapi_data import waapi_data


class formula_data(waapi_data):

    def __init__(self):
        self.project_data = []

    def get_object_args(self, property):
        return {
            "return": [
                "id",
                "name",
                "type",
                "@Attenuation",
                property
            ]
        }

    def get_project_data(self):
        version = self.project_data[0][0]["version"]["displayName"]
        name = self.project_data[1][0]["return"][0]["name"]
        print(version + " " + name + "\n")

    def get_object_data(self, selected_property):
        self.objects = self.object_data[0]["objects"]
        self.object_Ids = [object["id"] for object in self.objects]
        self.object_names = [object["name"] for object in self.objects]
        self.object_values = [object[selected_property] for object in self.objects if selected_property in object.keys()]
        if len(self.object_values) != len(self.object_Ids):
            print("Invalid selection, please select again: \n")
            return False

        for name in self.object_names:
            print(name)

        print("\n")
        res = input()
        if(res.upper() == 'Y'):
            return True
        else:
            return False
