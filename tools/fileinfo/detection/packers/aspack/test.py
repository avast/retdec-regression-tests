from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='ASP212_C_big.Exp_tbl_comp.ex'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*ASPack \(2\.12\)*')
