from regression_tests import *

class Bug1456Test(Test):
    settings = TestSettings(
        tool='unpacker',
        input='ramnit.ex'
    )

    def test_ramnit(self):
        assert self.unpacker.succeeded
        assert self.unpacker.output.contains('NRV2B')
