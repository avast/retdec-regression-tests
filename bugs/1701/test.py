from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input='libMaevex.so',
        args='--backend-no-opts'
    )

    def test(self):
        assert self.decomp.succeeded
