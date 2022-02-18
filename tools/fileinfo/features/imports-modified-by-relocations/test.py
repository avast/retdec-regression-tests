from regression_tests import *

class PeTest(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='sample.exe_',
        args='--verbose --json'
    )

    def test_correctly_analyzes_imports_and_exports(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['architecture'], 'x86')
        self.assertEqual(self.fileinfo.output['declaredNumberOfDataDirectories'], '16')
        self.assertEqual(self.fileinfo.output['endianness'], 'Little endian')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
        self.assertEqual(self.fileinfo.output['fileStatus'], 'PE32')
        self.assertEqual(self.fileinfo.output['fileType'], 'Executable file')
        self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '203')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['name'], 'GetVolumeInformationW')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['address'], '0x74078')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['libraryName'], 'KERNEL32.dll')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][146]['name'], 'ControlService')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][146]['address'], '0x74000')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][146]['libraryName'], 'ADVAPI32.dll')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][173]['name'], 'CoInitializeEx')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][173]['address'], '0x74340')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][173]['libraryName'], 'ole32.dll')
