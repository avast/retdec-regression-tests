from regression_tests import *

class Test_arm_elf(Test):
    settings = TestSettings(
        input='hello-arm-elf.o'
    )

    def test_c(self):
        assert self.out_c.has_string_literal('foo')
        assert self.out_c.has_string_literal('bar')
        assert self.out_c.has_string_literal('Hello World!')
        assert self.out_c.has_string_literal('%d %d\\n')

        foo = self.out_c.funcs['foo']
        assert foo.calls('puts')
        #assert foo.calls('sqrt')

        bar = self.out_c.funcs['bar']
        assert bar.calls('puts')

        main = self.out_c.funcs['main']
        assert main.calls('puts')
        assert main.calls('foo')
        assert main.calls('bar')
        assert main.calls('printf')

    def test_dsm(self):
        assert self.out_dsm.contains('; function: foo at 0x0 -- 0x60')
        assert self.out_dsm.contains('; function: bar at 0x64 -- 0x9c')
        assert self.out_dsm.contains('; function: main at 0xa0 -- 0xe4')

class Test_mips_elf(Test):
    settings = TestSettings(
        input='hello-mips-elf.o'
    )

    def test_c(self):
        assert self.out_c.has_string_literal('foo')
        assert self.out_c.has_string_literal('bar')
        assert self.out_c.has_string_literal('Hello World!')
        assert self.out_c.has_string_literal('%d %d\\n')

        foo = self.out_c.funcs['foo']
        assert foo.calls('puts')
        assert foo.calls('sqrt')

        bar = self.out_c.funcs['bar']
        assert bar.calls('puts')

        main = self.out_c.funcs['main']
        assert main.calls('puts')
        assert main.calls('foo')
        assert main.calls('bar')
        assert main.calls('printf')

    def test_dsm(self):
        assert self.out_dsm.contains('; function: foo at 0x0 -- 0x7c')
        assert self.out_dsm.contains('; function: bar at 0x7c -- 0xc8')
        assert self.out_dsm.contains('; function: main at 0xc8 -- 0x140')

class Test_ppc_elf(Test):
    settings = TestSettings(
        input='hello-ppc-elf.o'
    )

    def test_c(self):
        assert self.out_c.has_string_literal('foo')
        #assert self.out_c.has_string_literal('bar')
        assert self.out_c.has_string_literal('Hello World!')
        assert self.out_c.has_string_literal('%d %d\\n')

        foo = self.out_c.funcs['foo']
        assert foo.calls('puts')
        #assert foo.calls('sqrt')

        bar = self.out_c.funcs['bar']
        assert bar.calls('puts')

        main = self.out_c.funcs['main']
        assert main.calls('puts')
        assert main.calls('foo')
        assert main.calls('bar')
        assert main.calls('printf')

    def test_dsm(self):
        assert self.out_dsm.contains('; function: foo at 0x0 -- 0x88')
        assert self.out_dsm.contains('; function: bar at 0x88 -- 0xdc')
        assert self.out_dsm.contains('; function: main at 0xdc -- 0x160')

class Test_x86_elf(Test):
    settings = TestSettings(
        input='hello-x86-elf.o'
    )

    def test_c(self):
        assert self.out_c.has_string_literal('foo')
        assert self.out_c.has_string_literal('bar')
        assert self.out_c.has_string_literal('Hello World!')
        assert self.out_c.has_string_literal('%d %d\\n')

        foo = self.out_c.funcs['foo']
        assert foo.calls('puts')
        assert foo.calls('sqrt')

        bar = self.out_c.funcs['bar']
        assert bar.calls('puts')

        main = self.out_c.funcs['main']
        assert main.calls('puts')
        assert main.calls('foo')
        assert main.calls('bar')
        assert main.calls('printf')

    def test_dsm(self):
        assert self.out_dsm.contains('; function: foo at 0x0 -- 0x28')
        assert self.out_dsm.contains('; function: bar at 0x28 -- 0x42')
        assert self.out_dsm.contains('; function: main at 0x42 -- 0x90')
