from regression_tests import *

class TestBasic(Test):
    """Related to:
    #41:  https://github.com/avast-tl/retdec/issues/41
    #169: https://github.com/avast-tl/retdec/issues/169
    #391: https://github.com/avast-tl/retdec/pull/391
    """
    settings=TestSettings(
        input='Test.exe'
    )

    def test(self):
        main = self.out_c.funcs['main']
        assert main.calls('__readfsdword')
        assert self.out_c.contains('__readfsdword\(24\)')
