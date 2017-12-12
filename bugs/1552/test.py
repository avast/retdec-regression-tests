from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input='2agxmr6xjd.bin',
        arch='arm',
        args='--backend-no-opts --select-decode-only --select-ranges=0x569128-0x569160'
    )

    def test(self):
        assert self.decomp.succeeded
