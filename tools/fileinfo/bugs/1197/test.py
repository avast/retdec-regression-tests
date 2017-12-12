from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='Project1.ex'
    )

    def test_check_fileinfo_output(self):
        assert self.fileinfo.output.contains('PE')
        assert self.fileinfo.output.contains('x86')
        assert self.fileinfo.output.contains('DLL')
