from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='srv_drvr.101'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['File format'], 'ELF')
        self.assertEqual(self.fileinfo.output['File class'], '32-bit')
        self.assertEqual(self.fileinfo.output['File type'], 'Executable file')
        self.assertEqual(self.fileinfo.output['Architecture'], 'IA-64 (Intel Itanium)')
        self.assertEqual(self.fileinfo.output['Endianness'], 'Big endian')
        self.assertEqual(self.fileinfo.output['Entry point address'], '0x31a80')
        self.assertEqual(self.fileinfo.output['Entry point offset'], '0x31a80')
        self.assertEqual(self.fileinfo.output['Entry point section name'], '.text')
        self.assertEqual(self.fileinfo.output['Entry point section index'], '20')
        self.assertEqual(self.fileinfo.output['Detected tool'], 'HP C++ (compiler), section table heuristic')
        self.assertEqual(self.fileinfo.output['Original language'], 'C++')
        self.assertEqual(self.fileinfo.output['Overlay offset'], '0x1c3534')
        self.assertEqual(self.fileinfo.output['Overlay size'], '0x1e')
