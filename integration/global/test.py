from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        assert self.out_c.has_func( 'main' )
        self.assert_c_produces_output_when_run(
            input='100 500',
            expected_return_code=0,
            expected_output=
'''123456
456789
654321
100
987654
500
'''
        )
        self.assert_c_produces_output_when_run(
            input='200 600',
            expected_return_code=0,
            expected_output=
'''123456
456789
654321
200
987654
600
'''
        )

class Test_2017(TestBase):
    settings_2017 = CriticalTestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = CriticalTestSettings(
        input=files_in_dir('2015-03-30'),
    )
