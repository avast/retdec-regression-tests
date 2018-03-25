from regression_tests import *


# https://github.com/avast-tl/retdec/issues/89
class TestStringTableSegfault(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='79e34ba714e38c7e72f30b5dcb54ba4e4e05915dbaece7fdf4271b1410306e04'
    )

    def test_no_segfault(self):
        assert self.fileinfo.succeeded


# https://github.com/avast-tl/retdec/issues/89
class TestDynamicSegfault(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='4dfc8ebfa6d90d2fbacf56c035b04aa38a3c595f462904f4a038d45dcb9d3a7b'
    )

    def test_no_segfault(self):
        assert self.fileinfo.succeeded


# https://github.com/avast-tl/retdec/issues/248
class TestReloationTableSegfault(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='98bd83292d284692f5723d52dc1ba467a3a5c38c03ced34b5307c511e113e390'
    )

    def test_no_segfault(self):
        assert self.fileinfo.succeeded

