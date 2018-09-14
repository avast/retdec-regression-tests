from regression_tests import *

class TestDecodeAll(Test):
    settings = TestSettings(
        input='main.ex',
        args='--select-ranges 0x407740-0x40774d'
    )

    def test_check_for_selected_function(self):
        assert self.out_c.has_just_funcs( 'main' )

        fnc = self.out_c.funcs['main']
        assert fnc.calls('___main')

class TestDecodeOnly(Test):
    settings = TestSettings(
        input='main.ex',
        args='--select-ranges 0x407740-0x40774d --select-decode-only'
    )

    def test_check_for_selected_function(self):
        assert self.out_c.has_funcs( 'main' )

        fnc = self.out_c.funcs['main']
        assert fnc.calls('___main')
