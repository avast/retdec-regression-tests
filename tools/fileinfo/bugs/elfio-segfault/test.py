from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=['6xvdy6eVA1.in', 'checkShit', 'crackme2', 'libsecuritysdk-2.3.39.so', 'x86-elf-3f0a02183cff2839f3309fe5049e0353', 'x86-elf-f6e6e0624650e679629d51ce660e1f31', 'mips-elf-833b75712348c48d46ed822c1757515a']
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['File format'], 'ELF')
