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
        assert self.out_c.has_just_funcs('_ack')

class TestX86GccExe_main(Test):
    settings = TestSettings(
        tool='r2plugin',
        input='ack.x86.clang.macho',
        args='--select 0x1ee0' # main
    )

    def test_for_main(self):
        assert self.out_c.has_just_funcs('main')
