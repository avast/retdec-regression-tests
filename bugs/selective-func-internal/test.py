from regression_tests import *

class Test(Test):
    """Checks that our internal function name can be given as a parameter to

        retdec-decompiler.sh --select-functions

    See #1388 for more details.
    """

    settings = TestSettings(
        input='selective.ex',
        args='--select-functions function_401560'
    )

    def test_decompiles_selected_function_with_our_iternal_name(self):
        assert self.out_c.has_just_funcs('function_401560')
        assert not self.out_c.has_comment_matching(r'.* Functions selected to be decompiled but not found: function_401560')
