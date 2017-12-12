from regression_tests import *

class ArmClangMachoTest(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='arm_clang.macho'
    )

    def test_loader_info(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['loaderInfo']['numberOfSegments'], '7')

    def test_segment_names(self):
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['name'], '__text')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['name'], '__stub_helper')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][2]['name'], '__cstring')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][3]['name'], '__symbolstub1')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][4]['name'], '__lazy_symbol')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][5]['name'], '__nl_symbol_ptr')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][6]['name'], '__LINKEDIT')

    def test_segment_addresses(self):
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['address'], '0xbf98')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['address'], '0xbfbc')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][2]['address'], '0xbfec')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][3]['address'], '0xbffc')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][4]['address'], '0xc000')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][5]['address'], '0xc004')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][6]['address'], '0x10000')

    def test_segment_sizes(self):
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['size'], '0x22')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['size'], '0x30')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][2]['size'], '0xe')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][3]['size'], '0x4')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][4]['size'], '0x4')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][5]['size'], '0x8')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][6]['size'], '0x4000')

class X86ClangMachoTest(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='x86_clang.macho'
    )

    def test_loader_info(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['loaderInfo']['numberOfSegments'], '10')

    def test_segment_names(self):
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['name'], '__text')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['name'], '__symbol_stub')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][2]['name'], '__stub_helper')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][3]['name'], '__cstring')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][4]['name'], '__unwind_info')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][5]['name'], '__dyld')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][6]['name'], '__la_symbol_ptr')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][7]['name'], '__data')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][8]['name'], '__common')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][9]['name'], '__LINKEDIT')

    def test_segment_addresses(self):
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['address'], '0x1ed0')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['address'], '0x1f7e')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][2]['address'], '0x1f8c')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][3]['address'], '0x1fa2')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][4]['address'], '0x1fb0')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][5]['address'], '0x2000')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][6]['address'], '0x201c')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][7]['address'], '0x2024')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][8]['address'], '0x2028')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][9]['address'], '0x3000')

    def test_segment_sizes(self):
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['size'], '0xad')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['size'], '0xc')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][2]['size'], '0x16')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][3]['size'], '0xe')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][4]['size'], '0x48')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][5]['size'], '0x1c')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][6]['size'], '0x8')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][7]['size'], '0x4')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][8]['size'], '0x10')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][9]['size'], '0x1000')

class X64ClangMachoTest(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='x64_clang.macho'
    )

    def test_loader_info(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['loaderInfo']['numberOfSegments'], '10')

    def test_segment_names(self):
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['name'], '__text')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['name'], '__stubs')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][2]['name'], '__stub_helper')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][3]['name'], '__cstring')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][4]['name'], '__unwind_info')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][5]['name'], '__eh_frame')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][6]['name'], '__dyld')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][7]['name'], '__la_symbol_ptr')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][8]['name'], '__common')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][9]['name'], '__LINKEDIT')

    def test_segment_addresses(self):
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['address'], '0x100000eb0')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['address'], '0x100000f3a')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][2]['address'], '0x100000f48')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][3]['address'], '0x100000f60')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][4]['address'], '0x100000f70')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][5]['address'], '0x100000fc0')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][6]['address'], '0x100001000')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][7]['address'], '0x100001038')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][8]['address'], '0x100001048')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][9]['address'], '0x100002000')

    def test_segment_sizes(self):
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['size'], '0x8a')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['size'], '0xc')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][2]['size'], '0x18')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][3]['size'], '0xe')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][4]['size'], '0x50')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][5]['size'], '0x40')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][6]['size'], '0x38')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][7]['size'], '0x10')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][8]['size'], '0x20')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][9]['size'], '0x1000')

class TinyMachoTest(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='tiny.macho'
    )

    def test_loader_info(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['loaderInfo']['numberOfSegments'], '2')

    def test_segment_names(self):
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['name'], '__text')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['name'], '__cstring')

    def test_segment_addresses(self):
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['address'], '0x1000')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['address'], '0x101f')

    def test_segment_sizes(self):
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['size'], '0x1f')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['size'], '0xe')
