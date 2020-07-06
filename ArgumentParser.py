import argparse
class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise SystemExit(message)