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
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['entropy'], '5.22479')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][2]['entropy'], '7.92753')

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
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][1]['entropy'], '3.94076')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][2]['entropy'], '1.56128')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][3]['entropy'], '4.19161')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][4]['entropy'], '0.491237')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][5]['entropy'], '0.587093')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][6]['entropy'], '4.53775')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][7]['entropy'], '0.749595')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][8]['entropy'], '1.78555')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][9]['entropy'], '1.39158')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][10]['entropy'], '0.983356')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][11]['entropy'], '4.23637')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][12]['entropy'], '3.05255')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][13]['entropy'], '5.46602')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][14]['entropy'], '3.2389')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][15]['entropy'], '3.41042')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][16]['entropy'], '3.11942')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][17]['entropy'], '4.4406')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][18]['entropy'], '1.06128')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][19]['entropy'], '1.06128')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][20]['entropy'], '1.41557')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][21]['entropy'], '0')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][22]['entropy'], '0.793564')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][23]['entropy'], '0.668564')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][24]['entropy'], '2.5')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][25]['entropy'], '3.76718')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][26]['entropy'], '1.68769')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][27]['entropy'], '4.78992')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][28]['entropy'], '4.26212')

    def test_overlay_entropy(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['overlay']['entropy'], '0.468996')

class TestMACHO(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='macho_binary',
        args='--verbose --json'
    )

    def test_section_entropy(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['entropy'], '3.71602')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][1]['entropy'], '2.25163')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][2]['entropy'], '2.61719')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][3]['entropy'], '3.02206')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][4]['entropy'], '1.52771')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][5]['entropy'], '0')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][6]['entropy'], '1.5')

    def test_overlay_entropy(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['overlay']['entropy'], '5.90689')

class TestCOFF(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='coff_binary',
        args='--verbose --json'
    )

    def test_section_entropy(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['entropy'], '4.47214')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][3]['entropy'], '3.55666')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][4]['entropy'], '4.72614')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][5]['entropy'], '3.46696')

    def test_overlay_entropy(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['overlay']['entropy'], '3.6645')