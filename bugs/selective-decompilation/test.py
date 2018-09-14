from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='selective-decompiletion.elf',
        args='--select-functions func --select-decode-only'
    )

    def test_main_is_not_decompiled(self):
        # We cannot test that only func() is present because another function
        # is decompiled from some garbage after func().
        assert not self.out_c.has_func('main')
