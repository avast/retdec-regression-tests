from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input='g8.exe'
    )

    def test_dsm_output_is_not_too_big(self):
        num_lines = len(self.out_dsm.split('\n'))
        assert num_lines < 1000
