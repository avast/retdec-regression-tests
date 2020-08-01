import os

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

class Test_2018(Test):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17'),
    )

    def test_check_function_op1(self):
        assert self.out_c.has_func('op1')
        assert self.out_c.funcs['op1'].return_type.is_float(32)
        assert self.out_c.funcs['op1'].param_count == 2
        assert self.out_c.funcs['op1'].params[0].type.is_int(32)
        assert self.out_c.funcs['op1'].params[1].type.is_int(32)
        assert self.out_c.funcs['op1'].calls('printf')
        assert self.out_c.funcs['op1'].has_any_return_stmts()

    def test_check_function_op2(self):
        assert self.out_c.has_func('op2')
        assert self.out_c.funcs['op2'].return_type.is_float(32)
        assert self.out_c.funcs['op2'].param_count == 2
        assert self.out_c.funcs['op2'].params[0].type.is_int(32)
        assert self.out_c.funcs['op2'].params[1].type.is_int(32)
        assert (self.out_c.funcs['op2'].calls('printf')
                or self.out_c.funcs['op2'].calls('puts'))
        assert self.out_c.funcs['op2'].has_any_return_stmts()

        if self.out_c.funcs['op2'].calls('printf'):
            assert self.out_c.has_string_literal("div\\n")
        else:
            assert self.out_c.has_string_literal("div")

    def test_check_function_main(self):
        assert self.out_c.has_func('main')
        assert self.out_c.funcs['main'].calls('scanf')
        assert self.out_c.funcs['main'].calls('printf')
        assert self.out_c.funcs['main'].calls('op1')
        assert self.out_c.funcs['main'].calls('op2')
        assert self.out_c.funcs['main'].has_any_return_stmts()

    def test_check_presence_of_literal(self):
        assert self.out_c.has_string_literal('mul by %f\\n')
        assert self.out_c.has_string_literal('%d a %d\\n')
        assert self.out_c.has_string_literal('%d %d')
        assert self.out_c.has_string_literal('Result1 : %.2f\\n')
        assert self.out_c.has_string_literal('Result2 : %f\\n')
        assert self.out_c.has_string_literal('%d / 2.33 = %.2f\\n')

class Test_2017(TestBase):
    settings_2017 = TestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = TestSettings(
        input=files_in_dir('2015-03-30'),
    )
