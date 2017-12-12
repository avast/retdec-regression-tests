from regression_tests import *

class Test1(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json',
        input=[
            'CBlockEAD.gefElf',
            'ssm_boot.out'
        ]
    )

    def test_entry_point_section_is_set(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['entryPoint']['sectionName'], '.text')

class Test2(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='libpn547_fw_08_01_25_prod_plm_32bits.so',
        args='--json'
    )

    def test_fileinfo_warned(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['fileFormat'], 'ELF')
        self.assertTrue(len(self.fileinfo.output['warnings']) >= 1)
        self.assertEqual(self.fileinfo.output['warnings'][0], 'Invalid address of entry point.')
