from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='Abundant-O0-g'
    )

    def test_check_fileinfo_output(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains('PE')
        assert self.fileinfo.output.contains('x86')
        assert self.fileinfo.output.contains('Executable file')
        assert self.fileinfo.output.contains('Little endian')
        assert self.fileinfo.output.contains('Borland Delphi')
