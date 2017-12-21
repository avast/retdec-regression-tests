from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='fact_rec.ex'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*EXE Stealth \(2\.71\)*')
