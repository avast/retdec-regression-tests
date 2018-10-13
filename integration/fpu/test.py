from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='1.2 34.56 67.89',
            expected_return_code=0,
            expected_output=
'''#2 3.140000
3.140000
67.889999
'''
        )
        self.assert_c_produces_output_when_run(
            input='123.456 67.89 34.56',
            expected_return_code=0,
            expected_output=
'''#2 3.140000
123.456001
67.889999
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
