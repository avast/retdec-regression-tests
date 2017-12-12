"""Tests recognition of architectures and file formats by fileinfo."""

# IMPORTANT:
#
#   The emitted architectures and file formats are parsed in the decompilation
#   service. If you want to change them, consult this with Petr Zemek.
#

from regression_tests import *

base_settings = TestSettings(
    tool='fileinfo',
    args='--json'
)

class BaseTest(Test):
    def setUp(self):
        assert self.fileinfo.succeeded

class x86_ELF_Test(BaseTest):
    settings = TestSettings.from_settings(base_settings,
        input='x86-elf'
    )

    def test_detects_correct_format_and_architecture(self):
        self.assertEqual(self.fileinfo.output['architecture'], 'x86 (or later and compatible)')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'ELF')

class x86_PE_Test(BaseTest):
    settings = TestSettings.from_settings(base_settings,
        input='x86-pe'
    )

    def test_detects_correct_format_and_architecture(self):
        self.assertEqual(self.fileinfo.output['architecture'], 'x86')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')

class x86_MachO_Test(BaseTest):
    settings = TestSettings.from_settings(base_settings,
        input='x86-macho'
    )

    def test_detects_correct_format_and_architecture(self):
        self.assertEqual(self.fileinfo.output['architecture'], 'x86')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'Mach-O')

class x86_COFF_Test(BaseTest):
    settings = TestSettings.from_settings(base_settings,
        input='x86-coff'
    )

    def test_detects_correct_format_and_architecture(self):
        self.assertEqual(self.fileinfo.output['architecture'], 'x86')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'COFF')

class x86_64_ELF_Test(BaseTest):
    settings = TestSettings.from_settings(base_settings,
        input='x86_64-elf'
    )

    def test_detects_correct_format_and_architecture(self):
        self.assertEqual(self.fileinfo.output['architecture'], 'x86-64')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'ELF')

class x86_64_PE_Test(BaseTest):
    settings = TestSettings.from_settings(base_settings,
        input='x86_64-pe'
    )

    def test_detects_correct_format_and_architecture(self):
        self.assertEqual(self.fileinfo.output['architecture'], 'x86-64')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')

class ARM_ELF_Test(BaseTest):
    settings = TestSettings.from_settings(base_settings,
        input='arm-elf'
    )

    def test_detects_correct_format_and_architecture(self):
        self.assertEqual(self.fileinfo.output['architecture'], 'ARM')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'ELF')

class ARM_PE_Test(BaseTest):
    settings = TestSettings.from_settings(base_settings,
        input='arm-pe'
    )

    def test_detects_correct_format_and_architecture(self):
        self.assertEqual(self.fileinfo.output['architecture'], 'ARM (little endian)')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')

class ARM_MachO_Test(BaseTest):
    settings = TestSettings.from_settings(base_settings,
        input='arm-macho'
    )

    def test_detects_correct_format_and_architecture(self):
        self.assertEqual(self.fileinfo.output['architecture'], 'ARM (little endian)')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'Mach-O')

class Thumb_ELF_Test(BaseTest):
    settings = TestSettings.from_settings(base_settings,
        input='thumb-elf'
    )

    def test_detects_correct_format_and_architecture(self):
        self.assertEqual(self.fileinfo.output['architecture'], 'ARM')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'ELF')

class MIPS_ELF_Test(BaseTest):
    settings = TestSettings.from_settings(base_settings,
        input='mips-elf'
    )

    def test_detects_correct_format_and_architecture(self):
        self.assertEqual(self.fileinfo.output['architecture'], 'MIPS (MIPS I Architecture)')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'ELF')

class PIC32_ELF_Test(BaseTest):
    settings = TestSettings.from_settings(base_settings,
        input='pic32-elf'
    )

    def test_detects_correct_format_and_architecture(self):
        # The architecture is recognized as MIPS, but the detected compiler
        # should give us a hint that it is PIC32.
        self.assertEqual(self.fileinfo.output['architecture'], 'MIPS (MIPS I Architecture)')
        self.assertIn('XC32 GCC', self.fileinfo.output['tools'][0]['name'])
        self.assertEqual(self.fileinfo.output['fileFormat'], 'ELF')

class PowerPC_ELF_Test(BaseTest):
    settings = TestSettings.from_settings(base_settings,
        input='powerpc-elf'
    )

    def test_detects_correct_format_and_architecture(self):
        self.assertEqual(self.fileinfo.output['architecture'], 'PowerPC')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'ELF')

class IntelHEX_Test(BaseTest):
    settings = TestSettings.from_settings(base_settings,
        input='ihex'
    )

    def test_detects_correct_format_and_architecture(self):
        self.assertEqual(self.fileinfo.output['fileFormat'], 'Intel HEX')

class Universal_MachO_Test(BaseTest):
    settings = TestSettings.from_settings(base_settings,
        input='uni-macho'
    )

    def test_detects_correct_format_and_architecture(self):
        self.assertEqual(self.fileinfo.output['fileFormat'], 'Mach-O Universal Binary: [armv7] [arm64]')

class Unknown_PE_Test(BaseTest):
    settings = TestSettings.from_settings(base_settings,
        input='unknown-pe'
    )

    def test_detects_correct_format_and_architecture(self):
        self.assertEqual(self.fileinfo.output['architecture'], 'Unknown machine type (498)')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
