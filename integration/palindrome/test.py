from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='palindrome',
            expected_return_code=0,
            expected_output='Try again! (palindrome)\n'
        )
        self.assert_c_produces_output_when_run(
            input='krk',
            expected_return_code=0,
            expected_output='krk is a palindrome\n'
        )
        self.assert_c_produces_output_when_run(
            input='madam',
            expected_return_code=0,
            expected_output='madam is a palindrome\n'
        )
        self.assert_c_produces_output_when_run(
            input='drapegepard',
            expected_return_code=0,
            expected_output='drapegepard is a palindrome\n'
        )
        self.assert_c_produces_output_when_run(
            input='kajamamajak',
            expected_return_code=0,
            expected_output='kajamamajak is a palindrome\n'
        )

class Test_2017(TestBase):
    settings_2017 = CriticalTestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = CriticalTestSettings(
        input=files_in_dir('2015-03-30'),
    )
