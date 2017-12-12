from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='fact_rec_ASProtect1_2.ex'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*ASProtect \(1\.2\)*')
