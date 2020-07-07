from pathlib import Path
import importlib
class help:
    def __init__(self):
        self.help_message = "help - Display all the available commands"
        self.usage_message = "Incorrect usage. Try follow : help"
        self.name = "help"
        
    def generate_help_message(self,commands,names):
        message = ""
        for name in names:
            obj = commands[name]
            message += obj.help_message+"\n"
        return message
    def parse_args(self,string,commands,names):
        if string=="":
            return self.generate_help_message(commands,names)
        else:
            return ("error","Incorrect usage. Just try help.")
