from regression_tests import *

class DotNetTest(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=files_in_dir('inputs')
    )

    def test_fileinfo_json_output_is_correctly_parsed(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
        self.assertEqual(self.fileinfo.output['dataDirectories']['numberOfDataDirectories'], '16')
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][14]['index'], '14')
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][14]['type'], 'CLR runtime header')
        self.assertTrue(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][14]['address'] != '0')
        self.assertTrue(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][14]['size'] != '0')
        self.assertEqual(self.fileinfo.output['languages'][0]['name'], 'CIL/.NET')
        self.assertTrue(self.fileinfo.output['languages'][0]['bytecode'])

class PackedDotNetTest(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=files_in_dir('packed_inputs')
    )

    def test_fileinfo_json_output_is_correctly_parsed(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
        self.assertEqual(self.fileinfo.output['languages'][0]['name'], 'CIL/.NET')
        self.assertTrue(self.fileinfo.output['languages'][0]['bytecode'])
