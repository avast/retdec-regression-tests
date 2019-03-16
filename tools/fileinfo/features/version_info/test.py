from regression_tests import *

# https://github.com/avast-tl/retdec/issues/408
# Test for proper Visual Basic metadata parsing
class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='3e7126c600eb3d73c9b470aa98f2a416',
        args='--verbose --json'
    )

    def test_version_info_languages(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['versionInfo']['languages'][0]['lcid'], 'German - Germany')
        self.assertEqual(self.fileinfo.output['versionInfo']['languages'][0]['codePage'], 'utf-16')
        self.assertEqual(self.fileinfo.output['versionInfo']['languages'][1]['lcid'], 'Unspecified')
        self.assertEqual(self.fileinfo.output['versionInfo']['languages'][1]['codePage'], 'utf-16')

    def test_version_info_strings(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][0]['name'], 'CompanyName')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][0]['value'], 'obama')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][1]['name'], 'LegalCopyright')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][1]['value'], 'copyri')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][2]['name'], 'ProductName')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][2]['value'], 'Projekt1')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][3]['name'], 'FileVersion')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][3]['value'], '3.01.0004')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][4]['name'], 'ProductVersion')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][4]['value'], '3.01.0004')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][5]['name'], 'InternalName')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][5]['value'], 'my_st0re_loader_____')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][6]['name'], 'OriginalFilename')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][6]['value'], 'my_st0re_loader_____.exe')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][7]['name'], 'Comments')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][7]['value'], '')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][8]['name'], 'LegalCopyright')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][8]['value'], '\\xa9\\x00Firefox and Mozilla Developers, according to the MPL 1.1/GPL 2.0/LGPL 2.1 licenses, as applicable.')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][9]['name'], 'CompanyName')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][9]['value'], 'Mozilla Corporation')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][10]['name'], 'FileDescription')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][10]['value'], 'Firefox')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][11]['name'], 'FileVersion')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][11]['value'], '1.9.2.10')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][12]['name'], 'ProductVersion')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][12]['value'], '3.6.10')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][13]['name'], 'InternalName')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][13]['value'], 'Firefox')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][14]['name'], 'LegalTrademarks')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][14]['value'], 'Firefox is a Trademark of The Mozilla Foundation.')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][15]['name'], 'OriginalFilename')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][15]['value'], 'firefox.exe')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][16]['name'], 'ProductName')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][16]['value'], 'Firefox')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][17]['name'], 'BuildID')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][17]['value'], '20100914121323')
