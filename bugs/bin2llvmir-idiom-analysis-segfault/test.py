from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='libf021.so',
        args='--select-functions __gnu_satfractqidq --select-decode-only'
    )

    def test_c_contains_only_selected_function(self):
        assert self.out_c.has_just_funcs('__gnu_satfractqidq')

    # Idiom test exchangeBitShiftSDiv1
    # Idiom is applied, but it causes near total body elimination by optimizations.
    #
    #def test_c_does_not_contain_idiom_BitShiftSDiv1(self):
        #assert self.out_c.contains(r'a1 / 2')
