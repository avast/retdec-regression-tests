from regression_tests import *

# https://github.com/avast/retdec/issues/242
class TestNoInfLoop(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='infinity_loop'
    )

    def test_no_inf_loop(self):
        assert self.fileinfo.succeeded
