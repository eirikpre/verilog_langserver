
class Database:
    def __init__(self):
        self._files = {}

    def update_file(self, filename, items):
        self._files.update({filename : items})

    @property
    def declarations(self):
        declarations = {}
        for f in self._files:
            for dec in f.declarations:
                declarations.update(dec)
        return declarations

    @property
    def macros(self):
        pass


