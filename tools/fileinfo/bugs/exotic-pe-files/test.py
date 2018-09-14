from regression_tests import *

class InvalidNonNullOriginalFirstThunkTest(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='49E5E4256EE2A307DF59A4A3972F60F4.ex'
    )

    def test_invalid_non_null_original_first_thunk(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '32')

class SectionHeadersInOptionalHeaderTest(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='No_bound_import2.ex'
    )

    def test_section_headers_in_optional_header(self):
        assert self.fileinfo.succeeded
        self.assertEqual(len(self.fileinfo.output['sectionTable']['sections']), 1)
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['address'], '0x401000')
        self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '1')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['name'], 'MessageBoxA')

class PeHeaderTruncatedTest(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json',
        input='shutd0wn97.ex'
    )

    def test_pe_header_truncated(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['architecture'], 'x86')
        self.assertEqual(self.fileinfo.output['fileClass'], '32-bit')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
        self.assertEqual(self.fileinfo.output['fileType'], 'Executable file')

class SmallOffsetImportsTest(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='app4.ex'
    )

    def test_small_offset_imports(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '6')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['name'], 'DialogBoxIndirectParamA')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['name'], 'UnregisterHotKey')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][2]['name'], 'EndDialog')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][3]['name'], 'GetForegroundWindow')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][4]['name'], 'ShowWindow')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][5]['name'], 'RegisterHotKey')
