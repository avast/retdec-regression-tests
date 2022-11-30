from regression_tests import *

class CodeInDataSectionTest(Test):
    settings = TestSettings(input = 'multitext0.ex', arch = 'x86')

    def test_check_for_detected_functions(self):
        assert self.out_c.has_func( 'function_401000' )
        assert self.out_c.has_func( 'entry_point' )
        assert self.out_c.has_func( 'function_403000' )

    def test_contains_string(self):
        assert self.out_c.contains(r'Hello World!')

    def test_check_called_functions(self):
        # assert self.out_c.funcs['function_401000'].calls('GetStdHandle')
        # assert self.out_c.funcs['function_401000'].calls('WriteConsoleA')
        pass
