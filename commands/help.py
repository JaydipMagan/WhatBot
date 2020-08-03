from pathlib import Path
import importlib
class help:
    def __init__(self):
        self.help_message = "Help - Display all the available commands"
        self.usage_message = "Try follow : help"
        self.name = "help"
    
    def parse_args(self,string,commands,names):
        if string=="":
            return {"media":"help","text":self.help_message,"media_location":""}
        else:
            return {"media":"error","text":"Incorrect usage. Just try help.","media_location":""}
