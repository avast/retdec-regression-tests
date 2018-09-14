from regression_tests import *

class CallFromPeHeaderTest(Test):
    settings = TestSettings(
        input='No_bound_import2.ex',
    )

    def test_call_from_pe_header_entry_point(self):
        assert self.out_c.has_funcs('function_401000')
        assert self.out_c.funcs['function_401000'].calls('MessageBoxA')

class SmallOffsetTest(Test):
    settings = TestSettings(
        input='app4.ex',
    )

    def test_small_offset_decompilation(self):
        assert self.out_c.has_funcs('entry_point', 'function_4000dc')
        assert self.out_c.funcs['entry_point'].calls('DialogBoxIndirectParamA')
        assert self.out_c.funcs['function_4000dc'].calls('GetForegroundWindow', 'ShowWindow',
        'RegisterHotKey', 'UnregisterHotKey', 'EndDialog')

class SectionsWithNoSizeTest(Test):
    settings = TestSettings(
        input='ETricks.ex',
    )

    def test_import_calls(self):
        assert self.out_dsm.contains('0x401033:.*call 0x4010ad <MessageBeep>')
        assert self.out_dsm.contains('0x40103a:.*call 0x4010a7 <ExitProcess>')

    def test_import_detections(self):
        assert self.out_dsm.contains('0x4010a7:.*jmp dword ptr \[0x40403c\] <ExitProcess>')
        assert self.out_dsm.contains('0x4010ad:.*jmp dword ptr \[0x404044\] <MessageBeep>')

class TinyImportsTest(Test):
    settings = TestSettings(
        input='imports_tinyW7.ex'
    )

    def test_tiny_imports(self):
        assert self.out_c.has_funcs('entry_point')
        assert self.out_c.funcs['entry_point'].calls('printf', 'ExitProcess')
        assert self.out_c.has_string_literal(r' * tiny imports (W7)\n')

class DataInCodeTest(Test):
    settings = TestSettings(
        input='appendeddata.ex'
    )

    def test_data_in_code(self):
        assert self.out_c.has_funcs('entry_point')
        assert self.out_c.funcs['entry_point'].calls('printf', 'ExitProcess')
        assert self.out_c.has_string_literal(r' * appended data\n')

class ResourcesTest(Test):
    settings = TestSettings(
        input='resource2.ex'
    )

    def test_resources(self):
        assert self.out_c.has_funcs('entry_point')
        assert self.out_c.funcs['entry_point'].calls('FindResourceA', 'LoadResource', 'ExitProcess')
        assert self.out_c.has_string_literal(r'#7354')
        assert self.out_c.has_string_literal(r'#315')
