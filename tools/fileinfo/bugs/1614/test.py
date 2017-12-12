from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='991bf8ae92b3e59d41b2365be4edf88c_hydracrypt'
    )

    def test_fileinfo_json_output_correctly_parsed(self):
        assert self.fileinfo.succeeded
        assert (self.fileinfo.output.contains('symbolTable') == False)
        assert (self.fileinfo.output.contains('relocationTable') == False)
        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
        self.assertEqual(self.fileinfo.output['declaredNumberOfDataDirectories'], '16')
        self.assertEqual(self.fileinfo.output['dataDirectories']['numberOfDataDirectories'], '16')
        self.assertEqual(len(self.fileinfo.output['dataDirectories']['dataDirectoryEntries']), 16)
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][5]['index'], '5')
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][5]['address'], '0')
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][5]['size'], '0')
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][5]['type'], 'Relocation table')
