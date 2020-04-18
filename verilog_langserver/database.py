
class Database:
    def __init__(self):
        self._files = {}

    def update_file(self, uri, items):
        self._files.update({uri : items})

    @property
    def declarations(self):
        declarations = {}
        for f in self._files:
            for dec in f.declarations:
                declarations.update(dec)
        return declarations

    @property
    def symbols(self):
        symbols = []
        for _, items in self._files:
            symbols += items

    @property
    def macros(self):
        pass


