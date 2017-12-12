from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='mips-elf-df0691c3563daddf77f7ac9189475e08'
    )

    def test_has_symbol_tables(self):
        assert self.fileinfo.succeeded
        self.assertEqual(len(self.fileinfo.output['symbolTables']), 2)
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['numberOfSymbols'], '299')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['name'], 'symbol_dynamic_1')
        self.assertEqual(self.fileinfo.output['symbolTables'][1]['numberOfSymbols'], '283')
        self.assertEqual(self.fileinfo.output['symbolTables'][1]['name'], 'got_dynamic_1')
