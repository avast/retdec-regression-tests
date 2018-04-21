from regression_tests import *

class NotDotNetButImportMscoreeTest(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=files_in_dir('mscoree-but-not-clr-header')
    )

    def test_fileinfo_json_output_is_correctly_parsed(self):
        assert self.fileinfo.succeeded
        if 'languages' in self.fileinfo.output:
            for language in self.fileinfo.output['languages']:
                self.assertEqual(language['bytecode'], False)
        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
        self.assertTrue(len(self.fileinfo.output['dataDirectories']['dataDirectoryEntries']) >= 15)
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][14]['index'], '14')
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][14]['address'], '0')
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][14]['size'], '0')
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][14]['type'], 'CLR runtime header')

class NotEzirizTest(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=files_in_dir('mscoree-not-and-clr-header-not')
    )

    def test_fileinfo_json_output_is_correctly_parsed(self):
        assert self.fileinfo.succeeded
        assert (self.fileinfo.output.contains('Eziriz .NET Reactor') == False)
        if 'languages' in self.fileinfo.output:
            for language in self.fileinfo.output['languages']:
                self.assertEqual(language['bytecode'], False)
        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
        self.assertEqual(self.fileinfo.output['declaredNumberOfDataDirectories'], '16')
        self.assertEqual(self.fileinfo.output['dataDirectories']['numberOfDataDirectories'], '16')
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][14]['index'], '14')
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][14]['address'], '0')
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][14]['size'], '0')
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][14]['type'], 'CLR runtime header')
