from regression_tests import *

class UnitTests(Test):
    settings = TestSettings(
        tool='retdec-tests-runner.py'
    )

    def test_all_tests_pass(self):
        if 'no unit tests found' in self.tool.output:
            self.skipTest('no unit tests found')
            return

        output = 'tests failed; output:\n\n' + self.tool.output
        assert self.tool.succeeded, output
