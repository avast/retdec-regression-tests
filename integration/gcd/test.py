from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='957 1037',
            expected_return_code=0,
            expected_output=
'''gcd1 957 1037 = 1
gcd2 1037 957 = 1
gcd3 1037 957 = 1
'''
        )
        self.assert_c_produces_output_when_run(
            input='10 7',
            expected_return_code=0,
            expected_output=
'''gcd1 10 7 = 1
gcd2 7 10 = 1
gcd3 7 10 = 1
'''
        )
        self.assert_c_produces_output_when_run(
            input='135 99',
            expected_return_code=0,
            expected_output=
'''gcd1 135 99 = 9
gcd2 99 135 = 9
gcd3 99 135 = 9
'''
        )

class Test_2018(TestBase):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17', excluding=r'(.*\.exe|gcd.x64.clang.O0.g.elf)'),
    )

class Test_2018_x64Pe(Test):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17', matching=r'(.*\.exe|gcd.x64.clang.O0.g.elf)'),
    )

    def test_check_function_gcd1(self):
        assert self.out_c.has_func('gcd1')
        assert self.out_c.funcs['gcd1'].return_type.is_int(32)
        assert self.out_c.funcs['gcd1'].param_count == 2
        assert self.out_c.funcs['gcd1'].params[0].type.is_int(32)
        assert self.out_c.funcs['gcd1'].params[1].type.is_int(32)
        assert self.out_c.funcs['gcd1'].has_any_while_loops()
        assert self.out_c.funcs['gcd1'].has_any_return_stmts()
        assert self.out_c.funcs['gcd1'].has_any_if_stmts()
        assert self.out_c.funcs['gcd1'].has_any_assignments()

    def test_check_function_gcd2(self):
        assert self.out_c.has_func('gcd2')
        assert self.out_c.funcs['gcd2'].return_type.is_int(32)
        assert self.out_c.funcs['gcd2'].param_count == 2
        assert self.out_c.funcs['gcd2'].params[0].type.is_int(32)
        assert self.out_c.funcs['gcd2'].params[1].type.is_int(32)
        assert self.out_c.funcs['gcd2'].has_any_return_stmts()
        assert self.out_c.funcs['gcd2'].has_any_if_stmts()
        assert self.out_c.funcs['gcd2'].has_any_assignments()
        assert self.out_c.funcs['gcd2'].calls('gcd2')

    def test_check_function_gcd2(self):
        assert self.out_c.has_func('gcd3')
        assert self.out_c.funcs['gcd3'].return_type.is_int(32)
        assert self.out_c.funcs['gcd3'].param_count == 2
        assert self.out_c.funcs['gcd3'].params[0].type.is_int(32)
        assert self.out_c.funcs['gcd3'].params[1].type.is_int(32)
        assert self.out_c.funcs['gcd3'].has_any_assignments()
        assert self.out_c.funcs['gcd3'].has_any_while_loops()
        assert self.out_c.funcs['gcd3'].has_any_return_stmts()

    def test_check_function_main(self):
        assert self.out_c.has_func('main')
        assert self.out_c.funcs['main'].calls('gcd1')
        assert self.out_c.funcs['main'].calls('gcd2')
        assert self.out_c.funcs['main'].calls('gcd3')
        assert self.out_c.funcs['main'].calls('printf')
        assert self.out_c.funcs['main'].calls('scanf')
        assert self.out_c.funcs['main'].has_any_return_stmts()
        assert self.out_c.funcs['main'].has_any_assignments()

    def test_check_presence_of_literals(self):
        assert self.out_c.has_string_literal('%d %d')
        assert self.out_c.has_string_literal('gcd1 %d %d = %d\\n')
        assert self.out_c.has_string_literal('gcd2 %d %d = %d\\n')
        assert self.out_c.has_string_literal('gcd3 %d %d = %d\\n')

class Test_2017(TestBase):
    settings_2017 = TestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = TestSettings(
        input=files_in_dir('2015-03-30'),
    )
