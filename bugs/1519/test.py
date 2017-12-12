from regression_tests import *

inName="ackermann"

class CommonTest(Test):

    settings = TestSettings(
        input = 'min.exe'
    )

    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='',
            expected_return_code=0,
            expected_output='''123456'''
        )
