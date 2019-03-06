from regression_tests import *

class Test(Test):
    """Although the architecture reported for the input ELF is i386, it is a
    64b ELF and its header is probably corrupted (even IDA is unable to analyze
    it). Therefore, we should signal an error about an unsupported target
    format.
    """
    settings = TestSettings(
        input='x86_elf'
    )

    def setUp(self):
        # Prevent the base class from checking that the decompilation
        # succeeded (we expect it to fail).
        pass

    def test_decompilation_fails_because_of_unsupported_format(self):
        assert self.decompiler.failed
        assert self.decompiler.log.contains(r'Error: Unsupported target format and architecture combination')
