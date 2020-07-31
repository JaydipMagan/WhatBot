from pathlib import Path
import importlib
class help:
    def __init__(self):
        self.help_message = "Help - Display all the available commands"
        self.usage_message = "Try follow : help"
        self.name = "help"
        
    def generate_help_message(self,commands,names):
        message = ["Here are all the commands:",""]
        for name in names:
            obj = commands[name]
            message.append(obj.help_message)
        message+=["@all - send a @ to all the members","For more help with a particular command try command_name -h ","e.g. @Bot meme -h"]
        return message
    
    def parse_args(self,string,commands,names):
        if string=="":
            return {"media":"help","text":self.generate_help_message(commands,names),"media_location":""}
        else:
            return {"media":"error","text":"Incorrect usage. Just try help.","media_location":""}
