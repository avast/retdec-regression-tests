from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='fact_rec.ex'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*WWPack32 \(1\.x\)*')
