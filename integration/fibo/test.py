from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='10 1 3 5 6 8 10 15 18 23 33',
            expected_return_code=0,
            expected_output=
'''Input number of iterations: Input number: fibonacci(1) = 1
Input number: fibonacci(3) = 2
Input number: fibonacci(5) = 5
Input number: fibonacci(6) = 8
Input number: fibonacci(8) = 21
Input number: fibonacci(10) = 55
Input number: fibonacci(15) = 610
Input number: fibonacci(18) = 2584
Input number: fibonacci(23) = 28657
Input number: fibonacci(33) = 3524578
'''
        )

class Test_2015(TestBase):
    settings_2015 = TestSettings(
        input=files_in_dir('2015-03-30'),
    )

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

    def test_c_contains_for_or_while_loop(self):
        assert self.out_c.contains(r'(for|while) \(')

    def test_c_contains_all_strings(self):
        assert self.out_c.has_string_literal('Input number of iterations: ')
        assert self.out_c.has_string_literal('%d')
        assert self.out_c.has_string_literal('Input number: ')
        assert self.out_c.has_string_literal('fibonacci(%d) = %u\\n')

class Test_2018(TestBase):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17', excluding=r'.*\.exe'),
    )

class Test_2018_x64Pe(Test):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17', matching=r'.*\.exe'),
    )

    def test_check_function_fib(self):
        assert self.out_c.has_func('fib')
        assert self.out_c.funcs['fib'].return_type.is_int(32)
        assert self.out_c.funcs['fib'].param_count == 1
        assert self.out_c.funcs['fib'].params[0].type.is_int(32)
        assert self.out_c.funcs['fib'].calls('fib')
        assert self.out_c.funcs['fib'].has_any_if_stmts()
        assert self.out_c.funcs['fib'].has_any_return_stmts()

    def test_check_fnction_main(self):
        assert self.out_c.has_func('main')
        main = self.out_c.funcs['main']
        assert main.calls('printf')
        assert main.calls('scanf')
        assert main.calls('fib')
        assert main.has_any_for_loops() or main.has_any_while_loops()
        assert main.has_any_return_stmts()
        assert main.has_return_stmts('return 0')

    def test_check_presence_of_literals(self):
        assert self.out_c.has_string_literal('Input number of iterations: ')
        assert self.out_c.has_string_literal('%d')
        assert self.out_c.has_string_literal('Input number: ')
        assert self.out_c.has_string_literal('fibonacci(%d) = %u\\n')
