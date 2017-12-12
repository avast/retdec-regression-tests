from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='WindowMan.ex',
        args='--verbose --json'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['architecture'], 'x86')
        self.assertEqual(self.fileinfo.output['declaredNumberOfDataDirectories'], '16')
        self.assertEqual(self.fileinfo.output['endianness'], 'Little endian')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
        self.assertEqual(self.fileinfo.output['fileStatus'], 'PE32')
        self.assertEqual(self.fileinfo.output['fileType'], 'Executable file')
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'Microsoft Linker')
        self.assertEqual(self.fileinfo.output['tools'][0]['version'], '6.0')
        self.assertEqual(self.fileinfo.output['tools'][1]['name'], 'MSVC')
        self.assertEqual(self.fileinfo.output['tools'][1]['version'], '6.0')
        self.assertEqual(self.fileinfo.output['resourceTable']['numberOfResources'], '3')
        self.assertEqual(self.fileinfo.output['resourceTable']['resources'][0]['index'], '0')
        self.assertEqual(self.fileinfo.output['resourceTable']['resources'][0]['language'], 'German')
        self.assertEqual(self.fileinfo.output['resourceTable']['resources'][0]['languageId'], '7')
        self.assertEqual(self.fileinfo.output['resourceTable']['resources'][0]['nameId'], '1')
        self.assertEqual(self.fileinfo.output['resourceTable']['resources'][0]['offset'], '0x1488')
        self.assertEqual(self.fileinfo.output['resourceTable']['resources'][0]['size'], '0x8a8')
        self.assertEqual(self.fileinfo.output['resourceTable']['resources'][0]['sublanguageId'], '1')
        self.assertEqual(self.fileinfo.output['resourceTable']['resources'][0]['typeId'], '3')
        self.assertEqual(self.fileinfo.output['resourceTable']['resources'][1]['typeId'], '5')
        self.assertEqual(self.fileinfo.output['resourceTable']['resources'][2]['typeId'], '14')
