from .grammar.VerilogParser import VerilogParser

class Item:
    def __init__(self, name, file, start, end):
        """all Items must have name, file, start and end"""
        self.name = None
        # self.type = None
        self.file = None
        self.start = None
        self.end = None

class Module(Item):
    def __init__(self, ctx: VerilogParser.Module_declarationContext):

        super.__init__()


class Defines(Item):
    pass

