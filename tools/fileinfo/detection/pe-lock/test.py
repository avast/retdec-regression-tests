from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='pbmsrch_max_pelock1_0694.ex'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*PELock \(1\.x\)*')
