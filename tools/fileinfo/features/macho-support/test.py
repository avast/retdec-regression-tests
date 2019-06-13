from regression_tests import *

# Little endian 64-bit dynamic library
class TestMachoDynamicLE(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='macho_x86_64.dylib',
        args='--json --verbose'
    )

    def setUp(self):
        assert self.fileinfo.succeeded

    def test_analyze_basic_info(self):
        self.assertEqual(self.fileinfo.output['fileFormat'], 'Mach-O')
        self.assertEqual(self.fileinfo.output['fileClass'], '64-bit')
        self.assertEqual(self.fileinfo.output['fileType'], 'Dynamic library')
        self.assertEqual(self.fileinfo.output['architecture'], 'x86-64')
        self.assertEqual(self.fileinfo.output['endianness'], 'Little endian')

    def test_analyze_segments_sections(self):
        self.assertEqual(self.fileinfo.output['declaredNumberOfSegments'], '2')
        self.assertEqual(self.fileinfo.output['declaredNumberOfSections'], '3')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['name'], '__text')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['address'], '0xf50')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['offset'], '0xf50')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][1]['name'], '__unwind_info')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][2]['name'], '__eh_frame')

    def test_analyze_exports(self):
        self.assertEqual(self.fileinfo.output['exportTable']['numberOfExports'], '1')
        self.assertEqual(self.fileinfo.output['exportTable']['exports'][0]['address'], '0xf50')
        self.assertEqual(self.fileinfo.output['exportTable']['exports'][0]['index'], '0')
        self.assertEqual(self.fileinfo.output['exportTable']['exports'][0]['name'], '__Z9factoriali')

# Big endian 64-bit relocatable binary
class TestMachoObjBE(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='macho_ppc64.o',
        args='--json --verbose'
    )

    def setUp(self):
        assert self.fileinfo.succeeded

    def test_analyze_basic_info(self):
        self.assertEqual(self.fileinfo.output['fileFormat'], 'Mach-O')
        self.assertEqual(self.fileinfo.output['fileClass'], '64-bit')
        self.assertEqual(self.fileinfo.output['fileType'], 'Relocatable file')
        self.assertEqual(self.fileinfo.output['architecture'], 'PowerPC (big endian, 64-bit mode)')
        self.assertEqual(self.fileinfo.output['endianness'], 'Big endian')

    def test_analyze_segments(self):
        self.assertEqual(self.fileinfo.output['declaredNumberOfSegments'], '1')
        self.assertEqual(self.fileinfo.output['segmentTable'][0]['index'], '0')
        self.assertEqual(self.fileinfo.output['segmentTable'][0]['offset'], '0x260')
        self.assertEqual(self.fileinfo.output['segmentTable'][0]['sizeInFile'], '0x74')
        self.assertEqual(self.fileinfo.output['segmentTable'][0]['sizeInMemory'], '0x74')
        self.assertEqual(self.fileinfo.output['segmentTable'][0]['virtualAddress'], '0')

    def test_analyze_sections(self):
        self.assertEqual(self.fileinfo.output['declaredNumberOfSections'], '5')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['name'], '__text')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['address'], '0')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['alignmentInMemory'], '0x4')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['index'], '0')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['numberOfRelocationEntries'], '5')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['relocationEntriesOffset'], '0x2d4')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['offset'], '0x260')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['sizeInFile'], '0x3c')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['sizeInMemory'], '0x3c')

    def test_analyze_symbols(self):
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][0]['address'], '0x60')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][0]['associatedSectionIndex'], '2')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][0]['index'], '0')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][0]['name'], '_b')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][1]['name'], '_f')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][2]['name'], '_a')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][3]['name'], '_c')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][4]['name'], '_g')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][5]['associatedSize'], '4')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][5]['name'], 'dyld_stub_binding_helper')

    def test_analyze_exports(self):
        self.assertEqual(self.fileinfo.output['exportTable']['numberOfExports'], '2')
        self.assertEqual(self.fileinfo.output['exportTable']['exports'][0]['address'], '0x60')
        self.assertEqual(self.fileinfo.output['exportTable']['exports'][0]['index'], '0')
        self.assertEqual(self.fileinfo.output['exportTable']['exports'][0]['name'], '_b')
        self.assertEqual(self.fileinfo.output['exportTable']['exports'][1]['name'], '_f')

    def test_analyze_imports(self):
        self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '2')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['address'], '0x6c')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['index'], '0')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['name'], '_g')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['name'], '_c')

    def test_analyze_relocation_tables(self):
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['numberOfRelocations'], '3')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][0]['index'], '0')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][0]['offset'], '0x24')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][0]['type'], '14')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][1]['index'], '1')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][1]['offset'], '0x1c')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][1]['type'], '12')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][2]['index'], '2')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][2]['offset'], '0x18')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][2]['type'], '3')

# Binary with old style entry point command (LC_UNIXTHREAD) and dynamic symbol table (LC_DYSYMTAB)
class TestAckMachoComplete(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='macho_ack',
        args='--json --verbose'
    )

    def setUp(self):
        assert self.fileinfo.succeeded

    def test_analyze_basic_info(self):
        self.assertEqual(self.fileinfo.output['fileFormat'], 'Mach-O')
        self.assertEqual(self.fileinfo.output['fileClass'], '32-bit')
        self.assertEqual(self.fileinfo.output['fileType'], 'Executable file')
        self.assertEqual(self.fileinfo.output['architecture'], 'x86')
        self.assertEqual(self.fileinfo.output['endianness'], 'Little endian')

    # LC_UNIXTHREAD test
    def test_analyze_entry_point_info(self):
        self.assertEqual(self.fileinfo.output['entryPoint']['address'], '0x1e10')
        self.assertEqual(self.fileinfo.output['entryPoint']['offset'], '0xe10')
        self.assertEqual(self.fileinfo.output['entryPoint']['sectionIndex'], '0')
        self.assertEqual(self.fileinfo.output['entryPoint']['sectionName'], '__text')

    def test_analyze_segments(self):
        self.assertEqual(self.fileinfo.output['declaredNumberOfSegments'], '4')
        self.assertEqual(self.fileinfo.output['segmentTable'][0]['index'], '0')
        self.assertEqual(self.fileinfo.output['segmentTable'][0]['offset'], '0')
        self.assertEqual(self.fileinfo.output['segmentTable'][0]['sizeInFile'], '0')
        self.assertEqual(self.fileinfo.output['segmentTable'][0]['sizeInMemory'], '0x1000')
        self.assertEqual(self.fileinfo.output['segmentTable'][0]['virtualAddress'], '0')
        self.assertEqual(self.fileinfo.output['segmentTable'][1]['offset'], '0')
        self.assertEqual(self.fileinfo.output['segmentTable'][1]['sizeInFile'], '0x1000')
        self.assertEqual(self.fileinfo.output['segmentTable'][1]['sizeInMemory'], '0x1000')
        self.assertEqual(self.fileinfo.output['segmentTable'][1]['virtualAddress'], '0x1000')
        self.assertEqual(self.fileinfo.output['segmentTable'][2]['offset'], '0x1000')
        self.assertEqual(self.fileinfo.output['segmentTable'][2]['sizeInFile'], '0x1000')
        self.assertEqual(self.fileinfo.output['segmentTable'][3]['offset'], '0x2000')
        self.assertEqual(self.fileinfo.output['segmentTable'][3]['sizeInFile'], '0x168')

    def test_analyze_sections(self):
        self.assertEqual(self.fileinfo.output['declaredNumberOfSections'], '9')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['name'], '__text')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['address'], '0x1e10')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['alignmentInMemory'], '0x10')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['index'], '0')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['numberOfRelocationEntries'], '0')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['relocationEntriesOffset'], '0')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['offset'], '0xe10')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['sizeInFile'], '0x147')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['sizeInMemory'], '0x147')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][3]['name'], '__cstring')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][6]['name'], '__la_symbol_ptr')

    def test_analyze_symbols(self):
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][0]['address'], '0x1e50')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][0]['associatedSectionIndex'], '0')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][0]['index'], '0')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][0]['name'], 'dyld_stub_binding_helper')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][1]['name'], '__dyld_func_lookup')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][2]['name'], 'dyld__mach_header')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][3]['name'], '_NXArgc')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][4]['name'], '_NXArgv')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][5]['name'], '___progname')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][6]['name'], '__mh_execute_header')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][7]['name'], '_ack')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][8]['name'], '_environ')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][9]['name'], '_main')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][10]['name'], 'start')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][11]['name'], '_exit')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][12]['name'], '_printf')
        self.assertEqual(self.fileinfo.output['symbolTables'][0]['symbols'][13]['name'], '_scanf')

    # LC_DYSYMTAB (imports)
    def test_analyze_exports(self):
        self.assertEqual(self.fileinfo.output['exportTable']['numberOfExports'], '8')
        self.assertEqual(self.fileinfo.output['exportTable']['exports'][0]['address'], '0x202c')
        self.assertEqual(self.fileinfo.output['exportTable']['exports'][0]['index'], '0')
        self.assertEqual(self.fileinfo.output['exportTable']['exports'][0]['name'], '_NXArgc')
        self.assertEqual(self.fileinfo.output['exportTable']['exports'][1]['name'], '_NXArgv')
        self.assertEqual(self.fileinfo.output['exportTable']['exports'][2]['name'], '___progname')
        self.assertEqual(self.fileinfo.output['exportTable']['exports'][3]['name'], '__mh_execute_header')
        self.assertEqual(self.fileinfo.output['exportTable']['exports'][4]['name'], '_ack')
        self.assertEqual(self.fileinfo.output['exportTable']['exports'][5]['name'], '_environ')
        self.assertEqual(self.fileinfo.output['exportTable']['exports'][6]['name'], '_main')
        self.assertEqual(self.fileinfo.output['exportTable']['exports'][7]['name'], 'start')

    # LC_DYSYMTAB test (imports)
    def test_analyze_imports(self):
        self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '3')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['address'], '0x201c')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['index'], '0')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['libraryName'], 'libSystem')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['name'], '_exit')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['name'], '_printf')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][2]['name'], '_scanf')

# Binary file with new style entry point command (LC_LOAD) and dynamic symbol table (LC_DYLD_INFO)
class TestMachoNewStyle(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='macho_x86',
        args='--json --verbose'
    )

    def setUp(self):
        assert self.fileinfo.succeeded

    def test_analyze_basic_info(self):
        self.assertEqual(self.fileinfo.output['fileFormat'], 'Mach-O')
        self.assertEqual(self.fileinfo.output['fileClass'], '32-bit')
        self.assertEqual(self.fileinfo.output['fileType'], 'Executable file')
        self.assertEqual(self.fileinfo.output['architecture'], 'x86')
        self.assertEqual(self.fileinfo.output['endianness'], 'Little endian')

    # LC_MAIN test
    def test_analyze_entry_point_info(self):
        self.assertEqual(self.fileinfo.output['entryPoint']['address'], '0x1f60')
        self.assertEqual(self.fileinfo.output['entryPoint']['offset'], '0xf60')
        self.assertEqual(self.fileinfo.output['entryPoint']['sectionIndex'], '0')
        self.assertEqual(self.fileinfo.output['entryPoint']['sectionName'], '__text')

    # LC_DYLD_INFO test (imports)
    def test_analyze_imports(self):
        self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '2')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['address'], '0x2000')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['index'], '0')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['libraryName'], 'libSystem')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['name'], 'dyld_stub_binder')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['address'], '0x2008')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['index'], '1')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['libraryName'], 'libSystem')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['name'], '_printf')

    # LC_DYLD_INFO test (exports)
    def test_analyze_exports(self):
        self.assertEqual(self.fileinfo.output['exportTable']['numberOfExports'], '2')
        self.assertEqual(self.fileinfo.output['exportTable']['exports'][0]['address'], '0x1000')
        self.assertEqual(self.fileinfo.output['exportTable']['exports'][0]['index'], '0')
        self.assertEqual(self.fileinfo.output['exportTable']['exports'][0]['name'], '__mh_execute_header')
        self.assertEqual(self.fileinfo.output['exportTable']['exports'][1]['address'], '0x1f60')
        self.assertEqual(self.fileinfo.output['exportTable']['exports'][1]['index'], '1')
        self.assertEqual(self.fileinfo.output['exportTable']['exports'][1]['name'], '_main')

class TestMachoARMRelocs(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='macho_reloc_arm32.o',
        args='--json --verbose'
    )

    def test_analyze_relocation_tables(self):
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['numberOfRelocations'], '2')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][0]['index'], '0')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][0]['offset'], '0x28')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][0]['symbolName'], '_test_function')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][0]['type'], '6')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][1]['index'], '1')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][1]['offset'], '0x1e')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][1]['type'], '6')

class TestMachoARMScattRelocs(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='macho_scatt_reloc_arm32.o',
        args='--json --verbose'
    )

    def test_analyze_relocation_tables(self):
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['numberOfRelocations'], '3')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][0]['index'], '0')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][0]['offset'], '0xe')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][0]['symbolName'], '_NSLog')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][0]['type'], '6')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][1]['index'], '1')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][1]['offset'], '0x8')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][1]['type'], '9')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][2]['index'], '2')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][2]['offset'], '0x2')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][2]['type'], '9')

class TestMachox86Relocs(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='macho_reloc_x86.o',
        args='--json --verbose'
    )

    def test_analyze_relocation_tables(self):
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['numberOfRelocations'], '1')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][0]['index'], '0')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][0]['offset'], '0x40')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][0]['symbolName'], '_test_function')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][0]['type'], '0')

class TestMachox64Relocs(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='macho_reloc_x86_64.o',
        args='--json --verbose'
    )

    def test_analyze_relocation_tables(self):
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['numberOfRelocations'], '20')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][18]['index'], '18')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][18]['offset'], '0x115')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][18]['symbolName'], '___dso_handle')
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][18]['type'], '1')

