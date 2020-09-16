import xml.sax
import os
from wd_config import container_tags, wwu_root


class WwuParserHandler(xml.sax.ContentHandler):
    def __init__(self, targetIds, target_datas):
        self.Ids = targetIds
        self.datas = target_datas
        self.container = []
        self.current_id = []
        self.into_container = False
        self.into_rtpc = False
        self.into_object_ref = False

    def startElement(self, tag, attributes):
        if self.into_container is True:
            if self.into_rtpc is True:
                if tag == "ObjectRef":
                    for data in self.datas:
                        if data["Id"] == self.current_id[-1]:
                            data["RtpcId"].append(attributes["ID"])
            else:
                if tag == "RTPC":
                    self.into_rtpc = True
        else:
            if tag in container_tags:
                if attributes["ID"] in self.Ids:
                    self.container.append(tag)
                    self.current_id.append(attributes["ID"])
                    self.into_container = True

    def endElement(self, tag):
        if self.into_container is True:
            if tag == self.container[-1]:
                self.into_container = False
                self.current_id.pop()
                self.container.pop()

            elif tag == "RTPC":
                if self.into_rtpc is True:
                    self.into_rtpc = False

    def characters(self, content):
        pass


def fill_rtpc_ids(project_root, targetIds, target_datas):
    # Create XML Parser
    parser = xml.sax.make_parser()
    # Set Parser Handler
    Handler = WwuParserHandler(targetIds, target_datas)
    parser.setContentHandler(Handler)
    # Start To Parse
    wwus = GetWwuFiles(project_root)
    try:
        for wwu in wwus:
            parser.parse(wwu)
    except TypeError:
        print("WaapiDatabase:Error:No Valid Wwu File Exist!")
    


def GetWwuFiles(project_root):
    wwu_full_path = project_root + wwu_root
    try:
        list = os.listdir(wwu_full_path)
    except FileNotFoundError:
        print("WaapiDatabase:Error:Wwu File Path Is Invalid!")
    else:
        wwus = []
        for name in list:
            file = wwu_full_path + str(name)
            wwus.append(file)
        return wwus