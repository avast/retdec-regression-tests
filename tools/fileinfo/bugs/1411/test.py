from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='LiquidSky.ex'
    )

    def test_no_bytecode(self):
        assert self.fileinfo.succeeded
        assert not self.fileinfo.output.contains('bytecode')
