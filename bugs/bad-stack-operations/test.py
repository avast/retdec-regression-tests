from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='strcpy.elf'
    )

    def test_while_loop(self):
        assert self.out_c.contains('while \(.*v. != 0\)')
        assert self.out_c.contains('v5\+\+')
        assert self.out_c.contains('v4\+\+')
        assert self.out_c.contains('v4 =.*v6')
        assert self.out_c.contains('v6 =.*v5')
