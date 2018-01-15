from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input='lib_SoundAlive_ver118t.so',
        args='--stop-after bin2llvmir'
    )

    def test(self):
        assert self.decompiler.succeeded
