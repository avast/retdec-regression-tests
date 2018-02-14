from regression_tests import *

base_settings = TestSettings(
    tool='idaplugin',
    input='idaplugin.ex',
    idb='idaplugin.idb'
)

class TestDecompileAll(Test):
    settings = CriticalTestSettings.from_settings(base_settings)

    def test_main_comment(self):
        assert self.out_c.contains(r'// Comment:\n//     this is\n//     a main\n//     function\nint32_t _main')

class TestDecompileSelective(Test):
    settings = CriticalTestSettings.from_settings(base_settings,
        args='--select 0x40159a'
    )

    def test_main_comment(self):
        assert self.out_c.contains(r'// Comment:\n//     this is\n//     a main\n//     function<retdec_select>\nint32_t _main')
