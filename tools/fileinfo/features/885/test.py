from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='6c0fd0902e57aea263056d20fc9c73df'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(
            r'Microsoft Linker \(9.0\)'
        )
        assert self.fileinfo.output.contains(
            r'MSVC \(9.0\) Visual Studio 2008'
        )
        assert self.fileinfo.output.contains(r"C\+\+")
        self.assertEqual(self.fileinfo.output['File class'], '32-bit')
        self.assertEqual(self.fileinfo.output['File format'], 'PE')
        self.assertEqual(self.fileinfo.output['File type'], 'Executable file')
        self.assertEqual(self.fileinfo.output['Architecture'], 'x86')
        self.assertEqual(self.fileinfo.output['Endianness'], 'Little endian')
        self.assertEqual(self.fileinfo.output['Rich header offset'], '0x80')
