from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='68fbddc22d9ff18619fec578d7f95345'
    )

    def test_all_funcs(self):
        assert self.out_c.has_funcs('entry_point')
        main = self.out_c.funcs['entry_point']
        assert main.return_type.is_int()
