from regression_tests import *


class TestBasicBin2Patx86(Test):
    settings = TestSettings(
        tool='bin2pat',
        input='x86.o'
    )

    def test_correctly_creates_rules_count(self):
        assert self.bin2pat.succeeded
        self.assertEqual(len(self.bin2pat.out_yara.rules), 4)

    def test_complete_rule(self):
        # Test all fields of first rule.
        # We will do this complex test only for one rule.
        rules = self.bin2pat.out_yara.rules
        # Meta information.
        self.assertEqual(rules['file_0_0']['meta']['name'], '"my_strlen"')
        self.assertEqual(rules['file_0_0']['meta']['size'], '40')
        self.assertEqual(rules['file_0_0']['meta']['bitWidth'], '32')
        self.assertEqual(rules['file_0_0']['meta']['endianness'], '"little"')
        self.assertEqual(rules['file_0_0']['meta']['architecture'], '"x86"')
        # Condition. Hexadecimal pattern is broken to multiple lines.
        self.assertEqual(
            rules['file_0_0']['strings']['$1'],
            "{ 55 89 E5 83 EC 10 8B 45 08 89 45 FC EB 04 83 45 FC 01 8B 45"
            " FC 0F B6 00 84 C0 75 F2 8B 55 FC 8B 45 08 29 C2 89 D0 C9 C3 }"
        )
        self.assertEqual(rules['file_0_0']['conditions'], ['$1'])

    def test_rules_names_patterns_only(self):
        rules = self.bin2pat.out_yara.rules
        self.assertEqual(rules['file_0_1']['meta']['name'], '"factorial"')
        self.assertEqual(rules['file_0_1']['meta']['refs'], '"001e factorial"')
        self.assertEqual(
            rules['file_0_1']['strings']['$1'],
            "{ 55 89 E5 83 EC 08 83 7D 08 00 75 07 B8 01 00 00 00 EB 1A 8B 45"
            " 08 83 E8 01 83 EC 0C 50 E8 ?? ?? ?? ?? 83 C4 10 89 C2 8B 45 08"
            " 0F AF C2 C9 C3 }"
        )
        self.assertEqual(rules['file_0_2']['meta']['name'], '"ack"')
        self.assertEqual(rules['file_0_2']['meta']['refs'], '"0027 ack"')
        self.assertEqual(
            rules['file_0_2']['strings']['$1'],
            "{ 55 89 E5 83 EC 08 83 7D 08 00 75 08 8B 45 0C 83 C0 01 EB 46 83"
            " 7D 0C 00 75 16 8B 45 08 83 E8 01 83 EC 08 6A 01 50 E8 ?? ?? ??"
            " ?? 83 C4 10 EB 2A 8B 45 0C 83 E8 01 83 EC 08 50 FF 75 08 E8 ??"
            " ?? ?? ?? 83 C4 10 89 C2 8B 45 08 83 E8 01 83 EC 08 52 50 E8 ??"
            " ?? ?? ?? 83 C4 10 C9 C3 }"
        )
        self.assertEqual(rules['file_0_3']['meta']['name'], '"test"')
        self.assertEqual(
            rules['file_0_3']['meta']['refs'], '"000e factorial 0023 ack"'
        )
        self.assertEqual(
            rules['file_0_3']['strings']['$1'],
            "{ 55 89 E5 53 83 EC 04 83 EC 0C FF 75 08 E8 ?? ?? ?? ?? 83 C4 10"
            " 89 C3 8B 55 10 8B 45 0C 83 EC 08 52 50 E8 ?? ?? ?? ?? 83 C4 10"
            " 69 C0 E8 03 00 00 01 D8 8B 5D FC C9 C3 }"
        )


class TestBasicBin2Pat64(Test):
    settings = TestSettings(
        tool='bin2pat',
        input='x64.o'
    )

    def test_correctly_creates_rules_count(self):
        assert self.bin2pat.succeeded
        self.assertEqual(len(self.bin2pat.out_yara.rules), 4)

    def test_complete_rule(self):
        rules = self.bin2pat.out_yara.rules
        self.assertEqual(rules['file_0_0']['meta']['name'], '"my_strlen"')
        self.assertEqual(rules['file_0_0']['meta']['bitWidth'], '64')
        self.assertEqual(rules['file_0_0']['meta']['endianness'], '"little"')
        self.assertEqual(rules['file_0_0']['meta']['architecture'], '"x64"')
        self.assertEqual(
            rules['file_0_0']['strings']['$1'],
            "{ 55 48 89 E5 48 89 7D E8 48 8B 45 E8 48 89 45 F8 EB 05 48 83 45"
            " F8 01 48 8B 45 F8 0F B6 00 84 C0 75 F0 48 8B 55 F8 48 8B 45 E8"
            " 48 29 C2 48 89 D0 5D C3 }"
        )
        self.assertEqual(rules['file_0_0']['conditions'], ['$1'])

    def test_rules_names_patterns_only(self):
        rules = self.bin2pat.out_yara.rules
        self.assertEqual(rules['file_0_1']['meta']['name'], '"factorial"')
        self.assertEqual(rules['file_0_1']['meta']['refs'], '"0021 factorial"')
        self.assertEqual(
            rules['file_0_1']['strings']['$1'],
            "{ 55 48 89 E5 48 83 EC 10 89 7D FC 83 7D FC 00 75 07 B8 01 00 00"
            " 00 EB 15 8B 45 FC 83 E8 01 89 C7 E8 ?? ?? ?? ?? 89 C2 8B 45 FC"
            " 0F AF C2 C9 C3 }"
        )
        self.assertEqual(rules['file_0_2']['meta']['name'], '"ack"')
        self.assertEqual(rules['file_0_2']['meta']['refs'], '"0030 ack"')
        self.assertEqual(
            rules['file_0_2']['strings']['$1'],
            "{ 55 48 89 E5 48 83 EC 10 89 7D FC 89 75 F8 83 7D FC 00 75 08 8B"
            " 45 F8 83 C0 01 EB 3D 83 7D F8 00 75 14 8B 45 FC 83 E8 01 BE 01"
            " 00 00 00 89 C7 E8 ?? ?? ?? ?? EB 23 8B 45 F8 8D 50 FF 8B 45 FC"
            " 89 D6 89 C7 E8 ?? ?? ?? ?? 89 C2 8B 45 FC 83 E8 01 89 D6 89 C7"
            " E8 ?? ?? ?? ?? C9 C3 }"
        )
        self.assertEqual(rules['file_0_3']['meta']['name'], '"test"')
        self.assertEqual(
            rules['file_0_3']['meta']['refs'], '"0018 factorial 0029 ack"'
        )
        self.assertEqual(
            rules['file_0_3']['strings']['$1'],
            "{ 55 48 89 E5 53 48 83 EC 18 89 7D EC 89 75 E8 89 55 E4 8B 45 EC"
            " 89 C7 E8 ?? ?? ?? ?? 89 C3 8B 55 E4 8B 45 E8 89 D6 89 C7 E8 ??"
            " ?? ?? ?? 69 C0 E8 03 00 00 01 D8 48 83 C4 18 5B 5D C3 }"
        )


class TestBasicBin2PatMipsBE(Test):
    settings = TestSettings(
        tool='bin2pat',
        input='mips_be.o'
    )

    def test_complete_rule(self):
        assert self.bin2pat.succeeded
        rules = self.bin2pat.out_yara.rules
        self.assertEqual(len(rules), 1)
        self.assertEqual(rules['file_0_0']['meta']['name'], '"my_strlen"')
        self.assertEqual(rules['file_0_0']['meta']['bitWidth'], '32')
        self.assertEqual(rules['file_0_0']['meta']['endianness'], '"big"')
        self.assertEqual(rules['file_0_0']['meta']['architecture'], '"MIPS"')
        self.assertEqual(
            rules['file_0_0']['strings']['$1'],
            "{ 27 BD FF E8 AF BE 00 14 03 A0 F0 21 AF C4 00 18 8F C2 00 18 AF"
            " C2 00 08 0? ?? ?? ?? 00 00 00 00 8F C2 00 08 24 42 00 01 AF C2"
            " 00 08 8F C2 00 08 80 42 00 00 14 40 FF FA 00 00 00 00 8F C3 00"
            " 08 8F C2 00 18 00 62 10 23 03 C0 E8 21 8F BE 00 14 27 BD 00 18"
            " 03 E0 00 08 00 00 00 00 }"
        )


class TestBasicBin2PatMipsLE(Test):
    settings = TestSettings(
        tool='bin2pat',
        input='mips_le.o'
    )

    def test_complete_rule(self):
        assert self.bin2pat.succeeded
        rules = self.bin2pat.out_yara.rules
        self.assertEqual(len(rules), 1)
        self.assertEqual(rules['file_0_0']['meta']['name'], '"ack"')
        self.assertEqual(rules['file_0_0']['meta']['bitWidth'], '32')
        self.assertEqual(rules['file_0_0']['meta']['endianness'], '"little"')
        self.assertEqual(rules['file_0_0']['meta']['architecture'], '"MIPS"')
        self.assertEqual(
            rules['file_0_0']['meta']['refs'], '"0054 ack"'
        )
        self.assertEqual(
            rules['file_0_0']['strings']['$1'],
            "{ D8 FF BD 27 24 00 BF AF 20 00 BE AF 1C 00 B0 AF 21 F0 A0 03 28"
            " 00 C4 AF 2C 00 C5 AF 28 00 C2 8F 05 00 40 14 00 00 00 00 2C 00"
            " C2 8F 01 00 42 24 ?? ?? ?? 0? 00 00 00 00 2C 00 C2 8F 09 00 40"
            " 14 00 00 00 00 28 00 C2 8F FF FF 42 24 21 20 40 00 01 00 05 24"
            " ?? ?? ?? 0? 00 00 00 00 ?? ?? ?? 0? 00 00 00 00 28 00 C2 8F FF"
            " FF 50 24 2C 00 C2 8F FF FF 42 24 28 00 C4 8F 21 28 40 00 ?? ??"
            " ?? 0? 00 00 00 00 21 20 00 02 21 28 40 00 ?? ?? ?? 0? 00 00 00"
            " 00 21 E8 C0 03 24 00 BF 8F 20 00 BE 8F 1C 00 B0 8F 28 00 BD 27"
            " 08 00 E0 03 00 00 00 00 }"
        )


class TestBasicBin2PatPic32(Test):
    settings = TestSettings(
        tool='bin2pat',
        input='pic32.o'
    )

    def test_complete_rule(self):
        assert self.bin2pat.succeeded
        rules = self.bin2pat.out_yara.rules
        self.assertEqual(len(rules), 1)
        self.assertEqual(rules['file_0_0']['meta']['name'], '"factorial"')
        self.assertEqual(rules['file_0_0']['meta']['bitWidth'], '32')
        self.assertEqual(rules['file_0_0']['meta']['endianness'], '"little"')
        self.assertEqual(rules['file_0_0']['meta']['architecture'], '"MIPS"')
        self.assertEqual(rules['file_0_0']['meta']['refs'], '"0038 factorial"')
        self.assertEqual(
            rules['file_0_0']['strings']['$1'],
            "{ E8 FF BD 27 14 00 BF AF 10 00 BE AF 21 F0 A0 03 18 00 C4 AF 18"
            " 00 C2 8F 04 00 40 14 00 00 00 00 01 00 02 24 ?? ?? ?? 0? 00 00"
            " 00 00 18 00 C2 8F FF FF 42 24 21 20 40 00 ?? ?? ?? 0? 00 00 00"
            " 00 21 18 40 00 18 00 C2 8F 02 10 62 70 21 E8 C0 03 14 00 BF 8F"
            " 10 00 BE 8F 18 00 BD 27 08 00 E0 03 00 00 00 00 }"
        )

class TestBasicBin2PatPowerPCBE(Test):
    settings = TestSettings(
        tool='bin2pat',
        input='ppc_be.o'
    )

    def test_complete_rule(self):
        assert self.bin2pat.succeeded
        rules = self.bin2pat.out_yara.rules
        self.assertEqual(len(rules), 1)
        self.assertEqual(rules['file_0_0']['meta']['name'], '"ack"')
        self.assertEqual(rules['file_0_0']['meta']['bitWidth'], '32')
        self.assertEqual(rules['file_0_0']['meta']['endianness'], '"big"')
        self.assertEqual(
            rules['file_0_0']['meta']['architecture'],
            '"PowerPC"'
        )
        self.assertEqual(rules['file_0_0']['meta']['refs'], '"0054 ack"')
        self.assertEqual(
            rules['file_0_0']['strings']['$1'],
            "{ 94 21 FF E0 7C 08 02 A6 90 01 00 24 93 C1 00 18 93 E1 00 1C 7C"
            " 3F 0B 78 90 7F 00 08 90 9F 00 0C 80 1F 00 08 2F 80 00 00 40 9E"
            " 00 10 80 1F 00 0C 30 00 00 01 48 00 00 5C 80 1F 00 0C 2F 80 00"
            " 00 40 9E 00 20 80 1F 00 08 30 00 FF FF 7C 03 03 78 38 80 00 01"
            " 4? ?? ?? ?? 7C 60 1B 78 48 00 00 34 80 1F 00 08 33 C0 FF FF 80"
            " 1F 00 0C 30 00 FF FF 80 7F 00 08 7C 04 03 78 4? ?? ?? ?? 7C 60"
            " 1B 78 7F C3 F3 78 7C 04 03 78 4? ?? ?? ?? 7C 60 1B 78 7C 03 03"
            " 78 39 7F 00 20 80 0B 00 04 7C 08 03 A6 83 CB FF F8 83 EB FF FC"
            " 7D 61 5B 78 4E 80 00 20 }"
        )

class TestBin2PatInvalidRelocTest(Test):
    settings = TestSettings(
        tool='bin2pat',
        input='x86_modif.o'
    )

    # Binary x86_modif.o was modified to have invalid relocation for this test.
    def test_rules_names_patterns_only(self):
        rules = self.bin2pat.out_yara.rules
        assert 'Problem: unknown relocation code 50.' in self.bin2pat.log
        self.assertEqual(
            rules['file_0_1']['strings']['$1'],
            "{ 55 89 E5 83 EC 08 83 7D 08 00 75 07 B8 01 00 00 00 EB 1A 8B 45"
            " 08 83 E8 01 83 EC 0C 50 E8 FC FF FF FF 83 C4 10 89 C2 8B 45 08"
            " 0F AF C2 C9 C3 }"
        )

class TestBasicBin2PatArm32(Test):
    settings = TestSettings(
        tool='bin2pat',
        input='arm.o'
    )

    def test_correctly_creates_rules_count(self):
        assert self.bin2pat.succeeded
        self.assertEqual(len(self.bin2pat.out_yara.rules), 4)

    def test_complete_rule(self):
        rules = self.bin2pat.out_yara.rules
        self.assertEqual(rules['file_0_0']['meta']['name'], '"my_strlen"')
        self.assertEqual(rules['file_0_0']['meta']['bitWidth'], '32')
        self.assertEqual(rules['file_0_0']['meta']['endianness'], '"little"')
        self.assertEqual(rules['file_0_0']['meta']['architecture'], '"ARM"')
        self.assertEqual(
            rules['file_0_0']['strings']['$1'],
            "{ 04 B0 2D E5 00 B0 8D E2 14 D0 4D E2 10 00 0B E5 10 30 1B E5 08"
            " 30 0B E5 02 00 00 EA 08 30 1B E5 01 30 83 E2 08 30 0B E5 08 30"
            " 1B E5 00 30 D3 E5 00 00 53 E3 F8 FF FF 1A 08 20 1B E5 10 30 1B"
            " E5 02 30 63 E0 03 00 A0 E1 00 D0 4B E2 04 B0 9D E4 1E FF 2F E1 }"
        )
        self.assertEqual(rules['file_0_0']['conditions'], ['$1'])

    def test_rules_names_patterns_only(self):
        rules = self.bin2pat.out_yara.rules
        self.assertEqual(rules['file_0_1']['meta']['name'], '"factorial"')
        self.assertEqual(rules['file_0_1']['meta']['refs'], '"0030 factorial"')
        self.assertEqual(
            rules['file_0_1']['strings']['$1'],
            "{ 00 48 2D E9 04 B0 8D E2 08 D0 4D E2 08 00 0B E5 08 30 1B E5 00"
            " 00 53 E3 01 00 00 1A 01 30 A0 E3 06 00 00 EA 08 30 1B E5 01 30"
            " 43 E2 03 00 A0 E1 ?? ?? ?? ?? 00 30 A0 E1 08 20 1B E5"
            " 92 03 03 E0 03 00 A0 E1 04 D0 4B E2 00 88 BD E8 }"
        )
        self.assertEqual(rules['file_0_2']['meta']['name'], '"ack"')
        self.assertEqual(rules['file_0_2']['meta']['refs'], '"0048 ack"')
        self.assertEqual(
            rules['file_0_2']['strings']['$1'],
            "{ 10 48 2D E9 08 B0 8D E2 0C D0 4D E2 10 00 0B E5 14 10 0B E5 10"
            " 30 1B E5 00 00 53 E3 02 00 00 1A 14 30 1B E5 01 30 83 E2 15 00"
            " 00 EA 14 30 1B E5 00 00 53 E3 06 00 00 1A 10 30 1B E5 01 30 43"
            " E2 03 00 A0 E1 01 10 A0 E3 ?? ?? ?? ?? 00 30 A0 E1 0B"
            " 00 00 EA 10 30 1B E5 01 40 43 E2 14 30 1B E5 01 30 43 E2 10 00"
            " 1B E5 03 10 A0 E1 ?? ?? ?? ?? 00 30 A0 E1 04 00 A0 E1"
            " 03 10 A0 E1 ?? ?? ?? ?? 00 30 A0 E1 03 00 A0 E1 08 D0"
            " 4B E2 10 88 BD E8 }"
        )
        self.assertEqual(rules['file_0_3']['meta']['name'], '"test"')
        self.assertEqual(
            rules['file_0_3']['meta']['refs'], '"001c factorial 0034 ack"'
        )
        self.assertEqual(
            rules['file_0_3']['strings']['$1'],
            "{ 10 48 2D E9 08 B0 8D E2 14 D0 4D E2 10 00 0B E5 14 10 0B E5 18"
            " 20 0B E5 10 00 1B E5 ?? ?? ?? ?? 00 40 A0 E1 14 20 1B"
            " E5 18 30 1B E5 02 00 A0 E1 03 10 A0 E1 ?? ?? ?? ?? 00"
            " 30 A0 E1 FA 2F A0 E3 92 03 03 E0 03 30 84 E0 03 00 A0 E1 08 D0"
            " 4B E2 10 88 BD E8 }"
        )

class TestOPDFilesBin2PatPPC64(Test):
    settings = TestSettings(
        tool='bin2pat',
        input='ppc64-opd.o'
    )

    def test_correctly_creates_rules_count(self):
        assert self.bin2pat.succeeded
        self.assertEqual(len(self.bin2pat.out_yara.rules), 4)

    def test_complete_rule(self):
        rules = self.bin2pat.out_yara.rules
        self.assertEqual(rules['file_0_0']['meta']['name'], '"my_strlen"')
        self.assertEqual(rules['file_0_0']['meta']['bitWidth'], '64')
        self.assertEqual(rules['file_0_0']['meta']['endianness'], '"big"')
        self.assertEqual(rules['file_0_0']['meta']['architecture'], '"PowerPC"')
        self.assertEqual(
            rules['file_0_0']['strings']['$1'],
            "{ FB E1 FF F8 F8 21 FF B1 7C 3F 0B 78 F8 7F 00 80 E8 1F 00 80 F8"
            " 1F 00 30 48 00 00 10 E8 1F 00 30 30 00 00 01 F8 1F 00 30 E8 1F"
            " 00 30 7C 09 03 78 88 09 00 00 78 00 06 20 2F A0 00 00 40 9E FF"
            " E0 E8 1F 00 30 78 09 00 20 E8 1F 00 80 78 00 00 20 7C 00 48 50"
            " 78 00 00 20 7C 03 03 78 38 3F 00 50 EB E1 FF F8 4E 80 00 20 00"
            " 00 00 00 00 00 00 00 80 01 00 01 }"
        )
        self.assertEqual(rules['file_0_0']['conditions'], ['$1'])

    def test_rules_names_patterns_only(self):
        rules = self.bin2pat.out_yara.rules
        self.assertEqual(rules['file_0_1']['meta']['name'], '"factorial"')
        self.assertEqual(rules['file_0_1']['meta']['refs'], '"0040 factorial"')
        self.assertEqual(
            rules['file_0_1']['strings']['$1'],
            "{ 7C 08 02 A6 F8 01 00 10 FB E1 FF F8 F8 21 FF 81 7C 3F 0B 78 7C"
            " 60 1B 78 90 1F 00 B0 80 1F 00 B0 2F 80 00 00 40 9E 00 0C 38 00"
            " 00 01 48 00 00 30 80 1F 00 B0 30 00 FF FF 7C 00 07 B4 7C 03 03"
            " 78 4? ?? ?? ?? 7C 60 1B 78 7C 09 03 78 80 1F 00 B0 78 00 00 20"
            " 7C 09 01 D6 78 00 00 20 7C 03 03 78 38 3F 00 80 E8 01 00 10 7C"
            " 08 03 A6 EB E1 FF F8 4E 80 00 20 00 00 00 00 00 00 00 01 80 01"
            " 00 01 }"
        )
        self.assertEqual(rules['file_0_2']['meta']['name'], '"ack"')
        self.assertEqual(rules['file_0_2']['meta']['refs'], '"0064 ack"')
        self.assertEqual(
            rules['file_0_2']['strings']['$1'],
            "{ 7C 08 02 A6 F8 01 00 10 FB C1 FF F0 FB E1 FF F8 F8 21 FF 81 7C"
            " 3F 0B 78 7C 69 1B 78 7C 80 23 78 91 3F 00 B0 90 1F 00 B8 80 1F"
            " 00 B0 2F 80 00 00 40 9E 00 14 80 1F 00 B8 30 00 00 01 78 00 00"
            " 20 48 00 00 70 80 1F 00 B8 2F 80 00 00 40 9E 00 24 80 1F 00 B0"
            " 30 00 FF FF 78 00 00 20 7C 03 03 78 38 80 00 01 4? ?? ?? ?? 7C"
            " 60 1B 78 48 00 00 44 80 1F 00 B0 30 00 FF FF 78 1E 00 20 80 1F"
            " 00 B8 30 00 FF FF 78 00 00 20 81 3F 00 B0 79 29 00 20 7D 23 4B"
            " 78 7C 04 03 78 4? ?? ?? ?? 7C 60 1B 78 7F C3 F3 78 7C 04 03 78"
            " 4? ?? ?? ?? 7C 60 1B 78 7C 03 03 78 38 3F 00 80 E8 01 00 10 7C"
            " 08 03 A6 EB C1 FF F0 EB E1 FF F8 4E 80 00 20 00 00 00 00 00 00"
            " 00 01 80 02 00 01 }"
        )
        self.assertEqual(rules['file_0_3']['meta']['name'], '"test"')
        self.assertEqual(
            rules['file_0_3']['meta']['refs'], '"003c factorial 0060 ack"'
        )
        self.assertEqual(
            rules['file_0_3']['strings']['$1'],
            "{ 7C 08 02 A6 F8 01 00 10 FB C1 FF F0 FB E1 FF F8 F8 21 FF 81 7C"
            " 3F 0B 78 7C 6B 1B 78 7C 89 23 78 7C A0 2B 78 91 7F 00 B0 91 3F"
            " 00 B8 90 1F 00 C0 80 1F 00 B0 7C 00 07 B4 7C 03 03 78 4? ?? ??"
            " ?? 7C 60 1B 78 7C 1E 03 78 80 1F 00 B8 78 09 00 20 80 1F 00 C0"
            " 78 00 00 20 7D 23 4B 78 7C 04 03 78 4? ?? ?? ?? 7C 60 1B 78 1C"
            " 00 03 E8 78 00 00 20 7C 1E 02 14 78 00 00 20 7C 03 03 78 38 3F"
            " 00 80 E8 01 00 10 7C 08 03 A6 EB C1 FF F0 EB E1 FF F8 4E 80 00"
            " 20 00 00 00 00 00 00 00 01 80 02 00 01 }"
        )
