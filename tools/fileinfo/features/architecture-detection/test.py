from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='80c39a6f1a657b627e20c7aebd79e7c1'
    )

    def test_fileinfo_detect_powerpc(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['architecture'], 'PowerPC')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'ELF')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][1]['index'], '1')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][1]['name'], '.init')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][23]['index'], '23')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][23]['name'], '.PPC.EMB.apuinfo')
