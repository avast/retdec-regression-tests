from regression_tests import *

# original source file: ack.c

class TestIhexPic32GccO0O1(Test):
    settings = TestSettings(
        input=[
            # ack.c -a pic32 -f ihex -c gcc -C -O0 --endian=little
            # RUN: /home/peter/decompiler/gcc-pic32-elf/bin/xc32-gcc /home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/ack.c -o /home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/outputs/TestIhexPic32GccO0O1 (ack.c -a pic32 -f ihex -c gcc -C -O0 --endian=little)/ack.out.c.frontend.elf -std=c99 -O0 -g0  -lm -mprocessor=32MX695F512H -Wl,--defsym=__MPLAB_BUILD=1,--defsym=_min_heap_size=32768,--defsym=_min_stack_size=16384 -DINFINITY=(1.0/0.0) -DNAN=(0.0/0.0) -DPIC32 -I/home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/include
            'ack.pic32.gcc.O0.little.ihex',
            # ack.c -a pic32 -f ihex -c gcc -C -O1 --endian=little
            # RUN: /home/peter/decompiler/gcc-pic32-elf/bin/xc32-gcc /home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/ack.c -o /home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/outputs/TestIhexPic32GccO0O1 (ack.c -a pic32 -f ihex -c gcc -C -O1 --endian=little)/ack.out.c.frontend.elf -std=c99 -O1 -g0  -lm -mprocessor=32MX695F512H -Wl,--defsym=__MPLAB_BUILD=1,--defsym=_min_heap_size=32768,--defsym=_min_stack_size=16384 -DINFINITY=(1.0/0.0) -DNAN=(0.0/0.0) -DPIC32 -I/home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/include
            'ack.pic32.gcc.O1.little.ihex'],
        arch='pic32',
        args='--endian=little'
    )

    def test_for_strings(self):
        assert self.out_c.has_string_literal('%d %d')
        assert self.out_c.has_string_literal('ackerman( %d , %d ) = %d\\n')

    def test_call_graph(self):
        if self.settings.input == 'ack.pic32.gcc.O0.little.ihex':
            main = self.out_c.funcs[ 'function_9d001e0c' ]
            ack = self.out_c.funcs[ 'function_9d001d5c' ]
        elif self.settings.input == 'ack.pic32.gcc.O1.little.ihex':
            main = self.out_c.funcs[ 'function_9d0024b8' ]
            ack = self.out_c.funcs[ 'function_9d002460' ]

        #assert main.calls( 'scanf' )
        assert main.calls( ack )
        assert main.calls( 'printf' )

        assert ack.calls( ack )

class TestIhexMipsClang(Test):
    settings = TestSettings(
        input=[
            # ack.c -a mips -f ihex -c clang -C -O0 --endian=big
            # RUN: /home/peter/decompiler/gcc-llvm-mips-elf/bin/mips-linux-gnu-clang -mips32r2 /home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/ack.c -o /home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/outputs/TestIhexMipsClang (ack.c -a mips -f ihex -c clang -C -O0 --endian=big)/ack.out.c.frontend.elf -std=c99 -O0 -g0  --sysroot=/home/peter/decompiler/gcc-llvm-mips-elf/mips-linux-gnu/libc -lm -I/home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/include
            'ack.mips.clang.O0.big.ihex',
            # ack.c -a mips -f ihex -c clang -C -O1 --endian=big
            # RUN: /home/peter/decompiler/gcc-llvm-mips-elf/bin/mips-linux-gnu-clang -mips32r2 /home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/ack.c -o /home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/outputs/TestIhexMipsClang (ack.c -a mips -f ihex -c clang -C -O1 --endian=big)/ack.out.c.frontend.elf -std=c99 -O1 -g0  --sysroot=/home/peter/decompiler/gcc-llvm-mips-elf/mips-linux-gnu/libc -lm -I/home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/include
            'ack.mips.clang.O1.big.ihex',
            # ack.c -a mips -f ihex -c clang -C -O2 --endian=big
            # RUN: /home/peter/decompiler/gcc-llvm-mips-elf/bin/mips-linux-gnu-clang -mips32r2 /home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/ack.c -o /home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/outputs/TestIhexMipsClang (ack.c -a mips -f ihex -c clang -C -O2 --endian=big)/ack.out.c.frontend.elf -std=c99 -O2 -g0  --sysroot=/home/peter/decompiler/gcc-llvm-mips-elf/mips-linux-gnu/libc -lm -I/home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/include
            'ack.mips.clang.O2.big.ihex',
            # ack.c -a mips -f ihex -c clang -C -O3 --endian=big
            # RUN: /home/peter/decompiler/gcc-llvm-mips-elf/bin/mips-linux-gnu-clang -mips32r2 /home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/ack.c -o /home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/outputs/TestIhexMipsClang (ack.c -a mips -f ihex -c clang -C -O3 --endian=big)/ack.out.c.frontend.elf -std=c99 -O3 -g0  --sysroot=/home/peter/decompiler/gcc-llvm-mips-elf/mips-linux-gnu/libc -lm -I/home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/include
            'ack.mips.clang.O3.big.ihex'],
        arch='mips',
        args='--endian=big'
    )

    def test_call_graph(self):
        main = self.out_c.funcs[ 'main' ]
        ack = self.out_c.funcs[ 'function_4006f0' ]
        if self.settings.input == 'ack.mips.clang.O0.big.ihex':
            scanf = self.out_c.funcs[ 'function_400a40' ]
            printf = self.out_c.funcs[ 'function_400a20' ]
        else:
            scanf = self.out_c.funcs[ 'function_400980' ]
            printf = self.out_c.funcs[ 'function_400960' ]

        assert main.calls( scanf )
        assert main.calls( ack )
        assert main.calls( printf )
        assert ack.calls( ack )

class TestIhexMipsGccO0O1O2(Test):
    settings = TestSettings(
        input=[
            # ack.c -a mips -f ihex -c gcc -C -O0 --endian=little
            # RUN: /home/peter/decompiler/pspsdk/bin/psp-gcc /home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/ack.c -o /home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/outputs/TestIhexMipsGccO0O1O2 (ack.c -a mips -f ihex -c gcc -C -O0 --endian=little)/ack.out.c.frontend.elf -std=c99 -I. -I/home/peter/decompiler/pspsdk/psp/sdk/include -O0 -g0  -G0 -D_PSP_FW_VERSION=150 -L. -L/home/peter/decompiler/pspsdk/psp/sdk/lib -lc -lpspuser -lm -lpspnet_inet -mdouble-float -mfp32 -I/home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/include
            'ack.mips.gcc.O0.little.ihex',
            # ack.c -a mips -f ihex -c gcc -C -O1 --endian=little
            # RUN: /home/peter/decompiler/pspsdk/bin/psp-gcc /home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/ack.c -o /home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/outputs/TestIhexMipsGccO0O1O2 (ack.c -a mips -f ihex -c gcc -C -O1 --endian=little)/ack.out.c.frontend.elf -std=c99 -I. -I/home/peter/decompiler/pspsdk/psp/sdk/include -O1 -g0  -G0 -D_PSP_FW_VERSION=150 -L. -L/home/peter/decompiler/pspsdk/psp/sdk/lib -lc -lpspuser -lm -lpspnet_inet -mdouble-float -mfp32 -I/home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/include
            'ack.mips.gcc.O1.little.ihex',
            # ack.c -a mips -f ihex -c gcc -C -O2 --endian=little
            # RUN: /home/peter/decompiler/pspsdk/bin/psp-gcc /home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/ack.c -o /home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/outputs/TestIhexMipsGccO0O1O2 (ack.c -a mips -f ihex -c gcc -C -O2 --endian=little)/ack.out.c.frontend.elf -std=c99 -I. -I/home/peter/decompiler/pspsdk/psp/sdk/include -O2 -g0  -G0 -D_PSP_FW_VERSION=150 -L. -L/home/peter/decompiler/pspsdk/psp/sdk/lib -lc -lpspuser -lm -lpspnet_inet -mdouble-float -mfp32 -I/home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/include
            'ack.mips.gcc.O2.little.ihex'],
        arch='mips',
        args='--endian=little'
    )

    def test_for_strings(self):
        assert self.out_c.has_string_literal('%d %d')
        assert self.out_c.has_string_literal('ackerman( %d , %d ) = %d\\n')

    def test_call_graph(self):
        if self.settings.input == 'ack.mips.gcc.O0.little.ihex':
            main = self.out_c.funcs[ 'function_8900428' ]
        elif self.settings.input == 'ack.mips.gcc.O1.little.ihex':
            main = self.out_c.funcs[ 'function_89003c4' ]
        elif self.settings.input == 'ack.mips.gcc.O2.little.ihex':
            main = self.out_c.funcs[ 'function_89003c0' ]

        assert main.calls( 'scanf' )
        assert main.calls( 'function_8900368' )
        assert main.calls( 'printf' )

        ack = self.out_c.funcs[ 'function_8900368' ]
        assert ack.calls( 'function_8900368' )

class TestIhexMipsGccO3(Test):
    settings = TestSettings(
        # ack.c -a mips -f ihex -c gcc -C -O3 --endian=little
        # RUN: /home/peter/decompiler/pspsdk/bin/psp-gcc /home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/ack.c -o /home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/outputs/TestIhexMipsGccO3 (ack.c -a mips -f ihex -c gcc -C -O3 --endian=little)/ack.out.c.frontend.elf -std=c99 -I. -I/home/peter/decompiler/pspsdk/psp/sdk/include -O3 -g0  -G0 -D_PSP_FW_VERSION=150 			-L. -L/home/peter/decompiler/pspsdk/psp/sdk/lib -lc -lpspuser -lm -lpspnet_inet -mdouble-float -mfp32 -I/home/peter/decompiler/decompiler/testsuite/regression-tests/integration/current/ack/include
        input='ack.mips.gcc.O3.little.ihex',
        arch='mips',
        args='--endian=little'
    )

    def test_for_functions(self):
        assert self.out_c.has_func( 'entry_point' )
        assert self.out_c.has_func( 'function_8900554' ) # main

    def test_for_strings(self):
        assert self.out_c.has_string_literal('%d %d')
        assert self.out_c.has_string_literal('ackerman( %d , %d ) = %d\\n')

    def test_call_graph(self):
        main = self.out_c.funcs[ 'function_8900554' ]
        assert main.calls( 'scanf' )
        assert main.calls( 'printf' )
