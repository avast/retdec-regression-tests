from regression_tests import *

base_settings_little = TestSettings(
    tool='idaplugin',
    input='ack.mips.gcc.O0.little.ihex',
    idb='ack.mips.gcc.O0.little.idb'
)

class TestDecompileAllLittle(Test):
    settings = TestSettings.from_settings(base_settings_little)

    def test_for_strings(self):
        assert self.out_c.has_string_literal('%d %d')
        assert self.out_c.has_string_literal('ackerman( %d , %d ) = %d\\n')

    def test_call_graph(self):
        main = self.out_c.funcs[ 'sub_8900428' ]
        assert main.calls( 'sub_89005E8' ) # scanf
        assert main.calls( 'sub_8900368' )
        assert main.calls( 'sub_8900510' ) # printf

        ack = self.out_c.funcs[ 'sub_8900368' ]
        assert ack.calls( 'sub_8900368' )

class TestDecompileSelectiveAckLittle(Test):
    settings = TestSettings.from_settings(base_settings_little,
        args='--select 0x8900368'
    )

    def test_ack(self):
        assert self.out_c.has_just_funcs('sub_8900368')
        ack = self.out_c.funcs[ 'sub_8900368' ]
        assert ack.calls( 'sub_8900368' )

base_settings_big = TestSettings(
    tool='idaplugin',
    input='ack.mips.clang.O0.big.ihex',
    idb='ack.mips.clang.O0.big.idb'
)

class TestDecompileAllBig(Test):
    settings = TestSettings.from_settings(base_settings_big)

    def test_call_graph(self):
        main = self.out_c.funcs[ 'sub_4007C4' ]
        assert main.calls( 'sub_400A40' ) # scanf
        assert main.calls( 'sub_4006F0' )
        assert main.calls( 'sub_400A20' ) # printf

        ack = self.out_c.funcs[ 'sub_4006F0' ]
        assert ack.calls( 'sub_4006F0' )

class TestDecompileSelectiveAckBig(Test):
    settings = TestSettings.from_settings(base_settings_big,
        args='--select 0x4006f0'
    )

    def test_ack(self):
        assert self.out_c.has_just_funcs('sub_4006F0')
        ack = self.out_c.funcs[ 'sub_4006F0' ]
        assert ack.calls( 'sub_4006F0' )
