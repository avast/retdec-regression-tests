from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='10 1730 17',
            expected_return_code=0,
            expected_output=
'''Mam 10 a 1730
DIV: 0, MOD: 10, MUL: 17300, ADD: 1740, SUB: -1720, other: 17280, 17270, 17260, 17250, 17240.000000. Char: X
Special number: 0
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
