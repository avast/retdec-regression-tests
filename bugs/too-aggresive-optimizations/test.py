from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='ppc2',
        arch='powerpc',
        mode='raw',
        args='--raw-entry-point=0x10000000 --raw-section-vma=0x10000000 --endian=big'
    )

    def test_check_for_single_function(self):
        assert self.out_c.has_comment_matching(r'.*Address range: *0x10000000 - 0x10000020')
        fnc = self.out_c.funcs['entry_point']
        assert fnc.has_just_params('result')
        assert fnc.params['result'].type.is_int(32)
        assert self.out_c.contains('return 3') or self.out_c.contains('return result')
        assert self.out_c.contains('a1 = 3') or self.out_c.contains('result = 3')
        assert self.out_c.contains('\*.*\(result \+ 4\) = ')
        assert self.out_c.contains('\*.*\(result \+ 8\) = ')
        assert self.out_c.contains('\*.*\(result \+ 12\) = ')
        assert self.out_c.contains('\*.*\(result \+ 16\) = ')
