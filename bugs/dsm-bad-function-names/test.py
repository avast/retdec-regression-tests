from regression_tests import *

class TestDsm(Test):
    settings=TestSettings(
        input='test.exe'
    )

    def test_strings_in_code(self):
        assert self.out_dsm.contains(r'0x407755:.*call 0x407458 <puts>')
        assert self.out_dsm.contains(r'; function: _puts at 0x407458 -- 0x40745e')
        assert self.out_dsm.contains(r'0x407458:.*jmp dword ptr \[0x40b1e8\] <puts>')
