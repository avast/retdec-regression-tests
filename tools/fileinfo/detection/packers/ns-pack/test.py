from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='NSPack_23_C_big_DEF.ex'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*NsPacK \(2\.3\)*')
