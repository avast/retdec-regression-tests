from regression_tests import *


class TestX86ClangMacho_ack(Test):
    settings = TestSettings(
        tool='r2plugin',
        input='stack.x64.clang.macho',
        args='--select 0x100000eb0',
        commands=(
            's 0x100000eb0',
            'afn main',
            'afvb -0x14 a int',
            'afvb -0x18 b int',
            'afvb -0x1c c int',
            'afvb -0x20 d int'
        )
    )

    def test_for_ack(self):
        assert self.out_c.has_just_funcs('main')
        assert self.out_c.funcs['main'].calls('_scanf')
        assert self.out_c.funcs['main'].calls('_printf')
        assert self.out_c.funcs['main'].calls('_my_sum1')
        assert self.out_c.funcs['main'].calls('_my_sum2')
        assert self.out_c.funcs['main'].has_local_vars()
        assert self.out_c.funcs['main'].has_any_assignments()
        assert self.out_c.funcs['main'].has_any_if_stmts()
        assert self.out_c.funcs['main'].has_any_return_stmts()
        assert len(self.out_c.funcs['main'].return_stmts) == 1
