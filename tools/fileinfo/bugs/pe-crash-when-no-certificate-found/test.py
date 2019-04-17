from regression_tests import *

class Test(Test):
    """Checks that fileinfo does not crash when analyzing a PE sample for which
    we are unable to find a signer or counter-signer.

    https://github.com/avast/retdec/issues/87
    """

    settings=TestSettings(
        tool='fileinfo',
        args='--verbose',
        input=[
            '74DB92D527624055DC928DFC7DC19DDA7FA257B2BC9F5539CEAFE2E8B4FFD6F3.dat',
            'E7B7C4B486676CF535F9CFE1A84F991E8544E220EB0B06D33A0D808635DA3713.dat',
        ]
    )

    def test_fileinfo_does_not_crash(self):
        assert self.fileinfo.succeeded
