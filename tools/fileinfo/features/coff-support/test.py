from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='ack.o'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['File format'], 'COFF')
        self.assertEqual(self.fileinfo.output['File class'], '32-bit')
        self.assertEqual(self.fileinfo.output['File type'], 'Relocatable file')
        self.assertEqual(self.fileinfo.output['Architecture'], 'x86')
        self.assertEqual(self.fileinfo.output['Endianness'], 'Little endian')
