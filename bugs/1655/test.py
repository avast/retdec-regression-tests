from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input='lib704.o',
        args='--backend-no-opts'
    )

    def test(self):
        assert self.decompiler.succeeded
