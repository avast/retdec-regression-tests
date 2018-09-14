from regression_tests import *

class CorkamiTest(Test):
    settings=TestSettings(
        input=files_in_dir('inputs')
    )

    def test(self):
        assert self.out_c.has_funcs('entry_point')
        assert self.out_c.funcs['entry_point'].calls('printf', 'ExitProcess')
