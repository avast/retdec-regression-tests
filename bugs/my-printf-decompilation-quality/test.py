
from regression_tests import *

if not on_macos():
    class Test(Test):
        settings = TestSettings(
            input='x86-c96c707952ce5bf3334f97c3e76afba6'
        )

        def test_my_printf_calls_known_functions(self):
            self.out_c.has_funcs('my_printf')
            fnc = self.out_c.funcs['my_printf']
            assert fnc.calls('write')
            assert fnc.calls('strlen')
            assert fnc.calls('strchr')
            assert fnc.calls('memcpy')
            assert fnc.calls('memset')
