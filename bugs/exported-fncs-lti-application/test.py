from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='mylib.dll',
    )

    def test_check_scanf_is_user_defined(self):
        assert self.out_c.has_func( '_scanf' )
        main = self.out_c.funcs['_main']
        assert main.calls('_scanf')
