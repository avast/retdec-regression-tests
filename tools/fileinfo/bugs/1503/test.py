from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=['core', 'KainOSBoot.o', 'WinOLS_BMW_E46_DervTech2_-361860_', 'array3.out.c.frontend.ccoff'],
    )

    def test_fileinfo_correctly_failed(self):
        assert self.fileinfo.failed
        assert self.fileinfo.output.contains('Error: File format of the input file is not supported.')
