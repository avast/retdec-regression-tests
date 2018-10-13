from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='11',
            expected_return_code=0,
            expected_output="Prime factors of '11': 11\n"
        )
        self.assert_c_produces_output_when_run(
            input='4555631',
            expected_return_code=0,
            expected_output="Prime factors of '4555631': 4555631\n"
        )
        self.assert_c_produces_output_when_run(
            input='44545',
            expected_return_code=0,
            expected_output="Prime factors of '44545': 5 x 59 x 151\n"
        )
        self.assert_c_produces_output_when_run(
            input='23917',
            expected_return_code=0,
            expected_output="Prime factors of '23917': 23917\n"
        )
        self.assert_c_produces_output_when_run(
            input='44457413',
            expected_return_code=0,
            expected_output="Prime factors of '44457413': 7 x 11 x 13 x 23 x 1931\n"
        )
        self.assert_c_produces_output_when_run(
            input='81',
            expected_return_code=0,
            expected_output="Prime factors of '81': 3 x 3 x 3 x 3\n"
        )
        self.assert_c_produces_output_when_run(
            input='105',
            expected_return_code=0,
            expected_output="Prime factors of '105': 3 x 5 x 7\n"
        )
        self.assert_c_produces_output_when_run(
            input='4096',
            expected_return_code=0,
            expected_output="Prime factors of '4096': 2 x 2 x 2 x 2 x 2 x 2 x 2 x 2 x 2 x 2 x 2 x 2\n"
        )

class Test_2017(TestBase):
    settings_2017 = TestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = TestSettings(
        input=files_in_dir('2015-03-30'),
    )
