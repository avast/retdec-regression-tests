from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='Morphine_12_C_big_1.ex'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*Morphine \(1\.2\)*')
