from regression_tests import *

class TestX86ClangMacho_ack(Test):
    settings = TestSettings(
        tool='r2plugin',
        input='ack.x86.clang.macho',
        args='--select 0x01e90'
    )

    def test_for_ack(self):
        assert self.out_c.has_just_funcs('_ack')


class TestX86ClangMacho_main(Test):
    settings = TestSettings(
        tool='r2plugin',
        input='ack.x86.clang.macho',
        args='--select 0x1ee0'
    )

    def test_for_main(self):
        assert self.out_c.has_just_funcs('main')


class TestRenameFunction(Test):
    settings = TestSettings(
        tool='r2plugin',
        input='ack.x86.clang.macho',
        commands=(
            's 0x01e90',        # Seek address
            'afn ack_renamed'   # Rename function
        ),
        args='--select 0x01e90'
    )

    def test_ack_is_renamed(self):
        assert self.out_c.has_just_funcs('ack_renamed')


class TestArgs(Test):
    settings = TestSettings(
        tool='r2plugin',
        input='ack.x86.clang.macho',
        commands=(
            's 0x01e90',            # Seek address
            'afvb-*',               # Remove all local vars
            'afn ack',              # Rename function
            'afvb 8 m int32_t',     # Provide stack var m
            'afvb 12 n int32_t',    # Provide stack var n
        ),
        args='--select 0x01e90'
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


class TestArgsCustom(Test):
    settings = TestSettings(
        tool='r2plugin',
        input='ack.x86.clang.macho',
        commands=(
            's 0x01e90',            # Seek address
            'afvb-*',               # Remove all local vars
            'afn ack',              # Rename function
            'afvb 8 xxx int64_t',   # Provide stack var m
            'afvb 12 yyy char',     # Provide stack var n
        ),
        args='--select 0x01e90'
    )

    def test_parameters_are_set(self):
        assert self.out_c.has_just_funcs('ack')
        assert self.out_c.funcs['ack'].param_count == 2
        assert self.out_c.funcs['ack'].params[0].type.is_int(64)
        assert self.out_c.funcs['ack'].params[1].type.is_char()
        assert self.out_c.funcs['ack'].params[0].name == "xxx"
        assert self.out_c.funcs['ack'].params[1].name == "yyy"
        assert self.out_c.funcs['ack'].calls('ack')
        assert self.out_c.funcs['ack'].has_any_if_stmts()


class TestChangeSignature(Test):
    settings = TestSettings(
        tool='r2plugin',
        input='ack.x86.clang.macho',
        commands=(
            's 0x01e90',                                # Seek address
            '"afs int16_t _ack (char a, int64_t b);"'   # Change signature
                                                        # !! quotes required
        ),
        args='--select 0x01e90'
    )

    def test_parameters_are_set(self):
        assert self.out_c.has_just_funcs('_ack')
        assert self.out_c.funcs['_ack'].return_type.is_int(16)
        assert self.out_c.funcs['_ack'].param_count == 2
        assert self.out_c.funcs['_ack'].params[0].type.is_char()
        assert self.out_c.funcs['_ack'].params[1].type.is_int(64)
        assert self.out_c.funcs['_ack'].params[0].name == "a"
        assert self.out_c.funcs['_ack'].params[1].name == "b"


class TestChangeSignatureFP(Test):
    settings = TestSettings(
        tool='r2plugin',
        input='ack.x86.clang.macho',
        commands=(
            's 0x01e90',                                # Seek address
            '"afs float _ack (double a, float b);"'   # Change signature
                                                        # !! quotes required
        ),
        args='--select 0x01e90'
    )

    def test_parameters_are_set(self):
        assert self.out_c.has_just_funcs('_ack')
        assert self.out_c.funcs['_ack'].return_type.is_float()
        assert self.out_c.funcs['_ack'].param_count == 2
        assert self.out_c.funcs['_ack'].params[0].type.is_double()
        assert self.out_c.funcs['_ack'].params[1].type.is_float()
        assert self.out_c.funcs['_ack'].params[0].name == "a"
        assert self.out_c.funcs['_ack'].params[1].name == "b"
