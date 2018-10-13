from regression_tests import *

base_settings = TestSettings(
    tool='idaplugin',
    input='msvc-factorial-obj.coff'
)

class TestDecompileAll(Test):
    settings = TestSettings.from_settings(base_settings)

    def test_functions(self):
        assert self.out_c.has_funcs('_factorial') or self.out_c.has_funcs('_factorial_1')

class TestDecompileSelective(Test):
    settings = TestSettings.from_settings(base_settings,
        args='--select 0x0'
    )

    def test_pass(self):
        pass
