import re

from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input='arm-elf-09923a6e40662aab0ad2a1096f802f08',
        args='--select-functions=LzmaProps_Decode'
    )

    def test_selected_function(self):
        assert self.out_c.has_comment_matching('// Address range: 0x7148 - 0x71b4')
        assert self.out_c.has_just_funcs('LzmaProps_Decode')
        assert self.out_c.contains('v[0-9]+ >= 4 != v[0-9]+ != 4')
        assert self.out_c.contains('v[0-9]+ < .*&g[0-9]+')
        assert self.out_c.contains('v[0-9]+ >= 224 == \(v[0-9]+ != -32\)')
        assert self.out_c.contains('return 4')
