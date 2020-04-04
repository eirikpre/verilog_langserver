from .utils import Position


class Database:
    def __init__(self):
        self._files = {}

    def update_file(self, filename, objects):
        pass

    @property
    def declarations(self):
        declarations = {}
        for f in self._files:
            for o in f.declarations:
                declarations.update(o)
        return declarations

    @property
    def macros(self):
        pass


