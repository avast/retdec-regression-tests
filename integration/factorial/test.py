from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='5',
            expected_return_code=0,
            expected_output='factorial( 5 ) = 120\n'
        )
        self.assert_c_produces_output_when_run(
            input='1',
            expected_return_code=0,
            expected_output='factorial( 1 ) = 1\n'
        )
        self.assert_c_produces_output_when_run(
            input='0',
            expected_return_code=0,
            expected_output='factorial( 0 ) = 1\n'
        )
        self.assert_c_produces_output_when_run(
            input='12',
            expected_return_code=0,
            expected_output='factorial( 12 ) = 479001600\n'
        )
        self.assert_c_produces_output_when_run(
            input='9',
            expected_return_code=0,
            expected_output='factorial( 9 ) = 362880\n'
        )

class Test_2017(TestBase):
    settings_2017 = CriticalTestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2017_todo(Test):
    settings_2017 = CriticalTestSettings(
        input=files_in_dir('2017-11-14-todo'),
    )

    def test_c_contains_main(self):
        assert self.out_c.has_func('main')

    def test_c_contains_all_strings(self):
        assert self.out_c.has_string_literal('factorial( %d ) = %d\\n')

class Test_2015(TestBase):
    settings_2015 = CriticalTestSettings(
        input=files_in_dir('2015-03-30'),
    )
