from regression_tests import *

class Test_2017(Test):
    settings_2017 = TestSettings(
        input=files_in_dir('2017-11-14'),
    )

    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='aaaaaaaaaabbbbbbbbbbbbbbbbccccccccccccccdddddddddddd',
            expected_output='52\n',
            expected_return_code=52
        )

class Test_2015(Test):
    settings_2015 = TestSettings(
        input=files_in_dir('2015-03-30'),
    )

    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='aaaaaaaaaabbbbbbbbbbbbbbbbccccccccccccccdddddddddddd',
            expected_output='',
            expected_return_code=52
        )
