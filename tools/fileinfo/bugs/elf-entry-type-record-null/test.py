from regression_tests import *


class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='6d6d66d351c6f000a161c05826e6e04985c093d4a79e6b0ae909faca3ab57099'
    )

    def test_sample_loaded_ok(self):
        assert self.fileinfo.succeeded
        assert 'architecture' in self.fileinfo.output
