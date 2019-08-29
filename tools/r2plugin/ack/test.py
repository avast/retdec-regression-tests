from regression_tests import *

class TestX86GccExe_ack(Test):
    settings = TestSettings(
        tool='r2plugin',
        input='ack.x86.clang.macho',
        args='--select 0x01e90' # ack
    )

    def test_for_ack(self):
        assert self.out_c.has_just_funcs('_ack')


class TestProjFile(Test):
    settings = TestSettings(
        tool='r2plugin',
        input='ack.x86.clang.macho',
        project='ackproj/rc',
        args='--select 0x01e90' # ack
    )

    def test_for_ack(self):
        assert self.out_c.has_just_funcs('ack')
        assert self.out_c.funcs['ack'].param_count == 2
        assert self.out_c.funcs['ack'].params[0].type.is_int(32)
        assert self.out_c.funcs['ack'].params[1].type.is_int(32)
        assert self.out_c.funcs['ack'].params[0].name == "m"
        assert self.out_c.funcs['ack'].params[1].name == "n"
        assert self.out_c.funcs['ack'].calls('ack')
        assert self.out_c.funcs['ack'].has_any_if_stmts()

class TestX86GccExe_main(Test):
    settings = TestSettings(
        tool='r2plugin',
        input='ack.x86.clang.macho',
        args='--select 0x1ee0' # main
    )

    def test_for_main(self):
        assert self.out_c.has_just_funcs('main')
