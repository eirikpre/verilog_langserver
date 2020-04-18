import os
import time
import unittest
import pathlib

from verilog_langserver.verilog_parser.parser import Parser


class TestParser(unittest.TestCase):

    report_time = True
    diagnosis = True

    def setUp(self):
        self.folder = pathlib.Path(__file__).parent / 'verilog'
        self.parser = Parser()

    def test_symbols(self):
        starttime = time.time()
        for fn in [f.path for f in os.scandir(self.folder) if not f.is_dir()]:
            _ = self.parser.parse_fast(fn)
        if self.report_time:
            print("test_symbols:", time.time()-starttime, "seconds")

    @unittest.skipUnless(diagnosis, "Not diagnosis")
    def test_diagnosis(self):
        for fn in [f.path for f in os.scandir(self.folder) if not f.is_dir()][0:1]:
            s = os.path.split(fn)[-1]
            print(s , '...', end=' ')
            starttime = time.time()
            items = self.parser.parse_diagnosis(fn)
            print(f'{time.time()-starttime}s')
            for i in items:
                print('\t' + i.message)

if __name__ == '__main__':
    unittest.main()

