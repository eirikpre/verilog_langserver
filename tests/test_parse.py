import os
import unittest
import pathlib

from verilog_langserver.verilog_parser.parser import Parser


class TestParser(unittest.TestCase):
    def test_parse(self):
        parser = Parser()

        folder = pathlib.Path(__file__).parent / 'verilog'

        for fn in [f.path for f in os.scandir(folder) if not f.is_dir()]:
            print(fn)
            items = parser.parse_fast(fn)
            for i in items:
                print('\t' + i.name)

        return 1

if __name__ == '__main__':
    unittest.main()

