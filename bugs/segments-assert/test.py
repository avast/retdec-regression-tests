from regression_tests import *

class segments_in_elf_x86(Test):
    settings = TestSettings(
        input='x86-elf-f6fecb4c80d6c46e3dce02b0d68fc69f'
    )

    def test_for_reachable_functions(self):
        assert self.out_c.has_func( 'main' )
        assert self.out_c.has_func( 'fib' )

    def test_check_for_all_currently_detected_strings(self):
        assert self.out_c.has_string_literal( 'Input number: ' )
        assert self.out_c.has_string_literal( '%d' )
        assert self.out_c.has_string_literal( 'fibonacci(%d) = %d\\n' )

    def test_check_function_calls(self):
        fnc = self.out_c.funcs[ 'main' ]
        assert fnc.calls( 'printf' )
        assert fnc.calls( 'scanf' )
        assert fnc.calls( 'fib' )
        fnc = self.out_c.funcs[ 'fib' ]
        assert fnc.calls( 'fib' )

class segments_in_elf_mips(Test):
    settings = TestSettings(
        input='mips-elf-01c360d75e6cafe5545402cde25cac8d',
        args='-k'
    )

    # jk: the following functions also matches those detected by IDA
    def test_for_all_functions(self):
        assert self.out_c.has_func( 'entry_point' )
        assert self.out_c.has_func( 'function_0' )
        assert self.out_c.has_func( 'function_88' )
        assert self.out_c.has_func( 'function_264' )
        assert self.out_c.has_func( 'function_26c' )
        assert self.out_c.has_func( 'function_290' )
        assert self.out_c.has_func( 'function_298' )
        assert self.out_c.has_func( 'function_2bc' )
        assert self.out_c.has_func( 'function_2c4' )
        assert self.out_c.has_func( 'function_2e8' )
        assert self.out_c.has_func( 'function_2f0' )
        assert self.out_c.has_func( 'function_314' )
        assert self.out_c.has_func( 'function_31c' )

class segments_in_elf_arm(Test):
    settings = TestSettings(
        input='arm-elf-820c48690f115cbdc4b09c88cd751d75',
        args='-k'
    )

    def test_for_some_functions(self):
        assert self.out_c.has_func( 'main' )
        assert self.out_c.has_func( '_start' )
        assert self.out_c.has_func( 'usage' )
