from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='billingsoft.ex'
    )

    def test_fileinfo_json_output_correctly_parsed(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
        self.assertEqual(self.fileinfo.output['dataDirectories']['numberOfDataDirectories'], '16')
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][14]['index'], '14')
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][14]['size'], '0x48')
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][14]['type'], 'CLR runtime header')
        self.assertEqual(self.fileinfo.output['languages'][0]['name'], 'CIL/.NET')
        self.assertTrue(self.fileinfo.output['languages'][0]['bytecode'])
