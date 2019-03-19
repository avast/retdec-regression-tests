from regression_tests import *

# Test for binary file section entropies
class TestPE(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='pe_binary',
        args='--verbose --json'
    )

    def test_section_entropy(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['entropy'], '5.225')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][2]['entropy'], '7.928')

    def test_overlay_entropy(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['overlay']['entropy'], '0.000')

class TestELF(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='elf_binary',
        args='--verbose --json'
    )

    def test_section_entropy(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][1]['entropy'], '3.941')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][2]['entropy'], '1.561')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][3]['entropy'], '4.192')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][4]['entropy'], '0.491')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][5]['entropy'], '0.587')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][6]['entropy'], '4.538')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][7]['entropy'], '0.750')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][8]['entropy'], '1.786')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][9]['entropy'], '1.392')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][10]['entropy'], '0.983')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][11]['entropy'], '4.236')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][12]['entropy'], '3.053')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][13]['entropy'], '5.466')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][14]['entropy'], '3.239')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][15]['entropy'], '3.410')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][16]['entropy'], '3.119')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][17]['entropy'], '4.441')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][18]['entropy'], '1.061')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][19]['entropy'], '1.061')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][20]['entropy'], '1.416')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][21]['entropy'], '0.000')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][22]['entropy'], '0.794')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][23]['entropy'], '0.669')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][24]['entropy'], '2.500')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][25]['entropy'], '3.767')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][26]['entropy'], '1.688')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][27]['entropy'], '4.790')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][28]['entropy'], '4.262')

    def test_overlay_entropy(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['overlay']['entropy'], '0.469')

class TestMACHO(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='macho_binary',
        args='--verbose --json'
    )

    def test_section_entropy(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['entropy'], '3.716')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][1]['entropy'], '2.252')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][2]['entropy'], '2.617')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][3]['entropy'], '3.022')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][4]['entropy'], '1.528')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][5]['entropy'], '0.000')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][6]['entropy'], '1.500')

    def test_overlay_entropy(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['overlay']['entropy'], '5.907')

class TestCOFF(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='coff_binary',
        args='--verbose --json'
    )

    def test_section_entropy(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['entropy'], '4.472')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][3]['entropy'], '3.557')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][4]['entropy'], '4.726')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][5]['entropy'], '3.467')

    def test_overlay_entropy(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['overlay']['entropy'], '3.664')