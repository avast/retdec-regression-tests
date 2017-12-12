from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='1 2 3',
            expected_return_code=4,
            expected_output='XYZ\n'
        )
        self.assert_c_produces_output_when_run(
            input='0 10 0',
            expected_return_code=3,
            expected_output='XY\n'
        )

class Test_2017(TestBase):
    settings_2017 = CriticalTestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = CriticalTestSettings(
        input=files_in_dir('2015-03-30'),
    )
