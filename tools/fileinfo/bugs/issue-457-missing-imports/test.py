from regression_tests import *

class Test(Test):
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
