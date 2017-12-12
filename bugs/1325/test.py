from regression_tests import *

base_settings = TestSettings(
    input='main.ex',
)

class TestBase(Test):
    def test_has_no_functions(self):
        assert self.out_c.func_count == 0

class TestDecompileSelectXxxDecodeAll(TestBase):
    settings = CriticalTestSettings.from_settings(base_settings,
        args = '--select-functions xxx'
    )

class TestDecompileSelect0x0DecodeAll(TestBase):
    settings = CriticalTestSettings.from_settings(base_settings,
        args = '--select-ranges 0x0-0x0'
    )

class TestDecompileSelect0x1DecodeAll(TestBase):
    settings = CriticalTestSettings.from_settings(base_settings,
        args = '--select-ranges 0x0-0x1'
    )
    
class TestBaseDecodeOnly(Test):
    def test_decompilation_fails_with_correct_error_message(self):
        self.assertNotEqual(self.decomp.return_code, 0)
        assert self.decomp.log.contains(r'Error: No instructions were decoded')
    
class TestDecompileSelectXxxDecodeOnly(TestBaseDecodeOnly):
    settings = CriticalTestSettings.from_settings(base_settings,
        args = '--select-functions xxx --select-decode-only'
    )
    
    def setUp(self):
        pass
    
class TestDecompileSelect0x0DecodeOnly(TestBaseDecodeOnly):
    settings = CriticalTestSettings.from_settings(base_settings,
        args = '--select-ranges 0x0-0x0 --select-decode-only'
    )
    
    def setUp(self):
        pass
    
class TestDecompileSelect0x1DecodeOnly(TestBaseDecodeOnly):
    settings = CriticalTestSettings.from_settings(base_settings,
        args = '--select-ranges 0x0-0x1 --select-decode-only'
    )
    
    def setUp(self):
        pass
