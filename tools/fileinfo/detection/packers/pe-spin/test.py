from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='PESpin_132_C_big_anti_dmp.ex'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*PESpin \(1\.32\)*')
