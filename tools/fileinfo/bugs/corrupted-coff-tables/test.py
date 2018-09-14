from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='MINI-project-AMSO.ex'
    )

    def test_invalid_coff_symbol_name_with_limited_length(self):
        assert self.fileinfo.succeeded
        symbol_name = self.fileinfo.output['symbolTables'][0]['symbols'][2]['name']
        orig_symbol_name_part = symbol_name.encode('ascii').decode('unicode_escape')
        self.assertEqual(len(orig_symbol_name_part), 96)
