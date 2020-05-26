from regression_tests import *

class TestArgs(Test):
    settings = TestSettings(
        tool='r2plugin',
        input='ack-fastcall.x86.gcc.elf',
        commands=(
            's 0x0804847c',                             # Seek address
            'afc fastcall',                             # Set call convention
            'afs int32_t ack(int32_t m, int32_t n)'     # Set signature
        ),
        args='--select 0x0804847c'
    )

    def test_parameters_are_set(self):
        assert self.out_c.has_just_funcs('ack')
        assert self.out_c.funcs['ack'].param_count == 2
        assert self.out_c.funcs['ack'].params[0].type.is_int(32)
        assert self.out_c.funcs['ack'].params[1].type.is_int(32)
        assert self.out_c.funcs['ack'].params[0].name == "m"
        assert self.out_c.funcs['ack'].params[1].name == "n"
        assert self.out_c.funcs['ack'].calls('ack')
        assert self.out_c.funcs['ack'].has_any_if_stmts()
        assert self.out_c.funcs['ack'].has_any_return_stmts()
