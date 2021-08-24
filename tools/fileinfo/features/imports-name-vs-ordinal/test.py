from regression_tests import *

class PeTest32(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='Test32.exe_',
        args='--verbose --json'
    )

    def test_correctly_analyzes_imports_and_exports(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['declaredNumberOfDataDirectories'], '16')
        self.assertEqual(self.fileinfo.output['endianness'], 'Little endian')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
        self.assertEqual(self.fileinfo.output['fileType'], 'Executable file')
        self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '37')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['name'], 'RegOpenKeyExW')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['libraryName'], 'ADVAPI32.dll')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['name'], 'CreateFileW')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['libraryName'], 'KERNEL32.dll')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][15]['name'], '_cexit')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][15]['libraryName'], 'msvcrt.dll')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][30]['name'], 'MessageBeep')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][30]['libraryName'], 'USER32.dll')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][32]['name'], 'MessageBoxA')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][32]['libraryName'], 'USER32.dll')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][33]['ordinalNumber'], '19')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][33]['name'], 'send')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][33]['libraryName'], 'WS2_32.dll')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][34]['ordinalNumber'], '4')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][34]['name'], 'connect')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][34]['libraryName'], 'WS2_32.dll')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][36]['ordinalNumber'], '115')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][36]['name'], 'WSAStartup')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][36]['libraryName'], 'WS2_32.dll')

class PeTest64(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='Test64.exe_',
        args='--verbose --json'
    )

    def test_correctly_analyzes_imports_and_exports(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['declaredNumberOfDataDirectories'], '16')
        self.assertEqual(self.fileinfo.output['endianness'], 'Little endian')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
        self.assertEqual(self.fileinfo.output['fileType'], 'Executable file')
        self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '36')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['name'], 'RegOpenKeyExW')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['libraryName'], 'ADVAPI32.dll')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['name'], 'CreateFileW')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['libraryName'], 'KERNEL32.dll')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][15]['name'], '__getmainargs')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][15]['libraryName'], 'msvcrt.dll')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][30]['name'], 'MessageBeep')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][30]['libraryName'], 'USER32.dll')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][31]['name'], 'MessageBoxA')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][31]['libraryName'], 'USER32.dll')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][33]['ordinalNumber'], '115')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][33]['name'], 'WSAStartup')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][33]['libraryName'], 'WS2_32.dll')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][34]['ordinalNumber'], '4')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][34]['name'], 'connect')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][34]['libraryName'], 'WS2_32.dll')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][35]['ordinalNumber'], '19')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][35]['name'], 'send')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][35]['libraryName'], 'WS2_32.dll')
