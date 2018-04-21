from regression_tests import *

class Eziriz42Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=['x86-pe-ff10e014c94cbc89f9e653bc647b6d5a', 'x86-pe-d5a674ff381b95f36f3f4ef3e5a8d0c4-eziriz42']
    )

    def test_fileinfo_json_output_is_correctly_parsed(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
        self.assertEqual(self.fileinfo.output['dataDirectories']['numberOfDataDirectories'], '16')
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][14]['index'], '14')
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][14]['address'], '0')
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][14]['size'], '0')
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][14]['type'], 'CLR runtime header')
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'Eziriz .NET Reactor')
        self.assertEqual(self.fileinfo.output['tools'][0]['version'], '4.2')
        self.assertEqual(self.fileinfo.output['languages'][0]['name'], 'CIL/.NET')
        self.assertTrue(self.fileinfo.output['languages'][0]['bytecode'])

class Eziriz50Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='x86-pe-08f9c6c1cfb53ece69025050c95fcd5e-eziriz5'
    )

    def test_fileinfo_json_output_is_correctly_parsed(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
        self.assertEqual(self.fileinfo.output['dataDirectories']['numberOfDataDirectories'], '15')
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][14]['index'], '14')
        self.assertTrue(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][14]['address'] != 0)
        self.assertTrue(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][14]['size'] != 0)
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][14]['type'], 'CLR runtime header')
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'Eziriz .NET Reactor')
        self.assertEqual(self.fileinfo.output['tools'][0]['version'], '4.8 - 5.0')
        self.assertEqual(self.fileinfo.output['languages'][0]['name'], 'CIL/.NET')
        self.assertTrue(self.fileinfo.output['languages'][0]['bytecode'])
