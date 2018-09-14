from regression_tests import *

class InvalidCoffStringTableTest1(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='rc7.ex'
    )

    def test(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['sectionTable']['numberOfSections'], '20')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][3]['name'], '/4')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][9]['name'], '/14')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][10]['name'], '/29')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][11]['name'], '/41')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][12]['name'], '/55')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][13]['name'], '/67')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][14]['name'], '/80')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][15]['name'], '/91')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][16]['name'], '/102')

class InvalidCoffStringTableTest2(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='NitroTyper_ver_1.3_64_bit.ex'
    )

    def test(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['sectionTable']['numberOfSections'], '18')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][9]['name'], '/4')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][10]['name'], '/19')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][11]['name'], '/31')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][12]['name'], '/45')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][13]['name'], '/57')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][14]['name'], '/70')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][15]['name'], '/81')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][16]['name'], '/92')
