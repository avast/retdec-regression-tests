
from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='mips-elf-9a2ec63e3a061e1d2d86ea84e17343c4'
    )

    def setUp(self):
        # Prevent the base class from checking that the decompilation
        # succeeded (we expect it to fail).
        pass

    def test_check_error_message(self):
        assert self.decompiler.return_code == 1
        assert self.decompiler.log.contains( r'Error: Unsupported target format \'ELF64\'.' )
