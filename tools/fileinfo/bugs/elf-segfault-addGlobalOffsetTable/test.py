from regression_tests import *

class TestNoSegfault(Test):

    settings = TestSettings(
        tool='fileinfo',
        input='feac0b7ef47b197a381b04d057853ebe'
    )

    def test_fileinfo_does_not_crash(self):
        assert self.fileinfo.succeeded
