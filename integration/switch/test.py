from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='0',
            expected_return_code=0,
            expected_output=' 0 after 0 after 0 after 0 after 0 after 0 after 0 0 22 after before  0  after '
        )
        self.assert_c_produces_output_when_run(
            input='1',
            expected_return_code=0,
            expected_output=' 1 after 1 after 1 1after 1 1after 1 after 1 after1 22 after before  1  after '
        )
        self.assert_c_produces_output_when_run(
            input='4',
            expected_return_code=0,
            expected_output='4 0 after4after4after4after4after4after4 22 after before  4  after '
        )
        self.assert_c_produces_output_when_run(
            input='22',
            expected_return_code=0,
            expected_output='22 0 after22after22after22after22after22after 22 after before  22  after '
        )
        self.assert_c_produces_output_when_run(
            input='26',
            expected_return_code=0,
            expected_output='26 0 after26after26after26after26after26after26 22 after before  26  after '
        )
        self.assert_c_produces_output_when_run(
            input='30',
            expected_return_code=0,
            expected_output='30 0 after30after30after30after30after30after30 22 after before  30  after '
        )

class Test_2018(Test):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17'),
    )

    def test_check_global_variable(self):
        assert self.out_c.has_any_global_vars()
        assert self.out_c.has_global_vars('x')
        assert self.out_c.global_vars['x'].type.is_int(32)

    def check_switch_function_generic(self, func_name):
        assert self.out_c.has_func(func_name)
        assert self.out_c.funcs[func_name].return_type.is_void()
        assert self.out_c.funcs[func_name].param_count == 0
        #assert self.out_c.funcs[func_name].has_any_switch_stmts()
        #assert len (self.out_c.funcs[func_name].switch_stmts) == 1
        #assert self.out_c.funcs[func_name].switch_stmts[0].has_cases()
        #assert self.out_c.funcs[func_name].switch_stmts[0].has_default_case()
       # assert len(self.out_c.funcs[func_name].switch_stmts[0].cases) == 2
        assert self.out_c.funcs[func_name].calls('printf')

    def test_check_switch_functions(self):
        func_names = ['func1a', 'func1b', 'func2a', 'func2b', 'func3a', 'func3b', 'func4']

        for func in func_names:
            self.check_switch_function_generic(func)

    def test_check_function_jump_table(self):
        assert self.out_c.has_func('jump_table')
        assert self.out_c.funcs['jump_table'].return_type.is_void()
        assert self.out_c.funcs['jump_table'].param_count == 0
        #assert self.out_c.funcs['jump_table'].has_any_switch_stmts()
        #assert len (self.out_c.funcs['jump_table'].switch_stmts) == 1
        #assert self.out_c.funcs['jump_table'].switch_stmts[0].has_cases()
        #assert self.out_c.funcs['jump_table'].switch_stmts[0].has_default_case()
        #assert len(self.out_c.funcs['jump_table'].switch_stmts[0].cases) == 7
        assert self.out_c.funcs['jump_table'].calls('printf')

#    def test_check_function_jump_table2(self):
#        assert self.out_c.has_func('jump_table2')
#        assert self.out_c.funcs['jump_table2'].return_type.is_void()
#        assert self.out_c.funcs['jump_table2'].param_count == 0
#        assert self.out_c.funcs['jump_table2'].has_any_switch_stmts()
#        assert self.out_c.funcs['jump_table2'].calls('rand')
#        assert self.out_c.funcs['jump_table2'].has_switch_stmts('switch (rand())')
#        assert self.out_c.funcs['jump_table2'].switch_stmts['switch (rand())'].has_cases()
#        assert self.out_c.funcs['jump_table2'].switch_stmts['switch (rand())'].has_default_case()
#        assert len(self.out_c.funcs['jump_table2'].switch_stmts['switch (rand())'].cases) == 6
#        assert self.out_c.funcs['jump_table2'].calls('printf')

    def test_check_function_main(self):
        assert self.out_c.has_func('main')
        assert self.out_c.funcs['main'].has_any_assignments()
        assert self.out_c.funcs['main'].has_assignments('x = 0')
        assert self.out_c.funcs['main'].calls('func1a')
        assert self.out_c.funcs['main'].calls('func1b')
        assert self.out_c.funcs['main'].calls('func2a')
        assert self.out_c.funcs['main'].calls('func2b')
        assert self.out_c.funcs['main'].calls('func3a')
        assert self.out_c.funcs['main'].calls('func3b')
        assert self.out_c.funcs['main'].calls('func4')
        assert self.out_c.funcs['main'].calls('jump_table')
        assert self.out_c.funcs['main'].has_any_return_stmts()

    def test_check_presence_of_literals(self):
        assert self.out_c.has_string_literal(' 0 ')
        assert self.out_c.has_string_literal(' 1 ')
        #assert self.out_c.has_string_literal(' 20 ')
        #assert self.out_c.has_string_literal(' 21 ')
        assert self.out_c.has_string_literal(' 22 ')
        #assert self.out_c.has_string_literal(' 23 ')
        #assert self.out_c.has_string_literal(' 24 ')
        #assert self.out_c.has_string_literal(' 25 ')
        #assert self.out_c.has_string_literal(' 28 ')
        #assert self.out_c.has_string_literal(' 2, 3 \\n')
        #assert self.out_c.has_string_literal(' 5 \\n')
        #assert self.out_c.has_string_literal(' 8 \\n')
        #assert self.out_c.has_string_literal(' 57 \\n')
        #assert self.out_c.has_string_literal(' break \\n')
        assert self.out_c.has_string_literal('%d')
        assert self.out_c.has_string_literal(' %d ')
        assert self.out_c.has_string_literal('after')
        #assert self.out_c.has_string_literal(' before jump table 2 ')

class Test_2017(TestBase):
    settings_2017 = TestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = TestSettings(
        input=files_in_dir('2015-03-30'),
    )

class Test_MSVC(Test):
    settings = TestSettings(
        input='switch-test-msvc-O0.ex',
    )

    def test_for_switches_in_function_411a90(self):
        assert self.out_c.contains('default: {')
        assert self.out_c.contains('case 20: {')
        assert self.out_c.contains('case 21: {')
        assert self.out_c.contains('case 22: {')
        assert self.out_c.contains('case 23: {')
        assert self.out_c.contains('case 24: {')
        assert self.out_c.contains('case 25: {')
        assert self.out_c.contains('case 28: {')

    def test_for_switches_in_function_411c90(self):
        assert self.out_c.contains('default: {')
        assert self.out_c.contains('case 0: {')
        assert self.out_c.contains('case 2: {')
        assert self.out_c.contains('case 3: {')
        assert self.out_c.contains('case 5: {')
        assert self.out_c.contains('case 8: {')
        assert self.out_c.contains('case 57: {')

    def test_for_strings(self):
        assert self.out_c.has_string_literal(' before ')
        assert self.out_c.has_string_literal(' after ')
        assert self.out_c.has_string_literal(' 0 ')
        assert self.out_c.has_string_literal(' 1 ')
        assert self.out_c.has_string_literal('%d')
        assert self.out_c.has_string_literal(' 20 ')
        assert self.out_c.has_string_literal(' 21 ')
        assert self.out_c.has_string_literal(' 22 ')
        assert self.out_c.has_string_literal(' 23 ')
        assert self.out_c.has_string_literal(' 24 ')
        assert self.out_c.has_string_literal(' 25 ')
        assert self.out_c.has_string_literal(' 28 ')
        assert self.out_c.has_string_literal(' before jump table 2 ')
        assert self.out_c.has_string_literal(' break \\n')
        assert self.out_c.has_string_literal(' 0 \\n')
        assert self.out_c.has_string_literal(' 2, 3 \\n')
        assert self.out_c.has_string_literal(' 5 \\n')
        assert self.out_c.has_string_literal(' 8 \\n')
        assert self.out_c.has_string_literal(' 57 \\n')
        assert self.out_c.has_string_literal(' after jumpt table 2 ')

    def test_issue_636(self):
        assert self.out_c.contains('char \* g[0-9]; // 0x419548')
