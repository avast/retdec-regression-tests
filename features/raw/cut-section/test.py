from regression_tests import *

class BasicTest(Test):

    unk_name=''
    ack_name=''
    main_name=''
    scanf_name=''
    printf_name=''

    arg1_name='a1'
    arg2_name='a2'

    def test_function(self):
        assert self.out_c.has_funcs( self.ack_name, self.main_name )
        ack = self.out_c.funcs[ self.ack_name ]
        main = self.out_c.funcs[ self.main_name ]

        assert ack.calls( self.unk_name, self.ack_name )
        assert main.calls( self.scanf_name, self.ack_name, self.printf_name )

class FullTest(BasicTest):

    def test_ack_function(self):
        assert self.out_c.has_funcs( self.ack_name )
        fnc = self.out_c.funcs[ self.ack_name ]

        #assert fnc.return_type.is_int() # x86, elf, {gcc, clang}, does not pass this
        assert fnc.has_params( self.arg1_name, self.arg2_name )
        assert fnc.params[ self.arg1_name ].type.is_int(32)
        assert fnc.params[ self.arg2_name ].type.is_int(32)
        assert fnc.calls( self.unk_name, self.ack_name )

class TestArmClangElf(BasicTest):
    settings = TestSettings(
        input='ack-arm-elf-little-clang-O0.bin.elf-sec.raw',
        mode='raw',
        arch='arm',
        args='-k --endian little --raw-section-vma 0x8470 --raw-entry-point 0x8470'
    )

    unk_name='unknown_844c'
    ack_name='function_85a4'
    main_name='function_8674'
    scanf_name='unknown_8458'
    printf_name='unknown_8428'

class TestArmGccElf(Test):
    settings = TestSettings(
        input='ack-arm-elf-little-gcc-O0.bin.elf-sec.raw',
        mode='raw',
        arch='arm',
        args='-k --endian little --raw-section-vma 0x8470 --raw-entry-point 0x8470'
    )

    unk_name='unknown_844c'
    ack_name='function_85a4'

    def test_ack_function(self):
        assert self.out_c.has_funcs( self.ack_name )
        fnc = self.out_c.funcs[ self.ack_name ]

        assert fnc.calls( self.unk_name, self.ack_name )

'''
class TestArmGccExe(FullTest):
    settings = TestSettings(
        input='ack-arm-pe-little-gcc-O0.bin.exe-sec.raw',
        mode='raw',
        arch='arm',
        args='-k --endian little --raw-section-vma 0x11000 --raw-entry-point 0x11000'
    )

    unk_name='function_1171c'
    ack_name='function_11054'
    main_name='function_11110'
    scanf_name='function_11728'
    printf_name='function_11734'

    arg2_name='result'
'''

class TestMipsClangElf(FullTest):
    settings = TestSettings(
        input='ack-mips-elf-big-clang-O0.bin.elf-sec.raw',
        mode='raw',
        arch='mips',
        args='-k --endian big --raw-section-vma 0x400540 --raw-entry-point 0x400540'
    )

    unk_name='unknown_400aa0'
    ack_name='function_400710'
    main_name='main'
    scanf_name='unknown_400ab0'
    printf_name='unknown_400a80'

class TestMipsGccElf(FullTest):
    settings = TestSettings(
        input='ack-mips-elf-little-gcc-O0.bin.elf-sec.raw',
        mode='raw',
        arch='mips',
        args='-k --endian little --raw-section-vma 0x890003c --raw-entry-point 0x890003c'
    )

    unk_name='rand'
    ack_name='function_8900368'
    main_name='main'
    scanf_name='scanf'
    printf_name='printf'

class TestPic32GccElf(Test):
    settings = TestSettings(
        input='ack-pic32-elf-little-gcc-O0.bin.elf-sec.raw',
        mode='raw',
        arch='pic32',
        args='-k --endian little --raw-section-vma 0x9d002d74 --raw-entry-point 0x9d002d74'
    )

    # These are not 'ack' nor 'main'. Pic32 have then in separate sections '.text.X'.
    # Script cut out '.text' containing some other functions.
    #
    def test_some_random_functions(self):
        assert self.out_c.has_funcs('function_9d0036f0', 'entry_point')

class TestPowerpcClangElf(BasicTest):
    settings = TestSettings(
        input='ack-powerpc-elf-big-clang-O0.bin.elf-sec.raw',
        mode='raw',
        arch='powerpc',
        args='-k --endian big --raw-section-vma 0x10000390 --raw-entry-point 0x10000390'
    )

    unk_name='function_10000810'
    ack_name='function_100004dc'
    main_name='function_100005d4'
    scanf_name='function_10000800'
    printf_name='function_100007f0'

class TestPowerpcGccElf(BasicTest):
    settings = TestSettings(
        input='ack-powerpc-elf-big-gcc-O0.bin.elf-sec.raw',
        mode='raw',
        arch='powerpc',
        args='-k --endian big --raw-section-vma 0x10000390 --raw-entry-point 0x10000390'
    )

    unk_name='function_100007d0'
    ack_name='function_100004dc'
    main_name='function_100005b0'
    scanf_name='function_100007c0'
    printf_name='function_100007b0'

class TestThumbClangElf(Test):
    settings = TestSettings(
        input='ack-thumb-elf-little-clang-O0.bin.elf-sec.raw',
        mode='raw',
        arch='thumb',
        args='-k --endian little --raw-section-vma 0x8470 --raw-entry-point 0x8471'
    )

    unk_name='unknown_844c'
    ack_name='function_85a4'
    main_name='function_8618'
    scanf_name='unknown_8458'
    printf_name='unknown_8428'

    def test_main(self):
        main = self.out_c.funcs[ self.main_name ]
        assert main.calls( self.scanf_name, self.ack_name, self.printf_name )

class TestThumbGccElf(Test):
    settings = TestSettings(
        input='ack-thumb-elf-little-gcc-O0.bin.elf-sec.raw',
        mode='raw',
        arch='thumb',
        args='-k --endian little --raw-section-vma 0x847c --raw-entry-point 0x847d'
    )

    unk_name='unknown_8450'
    ack_name='function_85b0'
    main_name='function_861c' # 'function_8634'
    scanf_name='unknown_8460'
    printf_name='unknown_8428'

    def test_main(self):
        main = self.out_c.funcs[ self.main_name ]
        assert main.calls( self.scanf_name, self.ack_name, self.printf_name )

class TestX86ClangElf(BasicTest):
    settings = TestSettings(
        input='ack-x86-elf-little-clang-O0.bin.elf-sec.raw',
        mode='raw',
        arch='x86',
        args='-k --endian little --raw-section-vma 0x8048410 --raw-entry-point 0x8048410'
    )

    unk_name='unknown_80483f0'
    ack_name='function_8048550'
    main_name='function_8048610'
    scanf_name='unknown_8048400'
    printf_name='unknown_80483c0'

class TestX86ClangExe(FullTest):
    settings = TestSettings(
        input='ack-x86-pe-little-clang-O0.bin.exe-sec.raw',
        mode='raw',
        arch='x86',
        args='-k --endian little --raw-section-vma 0x401000 --raw-entry-point 0x4013ba'
    )

    unk_name='function_407598'
    ack_name='function_401560'
    main_name='function_401600'
    scanf_name='function_4075a0'
    printf_name='function_4075a8'

class TestX86GccElf(BasicTest):
    settings = TestSettings(
        input='ack-x86-elf-little-gcc-O0.bin.elf-sec.raw',
        mode='raw',
        arch='x86',
        args='-k --endian little --raw-section-vma 0x8048410 --raw-entry-point 0x8048410'
    )

    unk_name='unknown_80483f0'
    ack_name='function_804854c'
    main_name='function_80485c0'
    scanf_name='unknown_8048400'
    printf_name='unknown_80483c0'

class TestX86GccExe(FullTest):
    settings = TestSettings(
        input='ack-x86-pe-little-gcc-O0.bin.exe-sec.raw',
        mode='raw',
        arch='x86',
        args='-k --endian little --raw-section-vma 0x401000 --raw-entry-point 0x4013ba'
    )

    unk_name='function_407558'
    ack_name='function_401560'
    main_name='function_4015d4'
    scanf_name='function_407560'
    printf_name='function_407568'
