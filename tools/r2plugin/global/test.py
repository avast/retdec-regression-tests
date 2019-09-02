from regression_tests import *

class TestX64ClangMacho_global(Test):
    settings = TestSettings(
        tool='r2plugin',
        input='global.x64.clang.macho',
        commands='f globy @0x100001020',    # change name
        args='--select 0x100000ea0'         # select main
    )

    def test_for_main(self):
        assert self.out_c.has_just_funcs('entry0')

    def test_has_global(self):
        assert self.out_c.has_any_global_vars()
        assert self.out_c.has_global_vars('globy')


#class TestGlobalsExported(Test):
#    settings = TestSettings(
#        tool='r2plugin',
#        input='global.x64.clang.macho',
#        args='--select 0x100000ea0'  # ack
#    )
#
#    def test_for_main(self):
#        assert self.out_c.has_just_funcs('entry0')
