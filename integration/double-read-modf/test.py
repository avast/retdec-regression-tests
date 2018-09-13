from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='13.458',
            expected_return_code=13,
            expected_output='func( 13.458 ) = 13.000000\n'
        )
        self.assert_c_produces_output_when_run(
            input='-21.12',
            expected_return_code=21,
            expected_output='func( -21.120 ) = 21.000000\n'
        )

class Test_2018(Test):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17'),
    )

    def test_check_function_func(self):
        assert self.out_c.has_func('func')
        assert self.out_c.funcs['func'].return_type.is_double()
        assert self.out_c.funcs['func'].param_count == 1
        assert self.out_c.funcs['func'].params[0].type.is_double()
        assert self.out_c.funcs['func'].calls('modf')

    def test_check_function_main(self):
        assert self.out_c.has_func('main')
        assert self.out_c.funcs['main'].calls('scanf')
        assert self.out_c.funcs['main'].calls('func')
        assert self.out_c.funcs['main'].calls('printf')
        assert self.out_c.funcs['main'].has_any_return_stmts()

    def test_check_presence_of_literals(self):
        assert self.out_c.has_string_literal('%lf')
        assert self.out_c.has_string_literal('func( %.3lf ) = %lf\\n')

class Test_2017(TestBase):
    settings_2017 = TestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = TestSettings(
        input=files_in_dir('2015-03-30'),
    )
