from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='test.ko'
    )

    def test_fileinfo_succeeded(self):
        assert self.fileinfo.succeeded
