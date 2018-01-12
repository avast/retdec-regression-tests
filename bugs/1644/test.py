from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input='throwback_edea6803c60c9bc5da76f2da806d687c.exe',
        args='--backend-no-opts'
    )

    def test(self):
        assert self.decompiler.succeeded
