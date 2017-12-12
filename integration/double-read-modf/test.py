from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='13.458',
            expected_return_code=13,
            expected_output='func( 13.458 ) = 13.000000\n'
        )
        self.assert_c_produces_output_when_run(
            input='-21.12',
            expected_return_code=21,
            expected_output='func( -21.120 ) = 21.000000\n'
        )

class Test_2017(TestBase):
    settings_2017 = CriticalTestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = CriticalTestSettings(
        input=files_in_dir('2015-03-30'),
    )
