from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='1eRNZmNRpM.in'
    )

    def test_fileinfo_failed(self):
        assert self.fileinfo.failed
        assert self.fileinfo.output.contains('Error: File format of the input file is not supported.')
