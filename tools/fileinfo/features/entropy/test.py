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
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['entropy'], '0.653098')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][2]['entropy'], '0.990941')

    def test_overlay_entropy(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['overlay']['entropy'], '0')

class TestELF(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='elf_binary',
        args='--verbose --json'
    )

    def test_section_entropy(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][1]['entropy'], '0.492595')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][2]['entropy'], '0.19516')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][3]['entropy'], '0.523951')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][4]['entropy'], '0.0614047')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][5]['entropy'], '0.0733867')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][6]['entropy'], '0.567219')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][7]['entropy'], '0.0936994')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][8]['entropy'], '0.223194')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][9]['entropy'], '0.173947')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][10]['entropy'], '0.122919')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][11]['entropy'], '0.529546')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][12]['entropy'], '0.381569')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][13]['entropy'], '0.683252')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][14]['entropy'], '0.404863')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][15]['entropy'], '0.426302')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][16]['entropy'], '0.389928')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][17]['entropy'], '0.555075')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][18]['entropy'], '0.13266')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][19]['entropy'], '0.13266')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][20]['entropy'], '0.176947')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][21]['entropy'], '0')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][22]['entropy'], '0.0991956')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][23]['entropy'], '0.0835706')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][24]['entropy'], '0.3125')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][25]['entropy'], '0.470898')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][26]['entropy'], '0.210961')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][27]['entropy'], '0.59874')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][28]['entropy'], '0.532765')

    def test_overlay_entropy(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['overlay']['entropy'], '0.0586244')

class TestMACHO(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='macho_binary',
        args='--verbose --json'
    )

    def test_section_entropy(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['entropy'], '0.464502')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][1]['entropy'], '0.281454')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][2]['entropy'], '0.327149')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][3]['entropy'], '0.377757')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][4]['entropy'], '0.190964')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][5]['entropy'], '0')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][6]['entropy'], '0.1875')

    def test_overlay_entropy(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['overlay']['entropy'], '0.738361')

class TestCOFF(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='coff_binary',
        args='--verbose --json'
    )

    def test_section_entropy(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['entropy'], '0.559017')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][3]['entropy'], '0.444582')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][4]['entropy'], '0.590768')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][5]['entropy'], '0.43337')

    def test_overlay_entropy(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['overlay']['entropy'], '0.458062')