from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='10 17',
            expected_return_code=0,
            expected_output=
'''10 a 17
mul by 3.789000
Result1 : 74.41
div
Result2 : 1.062500
10 / 2.33 = 4.29
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
