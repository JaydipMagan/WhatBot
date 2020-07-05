import importlib
class help:
    def __init__(self):
        pass

    def generate_help_message(self,commands):
        message = ""
        for c in commands:
            command = c()
            message+=command.help()+"\n"
        return message

    def help(self):
        return self.help_message