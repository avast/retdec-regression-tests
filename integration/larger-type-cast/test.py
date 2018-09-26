from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='1',
            expected_output='You typed 1\n',
            expected_return_code=0
        )

class Test_2018(TestBase):
    settings_2018 = CriticalTestSettings(
        input=files_in_dir('2018-09-25'),
    )
