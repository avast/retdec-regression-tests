from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input='_keygen_.exe',
        arch='powerpc'
    )

    def test(self):
        assert self.decompiler.succeeded
