from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input='IRIthai.exe',
        # We need to only check that the generated LLVM IR is correct (see
        # #1608). Back-end runs too long on this input file, anyway.
        args='--stop-after bin2llvmir'
    )

    def test(self):
        assert self.decomp.succeeded
