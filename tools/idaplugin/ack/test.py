from regression_tests import *

inName="ack"

base_settings = TestSettings(
    tool='idaplugin'
)

class CommonTest(Test):
    def test_contains_main(self):
        assert self.out_c.has_funcs('main') or self.out_c.has_funcs('_main')

class TestArmClangElf(CommonTest):
    settings = TestSettings.from_settings(base_settings, input=inName+'.arm.clang-3.2.O0.g.elf' )

class TestArmGccElf(CommonTest):
    settings = TestSettings.from_settings(base_settings, input=inName+'.arm.gnuarmgcc-4.4.1.O0.g.elf' )

class TestArmGccExe(CommonTest):
    settings = TestSettings.from_settings(base_settings, input=inName+'.arm.mingw32ce-4.4.0.O0.g.ex' )

class TestMipsClangElf(CommonTest):
    settings = TestSettings.from_settings(base_settings, input=inName+'.mips.clang-3.2.O0.g.elf' )

class TestMipsGccElf(CommonTest):
    settings = TestSettings.from_settings(base_settings, input=inName+'.mips.pspgcc-4.3.5.O0.g.elf' )

class TestPic32GccElf(CommonTest):
    settings = TestSettings.from_settings(base_settings, input=inName+'.pic32.gcc-4.5.2.O0.g.elf' )

class TestPowerpcGccElf(CommonTest):
    settings = TestSettings.from_settings(base_settings, input=inName+'.powerpc.gcc-4.5.1.O0.g.elf' )

class TestThumbClangElf(CommonTest):
    settings = TestSettings.from_settings(base_settings, input=inName+'.thumb.clang-3.2.O0.g.elf' )

class TestThumbGccElf(CommonTest):
    settings = TestSettings.from_settings(base_settings, input=inName+'.thumb.gnuarmgcc-4.4.1.O0.g.elf' )

class TestX86ClangElf(CommonTest):
    settings = TestSettings.from_settings(base_settings, input=inName+'.x86.clang-3.2.O0.g.elf' )

# Matula: my IDA (not our plugin) throws "Unhandled C++ exception" when loading this file.
# It is unrelated to our plugin because it happens even when I uninstall it.
#
class TestX86ClangExe(CommonTest):
   settings = TestSettings.from_settings(base_settings, input=inName+'.x86.clang-3.2.O0.g.ex' )

class TestX86GccElf(CommonTest):
    settings = TestSettings.from_settings(base_settings, input=inName+'.x86.gcc-4.7.2.O0.g.elf' )

class TestX86GccExe(CommonTest):
    settings = TestSettings.from_settings(base_settings, input=inName+'.x86.mingw32-gcc-4.7.3.O0.g.ex' )

class TestX86ClangMacho(CommonTest):
    settings = TestSettings.from_settings(base_settings, input=inName+'.x86.clang.macho' )

class TestX86GccExe__main(Test):
    """Keep statically linked function in selected IDA decompilation.
       Do not even run static code recognition.
    """

    settings = TestSettings.from_settings(base_settings,
        input=inName+'.x86.mingw32-gcc-4.7.3.O0.g.ex',
        args='--select 0x4023E0'
    )

    def test_for__main(self):
        assert self.out_c.has_just_funcs('sub_4023E0') or self.out_c.has_just_funcs('___main')

class TestX86GccExe0x402400(Test):
    """Keep statically linked function in selected IDA decompilation.
       Do not even run static code recognition.
    """

    settings = TestSettings.from_settings(base_settings,
        input=inName+'.x86.mingw32-gcc-4.7.3.O0.g.ex',
        args='--select 0x402400'
    )

    def test_for___security_init_cookie(self):
        assert self.out_c.has_just_funcs('___security_init_cookie')

class TestX86ClangMacho__ack(Test):
    settings = TestSettings.from_settings(base_settings,
        input=inName+'.x86.clang.macho',
        args='--select 0x1e90'
    )

    def test_for__ack(self):
        assert self.out_c.has_just_funcs('_ack')
        fnc = self.out_c.funcs['_ack']
        assert fnc.calls('_ack')

class TestX86GccElf_EA64(CommonTest):
    settings = TestSettings.from_settings(base_settings,
        input=inName+'.x86.gcc-4.7.2.O0.g.elf',
        args='--ea64'
    )

class TestX64GccElf_EA64_full(CommonTest):
    settings = TestSettings.from_settings(base_settings,
        input=inName+'.x64.gcc.O0.g.elf',
        args='--ea64'
    )

class TestX64GccElf_EA64_selective(Test):
    settings = TestSettings.from_settings(base_settings,
        input=inName+'.x64.gcc.O0.g.elf',
        args='--ea64 --select 0x40065C'
    )

    def test_for_ack(self):
        assert self.out_c.has_just_funcs('ack')
        fnc = self.out_c.funcs['ack']
        assert fnc.calls('ack')
