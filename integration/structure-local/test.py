from regression_tests import *

class TestBase(Test):
    def test_check_function_fnc_basic_print(self):
        assert self.out_c.has_func('fnc_basic_print')
        assert self.out_c.funcs['fnc_basic_print'].return_type.is_int(32)
        assert self.out_c.funcs['fnc_basic_print'].param_count == 1
        #ssert self.out_c.funcs['fnc_basic_print'].params[0].type.is_pointer()
        #assert self.out_c.funcs['fnc_basic_print'].params[0].type.point_type.is_struct()
        assert self.out_c.funcs['fnc_basic_print'].calls('printf')

    def test_check_function_fnc_basic(self):
        assert self.out_c.has_func('fnc_basic')
        assert self.out_c.funcs['fnc_basic'].return_type.is_void()
        assert self.out_c.funcs['fnc_basic'].param_count == 0
        assert self.out_c.funcs['fnc_basic'].calls('malloc')
        assert self.out_c.funcs['fnc_basic'].calls('scanf')
        assert self.out_c.funcs['fnc_basic'].calls('printf')
        assert self.out_c.funcs['fnc_basic'].calls('fnc_basic_print')

    def test_check_function_fnc_complex_print(self):
        assert self.out_c.funcs['fnc_complex_print'].return_type.is_void()
        #assert self.out_c.funcs['fnc_complex_print'].param_count == 1
        #assert self.out_c.funcs['fnc_complex_print'].params[0].type.is_pointer()
        #assert self.out_c.funcs['fnc_complex_print'].params[0].type.point_type.is_struct()
        assert self.out_c.funcs['fnc_complex_print'].calls('printf')
        assert self.out_c.funcs['fnc_complex_print'].has_any_for_loops() or self.out_c.funcs['fnc_complex_print'].has_any_while_loops()

    def test_check_function_fnc_complex(self):
        assert self.out_c.has_func('fnc_complex')
        assert self.out_c.funcs['fnc_complex'].return_type.is_int(32)
        assert self.out_c.funcs['fnc_complex'].param_count == 0
        assert self.out_c.funcs['fnc_complex'].has_any_for_loops() or self.out_c.funcs['fnc_complex'].has_any_while_loops()
        assert self.out_c.funcs['fnc_complex'].calls('malloc')
        assert self.out_c.funcs['fnc_complex'].has_any_return_stmts()
        #assert self.out_c.funcs['fnc_complex'].has_return_stmts('return 0')

    def test_check_function_fnc_sasa_fill(self):
        assert self.out_c.has_func('fnc_sasa_fill')
        assert self.out_c.funcs['fnc_sasa_fill'].return_type.is_void()
        assert self.out_c.funcs['fnc_sasa_fill'].param_count == 1
        #assert self.out_c.funcs['fnc_sasa_fill'].params[0].type.is_pointer()
        #assert self.out_c.funcs['fnc_sasa_fill'].params[0].type.point_type.is_pointer()
        #assert self.out_c.funcs['fnc_sasa_fill'].params[0].type.point_type.point_type.is_struct()
        #assert self.out_c.funcs['fnc_sasa_fill'].calls('malloc')

    def test_check_function_fnc_sasa_print(self):
        assert self.out_c.has_func('fnc_sasa_print')
        assert self.out_c.funcs['fnc_sasa_print'].return_type.is_void()
        assert self.out_c.funcs['fnc_sasa_print'].param_count == 1
        #assert self.out_c.funcs['fnc_sasa_print'].params[0].type.is_pointer()
        #assert self.out_c.funcs['fnc_sasa_print'].params[0].type.point_type.is_struct()
        assert self.out_c.funcs['fnc_sasa_print'].calls('printf')
        assert self.out_c.funcs['fnc_sasa_print'].has_any_for_loops() or self.out_c.funcs['fnc_sasa_print'].has_any_while_loops()

    def test_check_function_fnc_sasa(self):
        assert self.out_c.has_func('fnc_sasa')
        assert self.out_c.funcs['fnc_sasa'].return_type.is_int(32)
        assert self.out_c.funcs['fnc_sasa'].param_count == 0
        assert self.out_c.funcs['fnc_sasa'].calls('malloc')
        assert self.out_c.funcs['fnc_sasa'].calls('fnc_sasa_fill')
        assert self.out_c.funcs['fnc_sasa'].calls('fnc_sasa_print')
        assert self.out_c.funcs['fnc_sasa'].has_any_return_stmts()
        #assert self.out_c.funcs['fnc_sasa'].has_return_stmts('return 0')

    def test_check_function_main(self):
        assert self.out_c.has_func('main')
        assert self.out_c.funcs['main'].calls('fnc_basic')
        assert self.out_c.funcs['main'].calls('fnc_complex')
        assert self.out_c.funcs['main'].calls('fnc_sasa')
        assert self.out_c.funcs['main'].has_any_return_stmts()
        assert self.out_c.funcs['main'].has_return_stmts('return 0')

    def test_check_presence_of_literals(self):
        #assert self.out_c.has_string_literal("\\n")
        assert self.out_c.has_string_literal("%d\\n")
        assert self.out_c.has_string_literal("%d %d\\n")
        assert self.out_c.has_string_literal("%f %d %d\\n")
        assert self.out_c.has_string_literal("%d %d %f\\n")
        #assert self.out_c.has_string_literal("%c %d %f\\n")
        assert self.out_c.has_string_literal("%d %d %d %f\\n")

class Test_2017(TestBase):
    settings_2017 = TestSettings(
        input=files_in_dir('2017-11-14'),
    )

#class Test_2015(TestBase):
    #settings_2015 = TestSettings(
        #input=files_in_dir('2015-03-30'),
    #)

class TestRun(TestBase):
    def test_produce_expected_output(self):
        if not on_macos():
            self.assert_c_produces_output_when_run(
                input='a 10 3.1415',
                expected_return_code=0,
                expected_output=
'''97 10 3.140000
3.140000 10 97
123 97 3.140000
1 2 3 0.000000
3 4 5 4.140000
5 6 7 8.280001
7 8 9 12.420000
9 10 11 16.560001
123 456

0
55
65

1
65
75

2
75
85

3
85
95

4
95
105

5
105
115

6
115
125

7
125
135

8
135
145

9
145
155
'''
        )

class Test_2018(TestBase):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17'),
    )
