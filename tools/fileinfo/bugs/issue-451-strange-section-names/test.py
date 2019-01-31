from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='4383fe67fec6ea6e44d2c7d075b9693610817edc68e8b2a76b2246b53b9186a1-unpacked'
    )

    def test(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['sectionTable']['numberOfSections'], '13')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['name'], '.text')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][1]['name'], '.data')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][2]['name'], '/4')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][3]['name'], '/18')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][4]['name'], '/30')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][5]['name'], '/43')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][6]['name'], '/59')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][7]['name'], '/75')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][8]['name'], '/94')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][9]['name'], '/106')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][10]['name'], '.idata')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][11]['name'], '.symtab')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][12]['name'], 'gu_idata')
