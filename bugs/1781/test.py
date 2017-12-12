from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input='arm-elf-8d2def0c193dbc351053f9acdcb0529a'
    )

    def test(self):
        assert self.decomp.succeeded
