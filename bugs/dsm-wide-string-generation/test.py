from regression_tests import *

class Test(Test):

    settings = TestSettings(
        input='wide-strings.x86.gcc.O2.exe'
    )

    def test_dsm_for_wide_strings(self):
        assert self.out_dsm.contains(r'0x40776a:.*mov dword ptr \[esp\], 0x409050 ; L"Hello world"')
        assert self.out_dsm.contains(r'0x409050:.*|H.e.l.l.o. .w.o.|   L"Hello world"')
