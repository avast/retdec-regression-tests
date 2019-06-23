from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=[
            '9ea552a98a3056c565cf10a00e806c888ccadd89c350bbc0ef53c5d6d838c8c7',
            'c62efa4dcdb33744ea8f682914eb8ad83fefd5070340bc69609deac287f7bcf5'
        ]
    )

    def test_version_info_is_loaded(self):
        self.assertIsNotNone(self.fileinfo.output['versionInfo'])
        self.assertEqual(len(self.fileinfo.output['versionInfo']['strings']), 8)
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][0]['name'], 'CompanyName')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][0]['value'], 'Hyper Technologies Inc.')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][1]['name'], 'FileDescription')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][1]['value'], 'DeepFreeze4 Project')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][2]['name'], 'FileVersion')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][2]['value'], '4.10.020.0448')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][3]['name'], 'InternalName')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][3]['value'], 'FrzState')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][4]['name'], 'LegalCopyright')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][4]['value'], 'Copyright\\xa9\\x00 1999-2002 Hyper Technologies Inc.')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][5]['name'], 'OriginalFilename')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][5]['value'], 'FrzState.exe')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][6]['name'], 'ProductName')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][6]['value'], 'Deep Freeze')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][7]['name'], 'ProductVersion')
        self.assertEqual(self.fileinfo.output['versionInfo']['strings'][7]['value'], '4.10.020.0448')
