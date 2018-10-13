from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='hello.exe'
    )

    def test_main_addresses(self):
        assert self.out_c.contains('Address range: 0x407740 - 0x40775e')
        assert self.out_dsm.contains('function: main at 0x407740 -- 0x40775e')
