from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='PECompact_2.98.5_C_big_5.ex'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*PECompact \(2\.98\.5\)*')
