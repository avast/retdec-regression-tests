from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='255',
            expected_return_code=0,
            expected_output='255 contains 8 bit set\n'
        )
        self.assert_c_produces_output_when_run(
            input='256',
            expected_return_code=0,
            expected_output='256 contains 1 bit set\n'
        )
        self.assert_c_produces_output_when_run(
            input='1023',
            expected_return_code=0,
            expected_output='1023 contains 10 bit set\n'
        )
        self.assert_c_produces_output_when_run(
            input='556445',
            expected_return_code=0,
            expected_output='556445 contains 12 bit set\n'
        )
        self.assert_c_produces_output_when_run(
            input='457785621',
            expected_return_code=0,
            expected_output='457785621 contains 12 bit set\n'
        )

class Test_2017(TestBase):
    settings_2017 = CriticalTestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = CriticalTestSettings(
        input=files_in_dir('2015-03-30'),
    )
