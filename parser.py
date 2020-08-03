import os,sys
from pathlib import Path
import importlib
class parser:

    def __init__(self):
        sys.path.append('commands')
        self.vaild_command_names,self.valid_commands,self.help_message = self.get_commands()
        
    def get_class(self,module,file):
        m = __import__(module+"."+file)
        m = getattr(m, file)            
        m = getattr(m, file)            
        return m

    def get_commands(self):
        command_names = []
        command_objs = {}
        message = ["Here are all the commands:",""]
        path = Path(r"commands")
        files_in_path = path.iterdir()
        for item in files_in_path:
            if item.is_file() and item.name[-2:]=="py" and item.name!="__init__.py":
                command_name = item.name[:-3]
                command_names.append(command_name)
                command_objs[command_name] = self.get_class("commands",command_name)()
                message.append(command_objs[command_name].help_message)
        message+=["@all - send a @ to all the members","For more help with a particular command try command_name -h ","e.g. @Bot meme -h"]
        return command_names,command_objs,message

    def parse(self,string):
        args = string.split()
        if args[0] not in self.vaild_command_names:
            return {"media":"error","text":args[0]+" is not a valid command. Use help to find out the valid commands.","media_location":""}
        else:
            obj = self.valid_commands [args[0]]
            cmd = " ".join(args[1:])
            if args[0]=="help":
                return {"media":"help","text":self.help_message,"media_location":""}
            return obj.parse_args(cmd)