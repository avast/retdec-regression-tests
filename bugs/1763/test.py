from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input = ['x86-elf-3264f357be0afb3068998259370ba105', 'x86-elf-6c3a2e29e618e3f17c1b32425f6fee52'],
        args = '--backend-no-opts'
    )

    def test_decompilation_succeeds(self):
        assert self.decomp.succeeded
