from regression_tests import *


base_settings_x86 = TestSettings(
    tool='idaplugin',
    input='ack-x86-pe-little-gcc-O0.bin.exe-sec.raw',
    idb='ack-x86-pe-little-gcc-O0.bin.exe-sec.idb'
)

class TestDecompileAllX86(Test):
    settings = CriticalTestSettings.from_settings(base_settings_x86)

    def test_call_graph(self):
        main = self.out_c.funcs[ 'sub_4015D4' ]
        assert main.calls( 'sub_407560' ) # scanf
        assert main.calls( 'sub_401560' ) # ack
        assert main.calls( 'sub_407568' ) # printf

        ack = self.out_c.funcs[ 'sub_401560' ]
        assert ack.calls( 'sub_401560' )

class TestDecompileSelectiveAckX86(Test):
    settings = CriticalTestSettings.from_settings(base_settings_x86,
        args='--select 0x401560'
    )

    def test_ack(self):
        assert self.out_c.has_just_funcs('sub_401560')
        ack = self.out_c.funcs[ 'sub_401560' ]
        assert ack.calls( 'sub_401560' )
