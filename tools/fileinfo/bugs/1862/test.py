from regression_tests import *

class TestNoSegfault(Test):

    settings = TestSettings(
        tool='fileinfo',
        input='feac0b7ef47b197a381b04d057853ebe'
    )

    def test_unmasq_does_not_produce_invalid_output(self):
        assert self.fileinfo.succeeded
