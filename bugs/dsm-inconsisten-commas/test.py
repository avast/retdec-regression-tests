from regression_tests import *

class Test(Test):

    settings = TestSettings(
        input='test.arm.exe'
    )

    def test_check_dsm(self):
        assert self.out_dsm.contains('0x11374:\s*f0 4f 2d e9\s*push \{r4, r5, r6, r7, r8, sb, sl, fp, lr\}')
