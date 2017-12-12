from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input='tr69',
        config='tr69-config.json',
        args='--select-ranges 0x4b2ef0-0x4b2f6b,0x1005b9b4-0x1005b9b7,0x46e7d8-0x46eb6f --select-decode-only'
    )

    def test(self):
        assert self.decomp.succeeded
