from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input=['firmware_upgrader', 'x86-elf-d20f06e2a8ceb9034e86260391f0bc33'],
        args='--backend-no-opts -k'
    )

    def test(self):
        assert self.decompiler.succeeded
