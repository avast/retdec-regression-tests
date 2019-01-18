from regression_tests import *

class TestMissingLibsAndFunctions(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='d17d6c07090a26c3368f0aca900d034fd2ccd5e165964c087101540fe634ba89',
        args='--verbose --json'
    )

    def test_for_all_needed_libs(self):
        assert self.fileinfo.succeeded

        type = 'string table offset of name of needed library (dt_needed)'
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][13]['type'], type)
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][13]['description'], 'liblog.so')
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][14]['type'], type)
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][14]['description'], 'libz.so')
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][15]['type'], type)
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][15]['description'], 'libdl.so')
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][16]['type'], type)
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][16]['description'], 'libstdc++.so')
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][17]['type'], type)
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][17]['description'], 'libm.so')
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][18]['type'], type)
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][18]['description'], 'libc.so')

        type = 'string table offset of name of shared object (dt_soname)'
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][19]['type'], type)
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][19]['description'], 'libjiagu.so')

    def test_for_random_imports_missing_before_solving_the_issue(self):
        self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '152')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['name'], '__cxa_finalize')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][14]['name'], 'mmap')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][23]['name'], '__errno')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][35]['name'], 'atoi')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][53]['name'], 'inotify_init')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][72]['name'], 'waitpid')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][88]['name'], 'sigaction')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][100]['name'], 'deflate')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][127]['name'], 'inflateEnd')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][139]['name'], 'getenv')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][151]['name'], '__gnu_Unwind_Find_exidx')

    def test_import_usage_types(self):
        self.assertEqual(self.fileinfo.output['importTable']['imports'][10]['name'], '__stack_chk_guard')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][10]['usageType'], 'OBJECT')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][104]['name'], '_tolower_tab_')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][104]['usageType'], 'OBJECT')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][119]['name'], '_toupper_tab_')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][119]['usageType'], 'OBJECT')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][120]['name'], '_ctype_')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][120]['usageType'], 'OBJECT')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][137]['name'], '__page_size')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][137]['usageType'], 'OBJECT')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][149]['name'], '__sF')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][149]['usageType'], 'OBJECT')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][100]['name'], 'deflate')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][100]['usageType'], 'FUNCTION')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][150]['name'], '__gnu_Unwind_Find_exidx')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][150]['usageType'], 'FUNCTION')

class TestDynamicSegmentToBig(Test):
    """ Dynamic segment in this file is too big - its offset + size > filesize.
        Test that we load it anyway.
    """
    settings = TestSettings(
        tool='fileinfo',
        input='68f8e2fdc6085ea83f51f46cdac7529188061ef6ec83150d8246b765a776a6ba',
        args='--verbose --json'
    )

    def test_for_dynamic_section_entries(self):
        assert self.fileinfo.succeeded

        # first entry
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][0]['type'], 'dt_pltgot')
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][0]['value'], '0xcf28')

        # needed libs entries
        type = 'string table offset of name of needed library (dt_needed)'
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][13]['type'], type)
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][13]['description'], 'libstdc++.so')
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][14]['type'], type)
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][14]['description'], 'libm.so')
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][15]['type'], type)
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][15]['description'], 'libc.so')
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][16]['type'], type)
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][16]['description'], 'libdl.so')

        # last entry
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][25]['type'], 'end of _dynamic array (dt_null)')
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][25]['value'], '0')

    def test_for_random_imports_missing_before_solving_the_issue(self):
        self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '54')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][5]['name'], 'malloc')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][16]['name'], 'exit')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][31]['name'], 'gettimeofday')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][47]['name'], 'raise')

class TestDynamicSectionHeaderIsCut(Test):
    """ There is no valid dynamic segment in this file, only dynamic section.
        Moreover, section's header entry goes beyond filesize - it cannot be read fully.
        Test that we load it anyway.
    """
    settings = TestSettings(
        tool='fileinfo',
        input='f106711ebad010d3e1fa132577c39019c4f61b63dd1e7bd97ee8a41cb4eb5f12',
        args='--verbose --json'
    )

    def test_for_dynamic_section_entries(self):
        assert self.fileinfo.succeeded

        type = 'string table offset of name of needed library (dt_needed)'

        # first
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][0]['type'], 'dt_pltgot')
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][0]['value'], '0xcf28')
        # first/last lib
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][13]['type'], type)
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][13]['description'], 'libstdc++.so')
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][16]['type'], type)
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][16]['description'], 'libdl.so')
        # last
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][25]['type'], 'end of _dynamic array (dt_null)')
        self.assertEqual(self.fileinfo.output['dynamicSections'][0]['dynamicSectionEntries'][25]['value'], '0')

class TestCorruptedSymtabSectionOkDynamicSymtab(Test):
    """ There is a .dynsym section in this file. But it is probably corrupted, because reading it
        gives a bunch of empty symbols.
        There is also symtab entry in dynamic segment that points to a different symtab containing
        few good symbols.
        Test that we read this second symtab.
    """
    settings = TestSettings(
        tool='fileinfo',
        input='c72b6e5980f8ef8269bd37c7b20ba5228a48c917ece56e7e391a084a73649b92',
        args='--verbose --json'
    )

    def test_for_random_imports_missing_before_solving_the_issue(self):
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['name'], '__cxa_finalize')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][6]['name'], 'dlopen')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][12]['name'], 'memset')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][22]['name'], 'fopen')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][27]['name'], 'getenv')

    def test_for_random_symbols_missing_before_solving_the_issue(self):
        self.assertEqual(self.fileinfo.output['symbolTables'][1]['symbols'][1]['name'], '__cxa_finalize')
        self.assertEqual(self.fileinfo.output['symbolTables'][1]['symbols'][7]['name'], 'inflate')
        self.assertEqual(self.fileinfo.output['symbolTables'][1]['symbols'][17]['name'], '__system_property_get')
        self.assertEqual(self.fileinfo.output['symbolTables'][1]['symbols'][28]['name'], 'sscanf')
        self.assertEqual(self.fileinfo.output['symbolTables'][1]['symbols'][31]['name'], 'JNI_OnLoad')
