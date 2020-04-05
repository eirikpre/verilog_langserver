import unittest
import pathlib

from verilog_langserver.verilog_parser.parser import Parser


class TestParser(unittest.TestCase):
    def test_parse(self):
        parser = Parser()

        folder = pathlib.Path(__file__).parent / 'verilog'
        all_items = {}

        for fn in [
                    folder / 'class_example.sv',
                    folder / 'design.v',
                    folder / 'driver.sv',
                    folder / 'interface.sv' ]:
            items = parser.parse_fast(fn)
            all_items.update(items)



        print(all_items)
        return 1

if __name__ == '__main__':
    unittest.main()

