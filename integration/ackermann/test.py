from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='0 0',
            expected_return_code=0,
            expected_output=
'''Naive:     3 (4 calls)
Iterative: 3 (2 calls)
Formula:   3 (1 calls)
'''
        )
        self.assert_c_produces_output_when_run(
            input='1 1',
            expected_return_code=0,
            expected_output=
'''Naive:     7 (27 calls)
Iterative: 7 (12 calls)
Formula:   7 (1 calls)
'''
        )
        self.assert_c_produces_output_when_run(
            input='2 2',
            expected_return_code=0,
            expected_output=
'''Naive:     61 (2432 calls)
Iterative: 61 (1188 calls)
Formula:   61 (1 calls)
'''
        )
        self.assert_c_produces_output_when_run(
            input='4 1',
            expected_return_code=0,
            expected_output=
'''Naive:     4 (6 calls)
Iterative: 4 (3 calls)
Formula:   4 (1 calls)
'''
        )
        self.assert_c_produces_output_when_run(
            input='6 2',
            expected_return_code=0,
            expected_output=
'''Naive:     61 (2432 calls)
Iterative: 61 (1188 calls)
Formula:   61 (1 calls)
'''
        )

class Test_2018(TestBase):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17', excluding=r'.*\.exe'),
    )

class Test_2018_x64Pe(Test):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17', matching=r'.*\.exe'),
    )

    def test_check_function_naive_ackermann(self):
        assert self.out_c.has_func('naive_ackermann')
        assert self.out_c.funcs['naive_ackermann'].param_count == 2
        assert self.out_c.funcs['naive_ackermann'].params[0].type.is_int(32)
        assert self.out_c.funcs['naive_ackermann'].params[1].type.is_int(32)
        assert not self.out_c.funcs['naive_ackermann'].has_any_while_loops()
        assert self.out_c.funcs['naive_ackermann'].has_any_if_stmts()
        assert self.out_c.funcs['naive_ackermann'].has_any_return_stmts()
        assert self.out_c.funcs['naive_ackermann'].calls('naive_ackermann')

    def test_check_function_iterative_ackermann(self):
        assert self.out_c.has_func('iterative_ackermann')
        assert self.out_c.funcs['iterative_ackermann'].param_count == 2
        assert self.out_c.funcs['iterative_ackermann'].params[0].type.is_int(32)
        assert self.out_c.funcs['iterative_ackermann'].params[1].type.is_int(32)
        assert self.out_c.funcs['iterative_ackermann'].calls('iterative_ackermann')
        assert self.out_c.funcs['iterative_ackermann'].has_any_if_stmts()
        assert self.out_c.funcs['iterative_ackermann'].has_any_while_loops()
        assert self.out_c.funcs['iterative_ackermann'].has_any_return_stmts()


    def test_check_formula_ackermann(self):
        assert self.out_c.has_func('formula_ackermann')
        assert self.out_c.funcs['formula_ackermann'].param_count == 2
        assert self.out_c.funcs['formula_ackermann'].params[0].type.is_int(32)
        assert self.out_c.funcs['formula_ackermann'].params[1].type.is_int(32)
        assert self.out_c.funcs['formula_ackermann'].calls('formula_ackermann')
        assert self.out_c.funcs['formula_ackermann'].has_any_if_stmts()
        assert self.out_c.funcs['formula_ackermann'].has_any_while_loops()
        assert self.out_c.funcs['formula_ackermann'].has_any_return_stmts()

    def test_check_main(self):
        assert self.out_c.has_func('main')
        assert self.out_c.funcs['main'].calls('scanf')
        assert self.out_c.funcs['main'].calls('naive_ackermann')
        assert self.out_c.funcs['main'].calls('iterative_ackermann')
        assert self.out_c.funcs['main'].calls('formula_ackermann')
        assert self.out_c.funcs['main'].calls('printf')
        assert self.out_c.funcs['main'].has_any_return_stmts()
        assert self.out_c.funcs['main'].has_any_assignments()
        assert self.out_c.funcs['main'].has_assignments('calls = 0')
        assert len(self.out_c.funcs['main'].return_stmts) == 1

    def test_check_presence_of_literals(self):
        assert self.out_c.has_string_literal('%d %d')
        assert self.out_c.has_string_literal('Naive:     %u (%u calls)\\n')
        assert self.out_c.has_string_literal('Iterative: %u (%u calls)\\n')
        assert self.out_c.has_string_literal('Formula:   %u (%u calls)\\n')

class Test_2017(TestBase):
    settings_2017 = TestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = TestSettings(
        input=files_in_dir('2015-03-30'),
    )

# Decoder should not decode physical bytes with no virtual counterparts.
class Test_2015_Decoder(Test):
    settings = TestSettings(
        input = '2015-03-30/ackermann.x86.clang-3.2.O0.g.ex'
    )

    def test_decodes_only_valid_range(self):
        assert self.out_dsm.contains('0x407a69:   00 00 00 ff ff ff ff')
        assert not self.out_dsm.contains('0x407a73:   00 00                          \tadd byte [ eax ], al')
