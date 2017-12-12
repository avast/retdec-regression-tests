from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='Youda_13_C_big_ALL.ex'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*yoda\'s Crypter \(1\.3\)*')
