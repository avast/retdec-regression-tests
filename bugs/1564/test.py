from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input='Presentation',
        args='-k --backend-no-opts'
    )

    def test(self):
        assert self.decomp.succeeded
