from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='palindrome',
            expected_return_code=0,
            expected_output='Try again! (palindrome)\n'
        )
        self.assert_c_produces_output_when_run(
            input='krk',
            expected_return_code=0,
            expected_output='krk is a palindrome\n'
        )
        self.assert_c_produces_output_when_run(
            input='madam',
            expected_return_code=0,
            expected_output='madam is a palindrome\n'
        )
        self.assert_c_produces_output_when_run(
            input='drapegepard',
            expected_return_code=0,
            expected_output='drapegepard is a palindrome\n'
        )
        self.assert_c_produces_output_when_run(
            input='kajamamajak',
            expected_return_code=0,
            expected_output='kajamamajak is a palindrome\n'
        )

class Test_2018(TestBase):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17', excluding=r'.*\.exe'),
    )

class Test_2018_x64Pe(Test):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17', matching=r'.*\.exe'),
    )

    def test_check_funcion_rev(self):
        assert self.out_c.has_func('rev')
        assert self.out_c.funcs['rev'].return_type.is_void()
        assert self.out_c.funcs['rev'].param_count == 2
        assert self.out_c.funcs['rev'].params[0].type.is_pointer()
        assert self.out_c.funcs['rev'].params[0].type.pointed_type.is_char()
        assert self.out_c.funcs['rev'].params[1].type.is_pointer()
        assert self.out_c.funcs['rev'].params[1].type.pointed_type.is_char()
        assert self.out_c.funcs['rev'].has_any_assignments()
        assert self.out_c.funcs['rev'].calls('strlen')
        assert self.out_c.funcs['rev'].has_any_for_loops() or self.out_c.funcs['rev'].has_any_while_loops()

    def test_check_function_main(self):
        assert self.out_c.has_func('main')
        assert self.out_c.funcs['main'].calls('malloc')
        assert self.out_c.funcs['main'].calls('scanf')
        assert self.out_c.funcs['main'].calls('printf')
        assert self.out_c.funcs['main'].calls('free')
        assert self.out_c.funcs['main'].has_any_while_loops()
        assert self.out_c.funcs['main'].has_any_if_stmts()
        assert self.out_c.funcs['main'].has_any_return_stmts()
        # assert self.out_c.funcs['main'].has_return_stmts('return 0') TODO

    def test_check_presence_of_literals(self):
        assert self.out_c.has_string_literal('%s')
        assert self.out_c.has_string_literal('%s is a palindrome\\n')
        assert self.out_c.has_string_literal('Try again! (%s)\\n')

class Test_2017(TestBase):
    settings_2017 = TestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = TestSettings(
        input=files_in_dir('2015-03-30'),
    )
