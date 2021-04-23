from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input='FD13AF98BC4C7A84E381EFB89BD7AAD4A03211157FC5050B03BF63E8090DD959',
        tool='unpacker'
    )

    def test_unpacking_successful(self):
        assert self.unpacker.succeeded
        self.assertTrue('Detected filter 0x26 with parameter 0x5 based on signature.' in self.unpacker.output)
