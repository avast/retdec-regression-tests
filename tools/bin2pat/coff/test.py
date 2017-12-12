from regression_tests import *


class TestBasicBin2Patx86Minqw(Test):
    settings = TestSettings(
        tool='bin2pat',
        input='mingw_x86.o'
    )

    def test_correctly_creates_rules_count(self):
        assert self.bin2pat.succeeded
        self.assertEqual(len(self.bin2pat.out_yara.rules), 4)

    def test_complete_rule(self):
        # Test all fields of first rule.
        # We will do this complex test only for one rule.
        rules = self.bin2pat.out_yara.rules
        # Meta information.
        self.assertEqual(rules['file_0_0']['meta']['name'], '"_my_strlen"')
        self.assertEqual(rules['file_0_0']['meta']['bitWidth'], '32')
        self.assertEqual(rules['file_0_0']['meta']['endianness'], '"little"')
        self.assertEqual(rules['file_0_0']['meta']['architecture'], '"x86"')
        # Condition. Hexadecimal pattern is broken to multiple lines.
        self.assertEqual(
            rules['file_0_0']['strings']['$1'],
            "{ 55 89 E5 83 EC 10 8B 45 08 89 45 FC EB 04 83 45 FC 01 8B 45 FC"
            " 0F B6 00 84 C0 75 F2 8B 55 FC 8B 45 08 89 D1 29 C1 89 C8 C9 C3 }"
        )
        self.assertEqual(rules['file_0_0']['conditions'], ['$1'])

    def test_rules_names_patterns_only(self):
        rules = self.bin2pat.out_yara.rules
        self.assertEqual(rules['file_0_1']['meta']['name'], '"_factorial"')
        self.assertEqual(
            rules['file_0_1']['strings']['$1'],
            "{ 55 89 E5 83 EC 18 83 7D 08 00 75 07 B8 01 00 00 00 EB 14 8B 45"
            " 08 83 E8 01 89 04 24 E8 DF FF FF FF 8B 55 08 0F AF C2 C9 C3 }"
        )
        self.assertEqual(rules['file_0_2']['meta']['name'], '"_ack"')
        self.assertEqual(
            rules['file_0_2']['strings']['$1'],
            "{ 55 89 E5 83 EC 18 83 7D 08 00 75 08 8B 45 0C 83 C0 01 EB 45 83"
            " 7D 0C 00 75 18 8B 45 08 83 E8 01 C7 44 24 04 01 00 00 00 89 04"
            " 24 E8 D0 FF FF FF EB 27 8B 45 0C 83 E8 01 89 44 24 04 8B 45 08"
            " 89 04 24 E8 B9 FF FF FF 8B 55 08 83 EA 01 89 44 24 04 89 14 24"
            " E8 A7 FF FF FF C9 C3 }"
        )
        self.assertEqual(rules['file_0_3']['meta']['name'], '"_test"')
        self.assertEqual(
            rules['file_0_3']['strings']['$1'],
            "{ 55 89 E5 53 83 EC 14 8B 45 08 89 04 24 E8 6A FF FF FF 89 C3 8B"
            " 55 10 8B 45 0C 89 54 24 04 89 04 24 E8 7F FF FF FF 69 C0 E8 03"
            " 00 00 01 D8 83 C4 14 5B 5D C3 90 90 }"
        )


class TestBasicBin2Patx86Msvc(Test):
    settings = TestSettings(
        tool='bin2pat',
        input='msvc_x86.obj'
    )

    def test_complete_rule(self):
        assert self.bin2pat.succeeded
        rules = self.bin2pat.out_yara.rules
        self.assertEqual(len(rules), 1)
        self.assertEqual(rules['file_0_0']['meta']['name'], '"_factorial"')
        self.assertEqual(rules['file_0_0']['meta']['bitWidth'], '32')
        self.assertEqual(rules['file_0_0']['meta']['endianness'], '"little"')
        self.assertEqual(rules['file_0_0']['meta']['architecture'], '"x86"')
        self.assertEqual(
            rules['file_0_0']['meta']['refs'],
            '"0033 _factorial 004a __RTC_CheckEsp"'
        )
        self.assertEqual(
            rules['file_0_0']['strings']['$1'],
            "{ 55 8B EC 81 EC C0 00 00 00 53 56 57 8D BD 40 FF FF FF B9 30 00"
            " 00 00 B8 CC CC CC CC F3 AB 83 7D 08 00 75 07 B8 01 00 00 00 EB"
            " 13 8B 45 08 83 E8 01 50 E8 ?? ?? ?? ?? 83 C4 04 0F AF 45 08 5F"
            " 5E 5B 81 C4 C0 00 00 00 3B EC E8 ?? ?? ?? ?? 8B E5 5D C3 }"
        )
        self.assertEqual(rules['file_0_0']['conditions'], ['$1'])


class TestBasicBin2Patx64Mingw(Test):
    settings = TestSettings(
        tool='bin2pat',
        input='mingw_x64.o'
    )

    def test_complete_rule(self):
        assert self.bin2pat.succeeded
        rules = self.bin2pat.out_yara.rules
        self.assertEqual(len(rules), 1)
        self.assertEqual(rules['file_0_0']['meta']['name'], '"factorial"')
        self.assertEqual(rules['file_0_0']['meta']['bitWidth'], '64')
        self.assertEqual(rules['file_0_0']['meta']['endianness'], '"little"')
        self.assertEqual(rules['file_0_0']['meta']['architecture'], '"x64"')
        self.assertEqual(
            rules['file_0_0']['strings']['$1'],
            "{ 55 48 89 E5 48 83 EC 20 89 4D 10 83 7D 10 00 75 07 B8 01 00 00"
            " 00 EB 13 8B 45 10 83 E8 01 89 C1 E8 DB FF FF FF 8B 55 10 0F AF"
            " C2 48 83 C4 20 5D C3 90 90 90 90 90 90 90 90 90 90 90 90 90 90"
            " 90 }"
        )
        self.assertEqual(rules['file_0_0']['conditions'], ['$1'])

class TestBasicBin2Patx64Msvc(Test):
    settings = TestSettings(
        tool='bin2pat',
        input='msvc_x64.obj'
    )

    def test_complete_rule(self):
        assert self.bin2pat.succeeded
        rules = self.bin2pat.out_yara.rules
        self.assertEqual(len(rules), 1)
        self.assertEqual(rules['file_0_0']['meta']['name'], '"factorial"')
        self.assertEqual(rules['file_0_0']['meta']['bitWidth'], '64')
        self.assertEqual(rules['file_0_0']['meta']['endianness'], '"little"')
        self.assertEqual(rules['file_0_0']['meta']['architecture'], '"x64"')
        self.assertEqual(rules['file_0_0']['meta']['refs'], '"001f factorial"')
        self.assertEqual(
            rules['file_0_0']['strings']['$1'],
            "{ 89 4C 24 08 48 83 EC 28 83 7C 24 30 00 75 07 B8 01 00 00 00 EB"
            " 16 8B 44 24 30 FF C8 8B C8 E8 ?? ?? ?? ?? 8B 4C 24 30 0F AF C8"
            " 8B C1 48 83 C4 28 C3 }"
        )
        self.assertEqual(rules['file_0_0']['conditions'], ['$1'])

class TestBasicBin2PatArm32Msvc(Test):
    settings = TestSettings(
        tool='bin2pat',
        input='msvc_arm.obj'
    )

    def test_complete_rule(self):
        assert self.bin2pat.succeeded
        rules = self.bin2pat.out_yara.rules
        self.assertEqual(len(rules), 1)
        self.assertEqual(rules['file_0_0']['meta']['name'], '"factorial"')
        self.assertEqual(rules['file_0_0']['meta']['bitWidth'], '32')
        self.assertEqual(rules['file_0_0']['meta']['endianness'], '"little"')
        self.assertEqual(rules['file_0_0']['meta']['architecture'], '"ARM"')
        self.assertEqual(rules['file_0_0']['meta']['refs'], '"001a factorial"')
        self.assertEqual(
            rules['file_0_0']['strings']['$1'],
            "{ 03 B4 2D E9 00 48 EB 46 82 B0 04 9B 00 2B 02 D1 01 23 00 93 09"
            " E0 04 9B 58 1E ?? ?? ?? ?? 01 90 04 9A 01 9B 02 FB 03 F3 00 93"
            " 00 98 02 B0 5D F8 04 BB 5D F8 0C FB }"
        )
        self.assertEqual(rules['file_0_0']['conditions'], ['$1'])
