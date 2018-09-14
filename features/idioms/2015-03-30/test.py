from regression_tests import *

inName="idioms"

class CommonTest(Test):

    #local_arch=""
    #local_format=""

    # Check presence of all functions.
    #
    def test_has_all_functions(self):
        assert self.out_c.has_func_matching(r'_?test_01_LessThanZero')
        assert self.out_c.has_func_matching(r'_?test_02_GreaterEqualZero')
        assert self.out_c.has_func_matching(r'_?test_03_XorAssignZero')
        assert self.out_c.has_func_matching(r'_?test_04_BitShiftMult')
        assert self.out_c.has_func_matching(r'_?test_05_DivByMinusTwo')
        assert self.out_c.has_func_matching(r'_?test_06_BitShiftDiv')
        assert self.out_c.has_func_matching(r'_?test_07_MagicDivSigned')
        assert self.out_c.has_func_matching(r'_?test_08_MagicDivSignedNegative')
        assert self.out_c.has_func_matching(r'_?test_09_MagicDivUnsinged')
        assert self.out_c.has_func_matching(r'_?test_10_XorMinusOne')
        assert self.out_c.has_func_matching(r'_?test_11_SignedModulo')
        assert self.out_c.has_func_matching(r'_?test_12_UnsignedModulo')
        assert self.out_c.has_func_matching(r'_?test_13_FloatNeg')
        assert self.out_c.has_func_matching(r'_?test_14_CopySign')
        assert self.out_c.has_func_matching(r'_?test_15_FloatAbs')

    # Idiom test LessThanZero
    #
    def test_c_does_not_contain_idiom_LessThanZero(self):
        assert self.out_c.contains(r'printf\("test_01_LessThanZero: %d", \(int32_t\)\(\S+ < 0\)\);')

    # Idiom test GreaterEqualZero
    #
    def test_c_does_not_contain_idiom_GreaterEqualZero(self):
        # TODO: powerpc - bug - "(int32_t)(-v1 < 1)" instead of "v1 > -1"
        # TODO: pic32 /O1/ - ---||---
        # TODO: arm /O1,O2,O#/ - ---||---
        # TODO: thumb - bug
        test_arch = {'mips', 'x86'}
        if self.local_arch in test_arch:
            assert self.out_c.contains(r'printf\("test_02_GreaterEqualZero: %d", \(int32_t\)\(\S+ > -1\)\);')

    # Idiom test LessThanZero
    #
    def test_c_does_not_contain_idiom_XorAssignZero(self):
        # TODO: thumb /O0/ - bug - empty function
        if self.local_arch != 'thumb':
            assert self.out_c.contains(r'printf\("test_03_XorAssignZero: %d", 0\);')

    # Idiom test BitShiftMult
    #
    def test_c_does_not_contain_idiom_BitShiftMult(self):
        assert self.out_c.contains(r'printf\("test_04_BitShiftMult_01: %d", 2 \* \S+\);')
        assert self.out_c.contains(r'printf\("test_04_BitShiftMult_02: %d", 4 \* \S+\);')
        assert self.out_c.contains(r'printf\("test_04_BitShiftMult_03: %d", 8 \* \S+\);')
        assert self.out_c.contains(r'printf\("test_04_BitShiftMult_04: %d", 16 \* \S+\);')
        assert self.out_c.contains(r'printf\("test_04_BitShiftMult_05: %d", 32 \* \S+\);')
        assert self.out_c.contains(r'printf\("test_04_BitShiftMult_06: %d", 64 \* \S+\);')
        assert self.out_c.contains(r'printf\("test_04_BitShiftMult_07: %d", 128 \* \S+\);')
        assert self.out_c.contains(r'printf\("test_04_BitShiftMult_08: %d", 256 \* \S+\);')
        assert self.out_c.contains(r'printf\("test_04_BitShiftMult_09: %d", 512 \* \S+\);')
        assert self.out_c.contains(r'printf\("test_04_BitShiftMult_10: %d", 1024 \* \S+\);')
        assert self.out_c.contains(r'printf\("test_04_BitShiftMult_20: %d", 0x100000 \* \S+\);')
        # TODO: thumb - bug
        if self.local_arch != 'thumb':
            assert self.out_c.contains(r'printf\("test_04_BitShiftMult_30: %d", 0x40000000 \* \S+\);')

    # Idiom test DivByMinusTwo
    #
    def test_c_does_not_contain_idiom_DivByMinusTwo(self):
        # TODO: x86 - bug - "((int32_t)(v1 < 0) + v1) / -2)" instead of "v1 / -2"
        # TODO: thumb - bug - "-((((int32_t)(v1 < 0) + v1) / 2))" instead of "v1 / -2"
        test_arch = {'mips', 'pic32', 'powerpc', 'arm'}
        if self.local_arch in test_arch:
            assert self.out_c.contains(r'printf\("test_05_DivByMinusTwo: %d", \S+ / -2\);')

    # Idiom test BitShiftDiv
    #
    def test_c_does_not_contain_idiom_BitShiftDiv(self):
        # TODO: x86 - bug - "(v1 < 0 ? v1 + 3 : v1) / 4" instead of "v1 / 4"
        # TODO: pic32 - bug - "(v1 < 0) + v1) / 2)" instead of "v1 / 4"
        # TODO: arm - bug - "((int32_t)(v1 < 0) + v1) / 2)" instead of "v1 / 2"
        # TODO: thumb - bug - "((int32_t)(v1 < 0) + v1) / 2)" instead of "v1 / 2"
        test_arch = {'mips', 'powerpc'}
        if self.local_arch in test_arch:
            # TODO: powerpc - bug - "v2 / 2 | v2 & -0x80000000" instead of "v1 / 2"
            if self.local_arch != 'powerpc':
                assert self.out_c.contains(r'printf\("test_06_BitShiftDiv_01: %d", \S+ / 2\);')
            assert self.out_c.contains(r'printf\("test_06_BitShiftDiv_02: %d", \S+ / 4\);')
            assert self.out_c.contains(r'printf\("test_06_BitShiftDiv_03: %d", \S+ / 8\);')
            assert self.out_c.contains(r'printf\("test_06_BitShiftDiv_04: %d", \S+ / 16\);')
            assert self.out_c.contains(r'printf\("test_06_BitShiftDiv_05: %d", \S+ / 32\);')
            assert self.out_c.contains(r'printf\("test_06_BitShiftDiv_06: %d", \S+ / 64\);')
            assert self.out_c.contains(r'printf\("test_06_BitShiftDiv_07: %d", \S+ / 128\);')
            assert self.out_c.contains(r'printf\("test_06_BitShiftDiv_08: %d", \S+ / 256\);')
            assert self.out_c.contains(r'printf\("test_06_BitShiftDiv_09: %d", \S+ / 512\);')
            assert self.out_c.contains(r'printf\("test_06_BitShiftDiv_10: %d", \S+ / 1024\);')
            assert self.out_c.contains(r'printf\("test_06_BitShiftDiv_20: %d", \S+ / 0x100000\);')
            assert self.out_c.contains(r'printf\("test_06_BitShiftDiv_30: %d", \S+ / 0x40000000\);')

    # Idiom test MagicDivSigned
    #
    def test_c_does_not_contain_idiom_MagicDivSigned(self):
        # TODO: x86 - bug - totally wrong
        # TODO: arm - bug - totally wrong
        # TODO: powerpc /O1,O2,O3/ - bug - some of the idioms contain type casting
        test_arch = {'mips', 'pic32', 'thumb'}
        if self.local_arch in test_arch:
            # TODO: pic32 - bug
            if self.local_arch != 'pic32':
                assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_03: %d", \S+ / 3\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_05: %d", \S+ / 5\);')
            # TODO: pic32 - bug
            if self.local_arch != 'pic32':
                assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_06: %d", \S+ / 6\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_07: %d", \S+ / 7\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_09: %d", \S+ / 9\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_10: %d", \S+ / 10\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_11: %d", \S+ / 11\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_12: %d", \S+ / 12\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_13: %d", \S+ / 13\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_14: %d", \S+ / 14\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_15: %d", \S+ / 15\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_17: %d", \S+ / 17\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_18: %d", \S+ / 18\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_19: %d", \S+ / 19\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_20: %d", \S+ / 20\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_29: %d", \S+ / 29\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_30: %d", \S+ / 30\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_31: %d", \S+ / 31\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_35: %d", \S+ / 35\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_47: %d", \S+ / 47\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_51: %d", \S+ / 51\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_57: %d", \S+ / 57\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_62: %d", \S+ / 62\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_70: %d", \S+ / 70\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_73: %d", \S+ / 73\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_89: %d", \S+ / 89\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_91: %d", \S+ / 91\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_94: %d", \S+ / 94\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_95: %d", \S+ / 95\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_99: %d", \S+ / 99\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_100: %d", \S+ / 100\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_101: %d", \S+ / 101\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_102: %d", \S+ / 102\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_120: %d", \S+ / 120\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_203: %d", \S+ / 203\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_204: %d", \S+ / 204\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_213: %d", \S+ / 213\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_218: %d", \S+ / 218\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_221: %d", \S+ / 221\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_228: %d", \S+ / 228\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_254: %d", \S+ / 254\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_255: %d", \S+ / 255\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_58441: %d", \S+ / 0xe449\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_58442: %d", \S+ / 0xe44a\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_58443: %d", \S+ / 0xe44b\);')
            assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_58444: %d", \S+ / 0xe44c\);')
            # TODO: mips - bug - load of 32-bit numbers
            # TODO: pic32 - bug - load of 32-bit numbers
            # TODO: thumb - bug - "*(int32_t *)g5 / 0xe44d"
            test_arch = {'powerpc', 'arm', 'x86'}
            if self.local_arch in test_arch:
                assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_58445: %d", \S+ / 0xe44d\);')
                assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_68441835: %d", \S+ / 0x41456eb\);')
                assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_68441836: %d", \S+ / 0x41456ec\);')
                assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_68441837: %d", \S+ / 0x41456ed\);')
                assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_68441838: %d", \S+ / 0x41456ee\);')
                assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_68441839: %d", \S+ / 0x41456ef\);')
                assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_68441840: %d", \S+ / 0x41456f0\);')
                assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_68441841: %d", \S+ / 0x41456f1\);')
                assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_68441842: %d", \S+ / 0x41456f2\);')
                # TODO: thumb - bug
                if self.local_arch != 'thumb':
                    assert self.out_c.contains(r'printf\("test_07_MagicDivSigned_68441843: %d", \S+ / 0x41456f3\);')

    # Idiom test MagicDivSignedNegative
    #
    def test_c_does_not_contain_idiom_MagicDivSignedNegative(self):
        # TODO: x86 - bug - totally wrong
        # TODO: arm - bug - totally wrong
        # TODO: powerpc /O1,O2,O3/ - bug - some of the idioms contain type casting
        test_arch = {'mips', 'pic32', 'thumb'}
        if self.local_arch in test_arch:
            # TODO: pic32 - bug
            if self.local_arch != 'pic32':
                assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_03: %d", \S+ / -3\);')
            assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_05: %d", \S+ / -5\);')
            # TODO: pic32 - bug
            if self.local_arch != 'pic32':
                assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_06: %d", \S+ / -6\);')
            assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_07: %d", \S+ / -7\);')
            assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_09: %d", \S+ / -9\);')
            assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_10: %d", \S+ / -10\);')
            assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_11: %d", \S+ / -11\);')
            assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_12: %d", \S+ / -12\);')
            assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_13: %d", \S+ / -13\);')
            assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_14: %d", \S+ / -14\);')
            assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_15: %d", \S+ / -15\);')
            assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_17: %d", \S+ / -17\);')
            assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_18: %d", \S+ / -18\);')
            assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_19: %d", \S+ / -19\);')
            assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_20: %d", \S+ / -20\);')
            assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_29: %d", \S+ / -29\);')
            assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_30: %d", \S+ / -30\);')
            assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_31: %d", \S+ / -31\);')
            assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_35: %d", \S+ / -35\);')
            assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_47: %d", \S+ / -47\);')
            assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_51: %d", \S+ / -51\);')
            assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_57: %d", \S+ / -57\);')
            assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_62: %d", \S+ / -62\);')
            assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_70: %d", \S+ / -70\);')
            assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_73: %d", \S+ / -73\);')
            # TODO: thumb - strange bug - all the following calls are missing
            if self.local_arch != 'thumb':
                assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_89: %d", \S+ / -89\);')
                assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_91: %d", \S+ / -91\);')
                assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_94: %d", \S+ / -94\);')
                assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_95: %d", \S+ / -95\);')
                assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_99: %d", \S+ / -99\);')
                assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_100: %d", \S+ / -100\);')
                assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_101: %d", \S+ / -101\);')
                assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_102: %d", \S+ / -102\);')
                assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_120: %d", \S+ / -120\);')
                assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_203: %d", \S+ / -203\);')
                assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_204: %d", \S+ / -204\);')
                assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_213: %d", \S+ / -213\);')
                assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_218: %d", \S+ / -218\);')
                assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_221: %d", \S+ / -221\);')
                assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_228: %d", \S+ / -228\);')
                assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_254: %d", \S+ / -254\);')
                assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_255: %d", \S+ / -255\);')
                # TODO: mips - bug - load of 32-bit numbers
                # TODO: pic32 - bug - load of 32-bit numbers
                test_arch = {'powerpc', 'arm', 'thumb', 'x86'}
                if self.local_arch in test_arch:
                    assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_58441: %d", \S+ / -0xe449\);')
                    assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_58442: %d", \S+ / -0xe44a\);')
                    assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_58443: %d", \S+ / -0xe44b\);')
                    assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_58444: %d", \S+ / -0xe44c\);')
                    assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_58445: %d", \S+ / -0xe44d\);')
                    assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_68441835: %d", \S+ / -0x41456eb\);')
                    assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_68441836: %d", \S+ / -0x41456ec\);')
                    assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_68441837: %d", \S+ / -0x41456ed\);')
                    assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_68441838: %d", \S+ / -0x41456ee\);')
                    assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_68441839: %d", \S+ / -0x41456ef\);')
                    assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_68441840: %d", \S+ / -0x41456f0\);')
                    assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_68441841: %d", \S+ / -0x41456f1\);')
                    assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_68441842: %d", \S+ / -0x41456f2\);')
                    assert self.out_c.contains(r'printf\("test_08_MagicDivSignedNegative_68441843: %d", \S+ / -0x41456f3\);')

    # Idiom test MagicDivUnsinged
    #
    def test_c_does_not_contain_idiom_MagicDivUnsinged(self):
        # TODO: x86 - bug - totally wrong
        # TODO: pic32 - bug - totally wrong
        # TODO: arm /O1-O3/ - bug - totally wrong
        # TODO: powerpc /O1,O2,O3/ - bug - some of the idioms contain type casting
        test_arch = {'mips', 'thumb'}
        if self.local_arch in test_arch:
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_03: %d", \S+ / 3\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_05: %d", \S+ / 5\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_06: %d", \S+ / 6\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_07: %d", \S+ / 7\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_09: %d", \S+ / 9\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_10: %d", \S+ / 10\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_11: %d", \S+ / 11\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_12: %d", \S+ / 12\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_13: %d", \S+ / 13\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_14: %d", \S+ / 14\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_15: %d", \S+ / 15\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_17: %d", \S+ / 17\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_18: %d", \S+ / 18\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_19: %d", \S+ / 19\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_20: %d", \S+ / 20\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_29: %d", \S+ / 29\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_30: %d", \S+ / 30\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_31: %d", \S+ / 31\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_35: %d", \S+ / 35\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_47: %d", \S+ / 47\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_51: %d", \S+ / 51\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_57: %d", \S+ / 57\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_62: %d", \S+ / 62\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_70: %d", \S+ / 70\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_73: %d", \S+ / 73\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_89: %d", \S+ / 89\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_91: %d", \S+ / 91\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_94: %d", \S+ / 94\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_95: %d", \S+ / 95\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_99: %d", \S+ / 99\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_100: %d", \S+ / 100\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_101: %d", \S+ / 101\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_102: %d", \S+ / 102\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_120: %d", \S+ / 120\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_203: %d", \S+ / 203\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_204: %d", \S+ / 204\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_213: %d", \S+ / 213\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_218: %d", \S+ / 218\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_221: %d", \S+ / 221\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_228: %d", \S+ / 228\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_254: %d", \S+ / 254\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_255: %d", \S+ / 255\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_58441: %d", \S+ / 0xe449\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_58442: %d", \S+ / 0xe44a\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_58443: %d", \S+ / 0xe44b\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_58444: %d", \S+ / 0xe44c\);')
            assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_58445: %d", \S+ / 0xe44d\);')
            # TODO: mips - bug - load of 32-bit numbers
            # TODO: thumb - bug - " struct struct_7 * v1"
            test_arch = {'pic32', 'powerpc', 'arm', 'x86'}
            if self.local_arch in test_arch:
                assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_68441835: %d", \S+ / 0x41456eb\);')
                assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_68441836: %d", \S+ / 0x41456ec\);')
                assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_68441837: %d", \S+ / 0x41456ed\);')
                assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_68441838: %d", \S+ / 0x41456ee\);')
                assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_68441839: %d", \S+ / 0x41456ef\);')
                assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_68441840: %d", \S+ / 0x41456f0\);')
                assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_68441841: %d", \S+ / 0x41456f1\);')
                assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_68441842: %d", \S+ / 0x41456f2\);')
                # TODO: thumb - bug
                if self.local_arch != 'thumb':
                    assert self.out_c.contains(r'printf\("test_09_MagicDivUnsinged_68441843: %d", \S+ / 0x41456f3\);')

    # Idiom test XorMinusOne
    #
    def test_c_does_not_contain_idiom_XorMinusOne(self):
        # TODO: thumb - bug
        if self.local_arch != 'thumb':
            assert self.out_c.contains(r'printf\("test_10_XorMinusOne: %d", -1 - \S+\);')

    # Idiom test SignedModulo
    #
    def test_c_does_not_contain_idiom_SignedModulo(self):
        # TODO: x86 - bug - totally wrong
        # TODO: arm - bug - totally wrong
        # TODO: powerpc - bug - some of the idioms contain type casting
        test_arch = {'mips', 'pic32', 'thumb'}
        if self.local_arch in test_arch:
            # TODO: thumb - bug - % (pow_2) is wrong
            if self.local_arch != 'thumb':
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_02: %d", \S+ % 2\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_03: %d", \S+ % 3\);')
            # TODO: thumb - bug - % (pow_2) is wrong
            if self.local_arch != 'thumb':
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_04: %d", \S+ % 4\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_05: %d", \S+ % 5\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_06: %d", \S+ % 6\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_07: %d", \S+ % 7\);')
            # TODO: thumb - bug - % (pow_2) is wrong
            if self.local_arch != 'thumb':
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_08: %d", \S+ % 8\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_09: %d", \S+ % 9\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_10: %d", \S+ % 10\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_11: %d", \S+ % 11\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_12: %d", \S+ % 12\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_13: %d", \S+ % 13\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_14: %d", \S+ % 14\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_15: %d", \S+ % 15\);')
            # TODO: thumb - bug - % (pow_2) is wrong
            if self.local_arch != 'thumb':
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_16: %d", \S+ % 16\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_17: %d", \S+ % 17\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_18: %d", \S+ % 18\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_19: %d", \S+ % 19\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_20: %d", \S+ % 20\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_29: %d", \S+ % 29\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_30: %d", \S+ % 30\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_31: %d", \S+ % 31\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_35: %d", \S+ % 35\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_47: %d", \S+ % 47\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_51: %d", \S+ % 51\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_57: %d", \S+ % 57\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_62: %d", \S+ % 62\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_70: %d", \S+ % 70\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_73: %d", \S+ % 73\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_89: %d", \S+ % 89\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_91: %d", \S+ % 91\);')
            assert self.out_c.contains(r'printf\("test_11_SignedModulo_94: %d", \S+ % 94\);')
            # TODO: thumb - multiple bug on thumb /O0 x O1 x .../
            if self.local_arch != 'thumb':
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_95: %d", \S+ % 95\);')
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_99: %d", \S+ % 99\);')
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_100: %d", \S+ % 100\);')
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_101: %d", \S+ % 101\);')
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_102: %d", \S+ % 102\);')
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_120: %d", \S+ % 120\);')
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_128: %d", \S+ % 128\);')
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_203: %d", \S+ % 203\);')
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_204: %d", \S+ % 204\);')
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_213: %d", \S+ % 213\);')
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_218: %d", \S+ % 218\);')
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_221: %d", \S+ % 221\);')
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_228: %d", \S+ % 228\);')
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_254: %d", \S+ % 254\);')
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_255: %d", \S+ % 255\);')
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_256: %d", \S+ % 256\);')
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_58441: %d", \S+ % 0xe449\);')
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_58442: %d", \S+ % 0xe44a\);')
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_58443: %d", \S+ % 0xe44b\);')
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_58444: %d", \S+ % 0xe44c\);')
                assert self.out_c.contains(r'printf\("test_11_SignedModulo_58445: %d", \S+ % 0xe44d\);')
                # TODO: mips - bug - load of 32-bit numbers
                # TODO: pic32 - bug - load of 32-bit numbers
                test_arch = {'powerpc', 'arm', 'thumb', 'x86'}
                if self.local_arch in test_arch:
                    assert self.out_c.contains(r'printf\("test_11_SignedModulo_68441835: %d", \S+ % 0x41456eb\);')
                    assert self.out_c.contains(r'printf\("test_11_SignedModulo_68441836: %d", \S+ % 0x41456ec\);')
                    assert self.out_c.contains(r'printf\("test_11_SignedModulo_68441837: %d", \S+ % 0x41456ed\);')
                    assert self.out_c.contains(r'printf\("test_11_SignedModulo_68441838: %d", \S+ % 0x41456ee\);')
                    assert self.out_c.contains(r'printf\("test_11_SignedModulo_68441839: %d", \S+ % 0x41456ef\);')
                    assert self.out_c.contains(r'printf\("test_11_SignedModulo_68441840: %d", \S+ % 0x41456f0\);')
                    assert self.out_c.contains(r'printf\("test_11_SignedModulo_68441841: %d", \S+ % 0x41456f1\);')
                    assert self.out_c.contains(r'printf\("test_11_SignedModulo_68441842: %d", \S+ % 0x41456f2\);')
                    assert self.out_c.contains(r'printf\("test_11_SignedModulo_68441843: %d", \S+ % 0x41456f3\);')

    # Idiom test UnsignedModulo
    #
    def test_c_does_not_contain_idiom_UnsignedModulo(self):
        # TODO: x86 - bug - totally wrong
        # TODO: arm - bug - totally wrong
        # TODO: thumb /O0/ - minor bug - there is a type cast
        # TODO: powerpc - bug - some of the idioms contain type casting
        test_arch = {'mips', 'pic32'}
        if self.local_arch in test_arch:
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_02: %d", .* % 2\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_03: %d", .* % 3\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_04: %d", .* % 4\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_05: %d", .* % 5\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_06: %d", .* % 6\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_07: %d", .* % 7\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_08: %d", .* % 8\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_09: %d", .* % 9\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_10: %d", .* % 10\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_11: %d", .* % 11\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_12: %d", .* % 12\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_13: %d", .* % 13\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_14: %d", .* % 14\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_15: %d", .* % 15\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_16: %d", .* % 16\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_17: %d", .* % 17\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_18: %d", .* % 18\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_19: %d", .* % 19\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_20: %d", .* % 20\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_29: %d", .* % 29\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_30: %d", .* % 30\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_31: %d", .* % 31\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_35: %d", .* % 35\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_47: %d", .* % 47\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_51: %d", .* % 51\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_57: %d", .* % 57\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_62: %d", .* % 62\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_70: %d", .* % 70\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_73: %d", .* % 73\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_89: %d", .* % 89\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_91: %d", .* % 91\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_94: %d", .* % 94\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_95: %d", .* % 95\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_99: %d", .* % 99\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_100: %d", .* % 100\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_101: %d", .* % 101\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_102: %d", .* % 102\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_120: %d", .* % 120\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_128: %d", .* % 128\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_203: %d", .* % 203\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_204: %d", .* % 204\)')
            assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_213: %d", .* % 213\)')
            # TODO: thumb - strange bug - all the following calls are missing
            if self.local_arch != 'thumb':
                assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_218: %d", .* % 218\)')
                assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_221: %d", .* % 221\)')
                assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_228: %d", .* % 228\)')
                assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_254: %d", .* % 254\)')
                assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_255: %d", .* % 255\)')
                # TODO: mips - bug
                # TODO: pic32 - bug
                test_arch = {'powerpc', 'arm', 'thumb', 'x86'}
                if self.local_arch in test_arch:
                    assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_256: %d", .* % 256\)')
                assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_58441: %d", .* % 0xe449\)')
                assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_58442: %d", .* % 0xe44a\)')
                assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_58443: %d", .* % 0xe44b\)')
                assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_58444: %d", .* % 0xe44c\)')
                assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_58445: %d", .* % 0xe44d\)')
                # TODO: mips - bug - load of 32-bit numbers
                # TODO: pic32 - bug - load of 32-bit numbers
                test_arch = {'powerpc', 'arm', 'thumb', 'x86'}
                if self.local_arch in test_arch:
                    assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_68441835: %d", .* % 0x41456eb\)')
                    assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_68441836: %d", .* % 0x41456ec\)')
                    assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_68441837: %d", .* % 0x41456ed\)')
                    assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_68441838: %d", .* % 0x41456ee\)')
                    assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_68441839: %d", .* % 0x41456ef\)')
                    assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_68441840: %d", .* % 0x41456f0\)')
                    assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_68441841: %d", .* % 0x41456f1\)')
                    assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_68441842: %d", .* % 0x41456f2\)')
                    assert self.out_c.contains(r'printf\("test_12_UnsignedModulo_68441843: %d", .* % 0x41456f3\)')

    # Idiom test FloatNeg - only for mips and arm (powerpc lacks support of FPU)
    #
    #
    def test_c_does_not_contain_idiom_FloatNeg(self):
        # TODO: mips - bug
        # TODO: pic32 - bug
        # TODO: arm - it is correct, but there remain many type casts
        # TODO: thumb - bug
        test_arch = {''}
        if self.local_arch in test_arch:
            assert self.out_c.contains(r'printf\("test_13_FloatNeg: %f", - \S+\);')

    # Idiom test CopySign - only for mips and arm (powerpc lacks support of FPU)
    #
    def test_c_does_not_contain_idiom_CopySign(self):
        # TODO: mips
        test_arch = {'pic32', 'arm', 'thumb'}
        if self.local_arch in test_arch:
            if self.local_format != 'pe':
                assert self.out_c.funcs['test_14_CopySign'].calls('copysignf')

    # Idiom test FloatAbs - only for mips and arm (powerpc lacks support of FPU)
    #
    def test_c_does_not_contain_idiom_FloatAbs(self):
        # TODO: mips - bug
        # TODO: pic32 /O1/ - bug
        # TODO: thumb /O1,O3/ - bug
        test_arch = {'arm'}
        if self.local_arch in test_arch:
            if self.local_format != 'pe':
                if self.out_c.funcs['test_15_FloatAbs'].calls('fabsf') or self.out_c.funcs['test_15_FloatAbs'].calls('fabs'):
                    test_15_FloatAbs_calls_fabsX = True
                else:
                    test_15_FloatAbs_calls_fabsX = False
                assert test_15_FloatAbs_calls_fabsX == True

class TestArmGccElfO0(CommonTest):
    settings = TestSettings( input=inName+'.arm.gnuarmgcc-4.4.1.O0.elf')
    local_arch="arm"
    local_format="elf"
class TestArmGccElfO1(CommonTest):
    settings = TestSettings( input=inName+'.arm.gnuarmgcc-4.4.1.O1.elf')
    local_arch="arm"
    local_format="elf"
class TestArmGccElfO3(CommonTest):
    settings = TestSettings( input=inName+'.arm.gnuarmgcc-4.4.1.O3.elf')
    local_arch="arm"
    local_format="elf"

class TestArmGccExeO0(CommonTest):
    settings = TestSettings( input=inName+'.arm.mingw32ce-4.4.0.O0.ex')
    local_arch="arm"
    local_format="pe"
class TestArmGccExeO1(CommonTest):
    settings = TestSettings( input=inName+'.arm.mingw32ce-4.4.0.O1.ex')
    local_arch="arm"
    local_format="pe"
class TestArmGccExeO3(CommonTest):
    settings = TestSettings( input=inName+'.arm.mingw32ce-4.4.0.O3.ex')
    local_arch="arm"
    local_format="pe"

class TestMipsGccElfO0(CommonTest):
    settings = TestSettings( input=inName+'.mips.pspgcc-4.3.5.O0.elf')
    local_arch="mips"
    local_format="elf"
class TestMipsGccElfO1(CommonTest):
    settings = TestSettings( input=inName+'.mips.pspgcc-4.3.5.O1.elf')
    local_arch="mips"
    local_format="elf"
class TestMipsGccElfO3(CommonTest):
    settings = TestSettings( input=inName+'.mips.pspgcc-4.3.5.O3.elf')
    local_arch="mips"
    local_format="elf"

class TestPic32GccElfO0(CommonTest):
    settings = TestSettings( input=inName+'.pic32.gcc-4.5.2.O0.elf')
    local_arch="pic32"
    local_format="elf"
class TestPic32GccElfO1(CommonTest):
    settings = TestSettings( input=inName+'.pic32.gcc-4.5.2.O1.elf')
    local_arch="pic32"
    local_format="elf"

class TestPowerpcGccElfO0(CommonTest):
    settings = TestSettings( input=inName+'.powerpc.gcc-4.5.1.O0.elf')
    local_arch="powerpc"
    local_format="elf"
class TestPowerpcGccElfO1(CommonTest):
    settings = TestSettings( input=inName+'.powerpc.gcc-4.5.1.O1.elf')
    local_arch="powerpc"
    local_format="elf"
class TestPowerpcGccElfO3(CommonTest):
    settings = TestSettings( input=inName+'.powerpc.gcc-4.5.1.O3.elf')
    local_arch="powerpc"
    local_format="elf"

class TestThumbGccElfO0(CommonTest):
    settings = TestSettings( input=inName+'.thumb.gnuarmgcc-4.4.1.O0.elf')
    local_arch="thumb"
    local_format="elf"
class TestThumbGccElfO1(CommonTest):
    settings = TestSettings( input=inName+'.thumb.gnuarmgcc-4.4.1.O1.elf')
    local_arch="thumb"
    local_format="elf"
class TestThumbGccElfO3(CommonTest):
    settings = TestSettings( input=inName+'.thumb.gnuarmgcc-4.4.1.O3.elf')
    local_arch="thumb"
    local_format="elf"

class TestX86GccElfO0(CommonTest):
    settings = TestSettings( input=inName+'.x86.gcc-4.7.2.O0.elf')
    local_arch="x86"
    local_format="elf"
class TestX86GccElfO1(CommonTest):
    settings = TestSettings( input=inName+'.x86.gcc-4.7.2.O1.elf')
    local_arch="x86"
    local_format="elf"
class TestX86GccElfO3(CommonTest):
    settings = TestSettings( input=inName+'.x86.gcc-4.7.2.O3.elf')
    local_arch="x86"
    local_format="elf"

class TestX86GccExeO0(CommonTest):
    settings = TestSettings( input=inName+'.x86.mingw32-gcc-4.7.3.O0.ex')
    local_arch="x86"
    local_format="pe"
class TestX86GccExeO1(CommonTest):
    settings = TestSettings( input=inName+'.x86.mingw32-gcc-4.7.3.O1.ex')
    local_arch="x86"
    local_format="pe"
class TestX86GccExeO3(CommonTest):
    settings = TestSettings( input=inName+'.x86.mingw32-gcc-4.7.3.O3.ex')
    local_arch="x86"
    local_format="pe"
