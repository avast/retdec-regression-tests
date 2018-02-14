
from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='mips-elf-df0691c-modif'
    )

    def test_check_for_entry_point_and_modified_function_name(self):
        self.out_c.has_funcs('entry_point', '_7StringAccumulator4CstrEv')
