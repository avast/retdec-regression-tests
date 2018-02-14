from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input=['mips-elf-020bc2943f91816a1a82c20f2a688336', 'mips-elf-fd27a58c009f1700499804d6f8a35981']
    )

    def test_decompilation_succeeds(self):
        assert self.decompiler.succeeded
