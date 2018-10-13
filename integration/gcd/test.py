from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='957 1037',
            expected_return_code=0,
            expected_output=
'''gcd1 957 1037 = 1
gcd2 1037 957 = 1
gcd3 1037 957 = 1
'''
        )
        self.assert_c_produces_output_when_run(
            input='10 7',
            expected_return_code=0,
            expected_output=
'''gcd1 10 7 = 1
gcd2 7 10 = 1
gcd3 7 10 = 1
'''
        )
        self.assert_c_produces_output_when_run(
            input='135 99',
            expected_return_code=0,
            expected_output=
'''gcd1 135 99 = 9
gcd2 99 135 = 9
gcd3 99 135 = 9
'''
        )

class Test_2017(TestBase):
    settings_2017 = TestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = TestSettings(
        input=files_in_dir('2015-03-30'),
    )
