from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input = 'mips-elf-94a5c4e284bb911cfdce4252b1e5129c',
        args = '--backend-no-opts'
    )

    def test_decompilation_succeeds(self):
        assert self.decompiler.succeeded
