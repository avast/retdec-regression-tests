from regression_tests import *

class TestDecodeOnly(Test):
    settings = TestSettings(
        input='71d5a692b877db86adae65c06de6d49b',
        args='--select-functions main --select-decode-only'
    )

    def test_check_for_selected_function(self):
        assert self.out_c.has_funcs( 'main' )

        fnc = self.out_c.funcs['main']
        assert fnc.calls('function_4d7014')
