from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='armv7-pe-0e3cc431212359d1434cf96a3310abb5'
    )

    def test_check_fileinfo_output(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains('PE')
        assert self.fileinfo.output.contains('ARM')
        assert self.fileinfo.output.contains('DLL')
        assert self.fileinfo.output.contains('Little endian')
