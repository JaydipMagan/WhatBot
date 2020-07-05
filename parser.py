import os,sys
from pathlib import Path
import importlib
class parser:

    def __init__(self):
        sys.path.append('commands')
        self.vaild_command_names = self.get_valid_command_names()
        self.commands = self.get_commands()

    def get_commands(self):
        commands = {}
        for x in self.vaild_command_names:
            obj = self.get_class("commands",x)
            commands[x] = obj
        return commands

    def get_class(self,module,file):
        m = __import__(module+"."+file)
        m = getattr(m, file)            
        m = getattr(m, file)            
        return m

    def get_valid_command_names(self):
        commands = []
        path = Path(r"commands")
        files_in_path = path.iterdir()
        for item in files_in_path:
            if item.is_file() and item.name[-2:]=="py" and item.name!="__init__.py":
                commands.append(item.name[:-3])
        return commands

    def parse(self,string):
        args = string.split()
        if args[0] not in self.vaild_command_names:
            raise SyntaxError(args[0]+" is not a valid command. Use help to find out the valid commands.")
        else:
            obj = self.commands[args[0]]
