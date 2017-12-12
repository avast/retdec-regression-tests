from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='wappwd'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['File format'], 'ELF')
        self.assertEqual(self.fileinfo.output['File class'], '32-bit')
        self.assertEqual(self.fileinfo.output['Architecture'], 'Unknown machine type (522)')
        self.assertEqual(self.fileinfo.output['Endianness'], 'Little endian')
