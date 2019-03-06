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

class Test_2018(TestBase):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17', excluding=r'.*\.exe'),
    )

class Test_2018_x64Pe(Test):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17', matching=r'.*\.exe'),
    )

    def test_check_function_factorial(self):
        assert self.out_c.has_func('factorial')
        assert self.out_c.funcs['factorial'].return_type.is_int(32)
        assert self.out_c.funcs['factorial'].param_count == 1
        assert self.out_c.funcs['factorial'].params[0].type.is_int(32)
        assert self.out_c.funcs['factorial'].has_any_if_stmts()
        assert self.out_c.funcs['factorial'].calls('factorial')
        assert self.out_c.funcs['factorial'].has_any_return_stmts()

    def test_check_function_main(self):
        assert self.out_c.has_func('main')
        assert self.out_c.funcs['main'].calls('scanf')
        assert self.out_c.funcs['main'].calls('printf')
        assert self.out_c.funcs['main'].has_any_return_stmts()

    def test_check_presence_of_literals(self):
        assert self.out_c.has_string_literal('%d')
        assert self.out_c.has_string_literal('factorial( %d ) = %d\\n')

class Test_2017(TestBase):
    settings_2017 = TestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2017_todo(Test):
    settings_2017 = TestSettings(
        input=files_in_dir('2017-11-14-todo'),
    )

    def test_c_contains_main(self):
        assert self.out_c.has_func('main')

    def test_c_contains_all_strings(self):
        assert self.out_c.has_string_literal('factorial( %d ) = %d\\n')

class Test_2015(TestBase):
    settings_2015 = TestSettings(
        input=files_in_dir('2015-03-30'),
    )
