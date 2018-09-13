from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='',
            expected_return_code=35,
            expected_output=''
        )

class Test_2018(Test):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17'),
    )

class Test_2017(TestBase):
    settings = TestSettings(
        input=files_in_dir('2017-11-14'),
    )
