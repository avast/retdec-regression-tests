from regression_tests import *

class Test_C(Test):
    settings = TestSettings(
        input=[
            'wide-strings.arm.clang.O0.elf',
            'wide-strings.arm.gcc.O0.elf',
            'wide-strings.mips.clang.O0.elf',
            'wide-strings.mips.gcc.O0.elf',
            'wide-strings.powerpc.clang.O0.elf',
            'wide-strings.powerpc.gcc.O0.elf',
            'wide-strings.thumb.clang.O0.elf',
            'wide-strings.thumb.gcc.O0.elf',
            'wide-strings.x86.clang.O0.elf',
            'wide-strings.x86.gcc.O0.elf',
            'wide-strings.arm.gcc.O0.exe',
            'wide-strings.x86.clang.O0.exe',
            'wide-strings.x86.gcc.O0.exe',
        ]
    )

    def test_check_for_strings(self):
        assert self.out_c.has_string_literal( 'wb' )
        assert self.out_c.has_string_literal( 'd:\\\\1.txt' )
        assert self.out_c.has_string_literal( 'fopen failed!\\n' )
        assert self.out_c.has_string_literal( 'fclose failed!\\n' )

        assert self.out_c.has_string_literal( '' )
        assert self.out_c.has_string_literal( 'ab' )

        str1=r'X \x010d \n'
        str2=r'X \x0000010d \n'
        assert self.out_c.has_string_literal(str1) or self.out_c.has_string_literal(str2)

class Test_bin(Test):
    settings = TestSettings(
        input='85fbb3af105cf46cc07911f37b1ffef3',
        # Decompile only main() because a complete decompilation takes more than
        # two minutes.
        args='--select-functions main'
    )

    def test_check_for_strings(self):
        assert self.out_c.has_string_literal( 'wb' )
        assert self.out_c.has_string_literal( 'd:\\\\1.txt' )
        assert self.out_c.has_string_literal( '_wfopen failed!\\n' )
        assert self.out_c.has_string_literal( 'fclose failed!\\n' )
