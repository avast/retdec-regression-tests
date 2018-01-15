from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input='libjiagu.so',
        args='--backend-no-opts'
    )

    def test(self):
        assert self.decompiler.succeeded
