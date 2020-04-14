from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='TidyESP.ex'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['File format'], 'PE')
        self.assertEqual(self.fileinfo.output['File class'], '32-bit')
        self.assertEqual(self.fileinfo.output['File type'], 'Executable file')
        self.assertEqual(self.fileinfo.output['Architecture'], 'x86')
        self.assertEqual(self.fileinfo.output['Endianness'], 'Little endian')
        self.assertEqual(self.fileinfo.output['Image base address'], '0x400000')
        self.assertEqual(self.fileinfo.output['Entry point address'], '0x59f695')
        self.assertEqual(self.fileinfo.output['Entry point offset'], '0xcbc95')
        self.assertEqual(self.fileinfo.output['Entry point section name'], '.vmp1')
        self.assertEqual(self.fileinfo.output['Rich header offset'], '0x80')
        self.assertEqual(self.fileinfo.output['Rich header key'], '0x278b8708')
        self.assertEqual(
            self.fileinfo.output['Detected tool'],
            [
                'VMProtect (2.04+) (packer), combined heuristic',
                'Microsoft Linker (12.0) (linker), combined heuristic',
                'Microsoft (linker), dos header style'
            ]
        )
