from regression_tests import *

class Clang61500Test(Test):
    settings=TestSettings(
        input=['float_P61500.powerpc.clang.O0.g.elf', 'float_P61500.powerpc.gcc.O0.g.elf', 'float_P61501.powerpc.clang.O0.g.elf', 'float_P61501.powerpc.gcc.O0.g.elf'],
    )

    def test(self):
        assert self.decomp.succeeded
