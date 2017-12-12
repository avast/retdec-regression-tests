from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='CRACKME3.EX'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*Krypton \(0\.5\)*')
