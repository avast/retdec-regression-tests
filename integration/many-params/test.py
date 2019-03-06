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

class Test_2018(Test):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17'),
    )

    def test_check_function_pokus(self):
        assert self.out_c.has_func('pokus')
        assert self.out_c.funcs['pokus'].return_type.is_int(32)
        assert self.out_c.funcs['pokus'].param_count == 11
        assert self.out_c.funcs['pokus'].params[0].type.is_int(32)
        assert self.out_c.funcs['pokus'].params[1].type.is_int(32)
        assert self.out_c.funcs['pokus'].params[2].type.is_int(32)
        assert self.out_c.funcs['pokus'].params[3].type.is_int(32)
        assert self.out_c.funcs['pokus'].params[4].type.is_int(32)
        assert self.out_c.funcs['pokus'].params[5].type.is_int(32)
        assert self.out_c.funcs['pokus'].params[6].type.is_int(32)
        assert self.out_c.funcs['pokus'].params[7].type.is_int(32)
        assert self.out_c.funcs['pokus'].params[8].type.is_int(32)
        assert self.out_c.funcs['pokus'].params[9].type.is_float(32)
        assert self.out_c.funcs['pokus'].params[10].type.is_char()
        assert self.out_c.funcs['pokus'].calls('printf')
        assert self.out_c.funcs['pokus'].has_any_return_stmts()

    def test_check_function_main(self):
        assert self.out_c.has_func('main')
        assert self.out_c.funcs['main'].calls('scanf')
        assert self.out_c.funcs['main'].calls('printf')
        assert self.out_c.funcs['main'].has_any_if_stmts()
        assert self.out_c.funcs['main'].has_any_return_stmts()

    def test_check_presence_of_literals(self):
        assert self.out_c.has_string_literal('DIV: %d, MOD: %d, MUL: %d, ADD: %d, SUB: %d, other: %d, %d, %d, %d, %f. Char: %c\\n')
        assert self.out_c.has_string_literal('%d %d')
        assert self.out_c.has_string_literal('Mam %d a %d\\n')
        assert self.out_c.has_string_literal('Special number: %d\\n')
        assert self.out_c.has_string_literal('Chyba vstupu, nacitanych %d\\n')

class Test_2017(TestBase):
    settings_2017 = TestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = TestSettings(
        input=files_in_dir('2015-03-30'),
    )
