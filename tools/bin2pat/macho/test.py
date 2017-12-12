from regression_tests import *


class TestBin2PatMachoArm32(Test):
    settings = TestSettings(
        tool='bin2pat',
        input='factorial.arm'
    )

    def test_correctly_creates_rules_count(self):
        assert self.bin2pat.succeeded
        self.assertEqual(len(self.bin2pat.out_yara.rules), 2)

    def test_complete_rule(self):
        rules = self.bin2pat.out_yara.rules
        self.assertEqual(rules['file_0_0']['meta']['name'], '"_factorial"')
        self.assertEqual(rules['file_0_0']['meta']['bitWidth'], '32')
        self.assertEqual(rules['file_0_0']['meta']['endianness'], '"little"')
        self.assertEqual(rules['file_0_0']['meta']['architecture'], '"ARM"')
        self.assertEqual(
            rules['file_0_0']['strings']['$1'],
            "{ 80 B5 6F 46 83 B0 01 90 01 98 02 28 02 D2 01 20 02 90 09 E0 01"
            " 98 01 99 01 39 00 90 08 46 ?? ?? ?? ?? 00 99 48 43 02 90 02 98"
            " 03 B0 80 BD }"
        )
        self.assertEqual(rules['file_0_0']['conditions'], ['$1'])

    def test_rules_names_patterns_only(self):
        rules = self.bin2pat.out_yara.rules
        self.assertEqual(rules['file_0_1']['meta']['name'], '"_function"')
        self.assertEqual(
            rules['file_0_1']['strings']['$1'],
            "{ 80 B5 6F 46 ?? ?? ?? ?? ?? ?? ?? ?? 78 44 00 68 80 47 ?? ?? ??"
            " ?? 80 BD }"
        )


class TestBin2YaraMachoX86(Test):
    settings = TestSettings(
        tool='bin2pat',
        input='factorial.x86'
    )

    def test_correctly_creates_rules_count(self):
        assert self.bin2pat.succeeded
        self.assertEqual(len(self.bin2pat.out_yara.rules), 2)

    def test_complete_rule(self):
        rules = self.bin2pat.out_yara.rules
        self.assertEqual(rules['file_0_0']['meta']['name'], '"_factorial"')
        self.assertEqual(rules['file_0_0']['meta']['bitWidth'], '32')
        self.assertEqual(rules['file_0_0']['meta']['endianness'], '"little"')
        self.assertEqual(rules['file_0_0']['meta']['architecture'], '"x86"')
        self.assertEqual(
            rules['file_0_0']['strings']['$1'],
            "{ 55 89 E5 83 EC 18 8B 45 08 89 45 F8 83 7D F8 02 0F 83 0C 00 00"
            " 00 C7 45 FC 01 00 00 00 E9 1D 00 00 00 8B 45 F8 8B 4D F8 83 E9"
            " 01 89 0C 24 89 45 F4 E8 CA FF FF FF 8B 4D F4 0F AF C8 89 4D FC"
            " 8B 45 FC 83 C4 18 5D C3 66 0F 1F 84 00 00 00 00 00 }"
        )
        self.assertEqual(rules['file_0_0']['conditions'], ['$1'])

    def test_rules_names_patterns_only(self):
        rules = self.bin2pat.out_yara.rules
        self.assertEqual(rules['file_0_1']['meta']['name'], '"_function"')
        self.assertEqual(
            rules['file_0_1']['meta']['refs'], '"0007 _test_function"'
        )
        self.assertEqual(
            rules['file_0_1']['strings']['$1'],
            "{ 55 89 E5 83 EC 08 E8 ?? ?? ?? ?? 89 04 24 E8 ?? ?? ?? ?? 83 C4"
            " 08 5D C3 }"
        )


class TestBin2YaraMachoPPC64(Test):
    settings = TestSettings(
        tool='bin2pat',
        input='test.ppc64'
    )

    def test_correctly_creates_rules_count(self):
        assert self.bin2pat.succeeded
        self.assertEqual(len(self.bin2pat.out_yara.rules), 1)

    def test_complete_rule(self):
        rules = self.bin2pat.out_yara.rules
        self.assertEqual(rules['file_0_0']['meta']['name'], '"_f"')
        self.assertEqual(rules['file_0_0']['meta']['bitWidth'], '64')
        self.assertEqual(rules['file_0_0']['meta']['endianness'], '"big"')
        self.assertEqual(rules['file_0_0']['meta']['architecture'], '"PowerPC"')
        self.assertEqual(
            rules['file_0_0']['strings']['$1'],
            "{ 7C 08 02 A6 FB E1 FF F8 42 9F 00 05 7F E8 02 A6 F8 01 00 10 F8"
            " 21 FF 81 ?? ?? ?? ?? ?? ?? ?? ?? 38 21 00 80 ?? ?? ?? ?? E8 01"
            " 00 10 EB E1 FF F8 7C 08 03 A6 E8 62 00 02 4E 80 00 20 }"
        )
        self.assertEqual(rules['file_0_0']['conditions'], ['$1'])
