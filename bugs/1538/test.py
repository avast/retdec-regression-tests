from regression_tests import *

class Test(Test):
    """Check that bin2llvmir does not crash or generate invalid LLVM IR."""

    settings=TestSettings(
        input='ELF.out',
        args='-k --stop-after bin2llvmir'
    )

    def test(self):
        assert self.decompiler.succeeded
