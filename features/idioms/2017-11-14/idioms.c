#include <stdio.h>
#include <math.h>

int __attribute__ ((noinline)) test_01_LessThanZero(void)
{
	int num;
	scanf("%d", &num);
	printf("test_01_LessThanZero: %d", num < 0);
	return 1;
}

int __attribute__ ((noinline)) test_02_GreaterEqualZero(void)
{
	int num;
	scanf("%d", &num);
	printf("test_02_GreaterEqualZero: %d", num >= 0);
	return 2;
}

int __attribute__ ((noinline)) test_03_XorAssignZero(void)
{
	int num;
	scanf("%d", &num);
	printf("test_03_XorAssignZero: %d", num ^= num);
	return 3;
}

int __attribute__ ((noinline)) test_04_BitShiftMult(void)
{
	int num;
	scanf("%d", &num);
	printf("test_04_BitShiftMult_01: %d", num * 2);
	printf("test_04_BitShiftMult_02: %d", num * 4);
	printf("test_04_BitShiftMult_03: %d", num * 8);
	printf("test_04_BitShiftMult_04: %d", num * 16);
	printf("test_04_BitShiftMult_05: %d", num * 32);
	printf("test_04_BitShiftMult_06: %d", num * 64);
	printf("test_04_BitShiftMult_07: %d", num * 128);
	printf("test_04_BitShiftMult_08: %d", num * 256);
	printf("test_04_BitShiftMult_09: %d", num * 512);
	printf("test_04_BitShiftMult_10: %d", num * 1024);
	printf("test_04_BitShiftMult_20: %d", num * 0x100000);
	printf("test_04_BitShiftMult_30: %d", num * 0x40000000);
	return 4;
}

int __attribute__ ((noinline)) test_05_DivByMinusTwo(void)
{
	int num;
	scanf("%d", &num);
	printf("test_05_DivByMinusTwo: %d", num / -2);
	return 5;
}

int __attribute__ ((noinline)) test_06_BitShiftDiv(void)
{
	int num;
	scanf("%d", &num);
	printf("test_06_BitShiftDiv_01: %d", num / 2);
	printf("test_06_BitShiftDiv_02: %d", num / 4);
	printf("test_06_BitShiftDiv_03: %d", num / 8);
	printf("test_06_BitShiftDiv_04: %d", num / 16);
	printf("test_06_BitShiftDiv_05: %d", num / 32);
	printf("test_06_BitShiftDiv_06: %d", num / 64);
	printf("test_06_BitShiftDiv_07: %d", num / 128);
	printf("test_06_BitShiftDiv_08: %d", num / 256);
	printf("test_06_BitShiftDiv_09: %d", num / 512);
	printf("test_06_BitShiftDiv_10: %d", num / 1024);
	printf("test_06_BitShiftDiv_20: %d", num / 0x100000);
	printf("test_06_BitShiftDiv_30: %d", num / 0x40000000);
	return 6;
}

int __attribute__ ((noinline)) test_07_MagicDivSigned(void)
{
	int num;
	scanf("%d", &num);
	printf("test_07_MagicDivSigned_03: %d", num / 3);
	printf("test_07_MagicDivSigned_05: %d", num / 5);
	printf("test_07_MagicDivSigned_06: %d", num / 6);
	printf("test_07_MagicDivSigned_07: %d", num / 7);
	printf("test_07_MagicDivSigned_09: %d", num / 9);
	printf("test_07_MagicDivSigned_10: %d", num / 10);
	printf("test_07_MagicDivSigned_11: %d", num / 11);
	printf("test_07_MagicDivSigned_12: %d", num / 12);
	printf("test_07_MagicDivSigned_13: %d", num / 13);
	printf("test_07_MagicDivSigned_14: %d", num / 14);
	printf("test_07_MagicDivSigned_15: %d", num / 15);
	printf("test_07_MagicDivSigned_17: %d", num / 17);
	printf("test_07_MagicDivSigned_18: %d", num / 18);
	printf("test_07_MagicDivSigned_19: %d", num / 19);
	printf("test_07_MagicDivSigned_20: %d", num / 20);
	printf("test_07_MagicDivSigned_29: %d", num / 29);
	printf("test_07_MagicDivSigned_30: %d", num / 30);
	printf("test_07_MagicDivSigned_31: %d", num / 31);
	printf("test_07_MagicDivSigned_35: %d", num / 35);
	printf("test_07_MagicDivSigned_47: %d", num / 47);
	printf("test_07_MagicDivSigned_51: %d", num / 51);
	printf("test_07_MagicDivSigned_57: %d", num / 57);
	printf("test_07_MagicDivSigned_62: %d", num / 62);
	printf("test_07_MagicDivSigned_70: %d", num / 70);
	printf("test_07_MagicDivSigned_73: %d", num / 73);
	printf("test_07_MagicDivSigned_89: %d", num / 89);
	printf("test_07_MagicDivSigned_91: %d", num / 91);
	printf("test_07_MagicDivSigned_94: %d", num / 94);
	printf("test_07_MagicDivSigned_95: %d", num / 95);
	printf("test_07_MagicDivSigned_99: %d", num / 99);
	printf("test_07_MagicDivSigned_100: %d", num / 100);
	printf("test_07_MagicDivSigned_101: %d", num / 101);
	printf("test_07_MagicDivSigned_102: %d", num / 102);
	printf("test_07_MagicDivSigned_120: %d", num / 120);
	printf("test_07_MagicDivSigned_203: %d", num / 203);
	printf("test_07_MagicDivSigned_204: %d", num / 204);
	printf("test_07_MagicDivSigned_213: %d", num / 213);
	printf("test_07_MagicDivSigned_218: %d", num / 218);
	printf("test_07_MagicDivSigned_221: %d", num / 221);
	printf("test_07_MagicDivSigned_228: %d", num / 228);
	printf("test_07_MagicDivSigned_254: %d", num / 254);
	printf("test_07_MagicDivSigned_255: %d", num / 255);
	printf("test_07_MagicDivSigned_58441: %d", num / 0xE449);
	printf("test_07_MagicDivSigned_58442: %d", num / 0xE44A);
	printf("test_07_MagicDivSigned_58443: %d", num / 0xE44B);
	printf("test_07_MagicDivSigned_58444: %d", num / 0xE44C);
	printf("test_07_MagicDivSigned_58445: %d", num / 0xE44D);
	printf("test_07_MagicDivSigned_68441835: %d", num / 0x41456EB);
	printf("test_07_MagicDivSigned_68441836: %d", num / 0x41456EC);
	printf("test_07_MagicDivSigned_68441837: %d", num / 0x41456ED);
	printf("test_07_MagicDivSigned_68441838: %d", num / 0x41456EE);
	printf("test_07_MagicDivSigned_68441839: %d", num / 0x41456EF);
	printf("test_07_MagicDivSigned_68441840: %d", num / 0x41456F0);
	printf("test_07_MagicDivSigned_68441841: %d", num / 0x41456F1);
	printf("test_07_MagicDivSigned_68441842: %d", num / 0x41456F2);
	printf("test_07_MagicDivSigned_68441843: %d", num / 0x41456F3);
	return 7;
}


int __attribute__ ((noinline)) test_08_MagicDivSignedNegative(void)
{
	int num;
	scanf("%d", &num);
	printf("test_08_MagicDivSignedNegative_03: %d", num / -3);
	printf("test_08_MagicDivSignedNegative_05: %d", num / -5);
	printf("test_08_MagicDivSignedNegative_06: %d", num / -6);
	printf("test_08_MagicDivSignedNegative_07: %d", num / -7);
	printf("test_08_MagicDivSignedNegative_09: %d", num / -9);
	printf("test_08_MagicDivSignedNegative_10: %d", num / -10);
	printf("test_08_MagicDivSignedNegative_11: %d", num / -11);
	printf("test_08_MagicDivSignedNegative_12: %d", num / -12);
	printf("test_08_MagicDivSignedNegative_13: %d", num / -13);
	printf("test_08_MagicDivSignedNegative_14: %d", num / -14);
	printf("test_08_MagicDivSignedNegative_15: %d", num / -15);
	printf("test_08_MagicDivSignedNegative_17: %d", num / -17);
	printf("test_08_MagicDivSignedNegative_18: %d", num / -18);
	printf("test_08_MagicDivSignedNegative_19: %d", num / -19);
	printf("test_08_MagicDivSignedNegative_20: %d", num / -20);
	printf("test_08_MagicDivSignedNegative_29: %d", num / -29);
	printf("test_08_MagicDivSignedNegative_30: %d", num / -30);
	printf("test_08_MagicDivSignedNegative_31: %d", num / -31);
	printf("test_08_MagicDivSignedNegative_35: %d", num / -35);
	printf("test_08_MagicDivSignedNegative_47: %d", num / -47);
	printf("test_08_MagicDivSignedNegative_51: %d", num / -51);
	printf("test_08_MagicDivSignedNegative_57: %d", num / -57);
	printf("test_08_MagicDivSignedNegative_62: %d", num / -62);
	printf("test_08_MagicDivSignedNegative_70: %d", num / -70);
	printf("test_08_MagicDivSignedNegative_73: %d", num / -73);
	printf("test_08_MagicDivSignedNegative_89: %d", num / -89);
	printf("test_08_MagicDivSignedNegative_91: %d", num / -91);
	printf("test_08_MagicDivSignedNegative_94: %d", num / -94);
	printf("test_08_MagicDivSignedNegative_95: %d", num / -95);
	printf("test_08_MagicDivSignedNegative_99: %d", num / -99);
	printf("test_08_MagicDivSignedNegative_100: %d", num / -100);
	printf("test_08_MagicDivSignedNegative_101: %d", num / -101);
	printf("test_08_MagicDivSignedNegative_102: %d", num / -102);
	printf("test_08_MagicDivSignedNegative_120: %d", num / -120);
	printf("test_08_MagicDivSignedNegative_203: %d", num / -203);
	printf("test_08_MagicDivSignedNegative_204: %d", num / -204);
	printf("test_08_MagicDivSignedNegative_213: %d", num / -213);
	printf("test_08_MagicDivSignedNegative_218: %d", num / -218);
	printf("test_08_MagicDivSignedNegative_221: %d", num / -221);
	printf("test_08_MagicDivSignedNegative_228: %d", num / -228);
	printf("test_08_MagicDivSignedNegative_254: %d", num / -254);
	printf("test_08_MagicDivSignedNegative_255: %d", num / -255);
	printf("test_08_MagicDivSignedNegative_58441: %d", num / -0xE449);
	printf("test_08_MagicDivSignedNegative_58442: %d", num / -0xE44A);
	printf("test_08_MagicDivSignedNegative_58443: %d", num / -0xE44B);
	printf("test_08_MagicDivSignedNegative_58444: %d", num / -0xE44C);
	printf("test_08_MagicDivSignedNegative_58445: %d", num / -0xE44D);
	printf("test_08_MagicDivSignedNegative_68441835: %d", num / -0x41456EB);
	printf("test_08_MagicDivSignedNegative_68441836: %d", num / -0x41456EC);
	printf("test_08_MagicDivSignedNegative_68441837: %d", num / -0x41456ED);
	printf("test_08_MagicDivSignedNegative_68441838: %d", num / -0x41456EE);
	printf("test_08_MagicDivSignedNegative_68441839: %d", num / -0x41456EF);
	printf("test_08_MagicDivSignedNegative_68441840: %d", num / -0x41456F0);
	printf("test_08_MagicDivSignedNegative_68441841: %d", num / -0x41456F1);
	printf("test_08_MagicDivSignedNegative_68441842: %d", num / -0x41456F2);
	printf("test_08_MagicDivSignedNegative_68441843: %d", num / -0x41456F3);
	return 8;
}

int __attribute__ ((noinline)) test_09_MagicDivUnsinged(void)
{
	unsigned int num;
	scanf("%d", &num);
	printf("test_09_MagicDivUnsinged_03: %d", num / 3);
	printf("test_09_MagicDivUnsinged_05: %d", num / 5);
	printf("test_09_MagicDivUnsinged_06: %d", num / 6);
	printf("test_09_MagicDivUnsinged_07: %d", num / 7);
	printf("test_09_MagicDivUnsinged_09: %d", num / 9);
	printf("test_09_MagicDivUnsinged_10: %d", num / 10);
	printf("test_09_MagicDivUnsinged_11: %d", num / 11);
	printf("test_09_MagicDivUnsinged_12: %d", num / 12);
	printf("test_09_MagicDivUnsinged_13: %d", num / 13);
	printf("test_09_MagicDivUnsinged_14: %d", num / 14);
	printf("test_09_MagicDivUnsinged_15: %d", num / 15);
	printf("test_09_MagicDivUnsinged_17: %d", num / 17);
	printf("test_09_MagicDivUnsinged_18: %d", num / 18);
	printf("test_09_MagicDivUnsinged_19: %d", num / 19);
	printf("test_09_MagicDivUnsinged_20: %d", num / 20);
	printf("test_09_MagicDivUnsinged_29: %d", num / 29);
	printf("test_09_MagicDivUnsinged_30: %d", num / 30);
	printf("test_09_MagicDivUnsinged_31: %d", num / 31);
	printf("test_09_MagicDivUnsinged_35: %d", num / 35);
	printf("test_09_MagicDivUnsinged_47: %d", num / 47);
	printf("test_09_MagicDivUnsinged_51: %d", num / 51);
	printf("test_09_MagicDivUnsinged_57: %d", num / 57);
	printf("test_09_MagicDivUnsinged_62: %d", num / 62);
	printf("test_09_MagicDivUnsinged_70: %d", num / 70);
	printf("test_09_MagicDivUnsinged_73: %d", num / 73);
	printf("test_09_MagicDivUnsinged_89: %d", num / 89);
	printf("test_09_MagicDivUnsinged_91: %d", num / 91);
	printf("test_09_MagicDivUnsinged_94: %d", num / 94);
	printf("test_09_MagicDivUnsinged_95: %d", num / 95);
	printf("test_09_MagicDivUnsinged_99: %d", num / 99);
	printf("test_09_MagicDivUnsinged_100: %d", num / 100);
	printf("test_09_MagicDivUnsinged_101: %d", num / 101);
	printf("test_09_MagicDivUnsinged_102: %d", num / 102);
	printf("test_09_MagicDivUnsinged_120: %d", num / 120);
	printf("test_09_MagicDivUnsinged_203: %d", num / 203);
	printf("test_09_MagicDivUnsinged_204: %d", num / 204);
	printf("test_09_MagicDivUnsinged_213: %d", num / 213);
	printf("test_09_MagicDivUnsinged_218: %d", num / 218);
	printf("test_09_MagicDivUnsinged_221: %d", num / 221);
	printf("test_09_MagicDivUnsinged_228: %d", num / 228);
	printf("test_09_MagicDivUnsinged_254: %d", num / 254);
	printf("test_09_MagicDivUnsinged_255: %d", num / 255);
	printf("test_09_MagicDivUnsinged_58441: %d", num / 0xE449);
	printf("test_09_MagicDivUnsinged_58442: %d", num / 0xE44A);
	printf("test_09_MagicDivUnsinged_58443: %d", num / 0xE44B);
	printf("test_09_MagicDivUnsinged_58444: %d", num / 0xE44C);
	printf("test_09_MagicDivUnsinged_58445: %d", num / 0xE44D);
	printf("test_09_MagicDivUnsinged_68441835: %d", num / 0x41456EB);
	printf("test_09_MagicDivUnsinged_68441836: %d", num / 0x41456EC);
	printf("test_09_MagicDivUnsinged_68441837: %d", num / 0x41456ED);
	printf("test_09_MagicDivUnsinged_68441838: %d", num / 0x41456EE);
	printf("test_09_MagicDivUnsinged_68441839: %d", num / 0x41456EF);
	printf("test_09_MagicDivUnsinged_68441840: %d", num / 0x41456F0);
	printf("test_09_MagicDivUnsinged_68441841: %d", num / 0x41456F1);
	printf("test_09_MagicDivUnsinged_68441842: %d", num / 0x41456F2);
	printf("test_09_MagicDivUnsinged_68441843: %d", num / 0x41456F3);
	return 9;
}

int __attribute__ ((noinline)) test_10_XorMinusOne(void)
{
	int num;
	scanf("%d", &num);
	printf("test_10_XorMinusOne: %d", -num - 1);
	return 10;
}

int __attribute__ ((noinline)) test_11_SignedModulo(void)
{
	int num;
	scanf("%d", &num);
	printf("test_11_SignedModulo_02: %d", num % 2);
	printf("test_11_SignedModulo_03: %d", num % 3);
	printf("test_11_SignedModulo_04: %d", num % 4);
	printf("test_11_SignedModulo_05: %d", num % 5);
	printf("test_11_SignedModulo_06: %d", num % 6);
	printf("test_11_SignedModulo_07: %d", num % 7);
	printf("test_11_SignedModulo_08: %d", num % 8);
	printf("test_11_SignedModulo_09: %d", num % 9);
	printf("test_11_SignedModulo_10: %d", num % 10);
	printf("test_11_SignedModulo_11: %d", num % 11);
	printf("test_11_SignedModulo_12: %d", num % 12);
	printf("test_11_SignedModulo_13: %d", num % 13);
	printf("test_11_SignedModulo_14: %d", num % 14);
	printf("test_11_SignedModulo_15: %d", num % 15);
	printf("test_11_SignedModulo_16: %d", num % 16);
	printf("test_11_SignedModulo_17: %d", num % 17);
	printf("test_11_SignedModulo_18: %d", num % 18);
	printf("test_11_SignedModulo_19: %d", num % 19);
	printf("test_11_SignedModulo_20: %d", num % 20);
	printf("test_11_SignedModulo_29: %d", num % 29);
	printf("test_11_SignedModulo_30: %d", num % 30);
	printf("test_11_SignedModulo_31: %d", num % 31);
	printf("test_11_SignedModulo_35: %d", num % 35);
	printf("test_11_SignedModulo_47: %d", num % 47);
	printf("test_11_SignedModulo_51: %d", num % 51);
	printf("test_11_SignedModulo_57: %d", num % 57);
	printf("test_11_SignedModulo_62: %d", num % 62);
	printf("test_11_SignedModulo_70: %d", num % 70);
	printf("test_11_SignedModulo_73: %d", num % 73);
	printf("test_11_SignedModulo_89: %d", num % 89);
	printf("test_11_SignedModulo_91: %d", num % 91);
	printf("test_11_SignedModulo_94: %d", num % 94);
	printf("test_11_SignedModulo_95: %d", num % 95);
	printf("test_11_SignedModulo_99: %d", num % 99);
	printf("test_11_SignedModulo_100: %d", num % 100);
	printf("test_11_SignedModulo_101: %d", num % 101);
	printf("test_11_SignedModulo_102: %d", num % 102);
	printf("test_11_SignedModulo_128: %d", num % 128);
	printf("test_11_SignedModulo_120: %d", num % 120);
	printf("test_11_SignedModulo_203: %d", num % 203);
	printf("test_11_SignedModulo_204: %d", num % 204);
	printf("test_11_SignedModulo_213: %d", num % 213);
	printf("test_11_SignedModulo_218: %d", num % 218);
	printf("test_11_SignedModulo_221: %d", num % 221);
	printf("test_11_SignedModulo_228: %d", num % 228);
	printf("test_11_SignedModulo_254: %d", num % 254);
	printf("test_11_SignedModulo_255: %d", num % 255);
	printf("test_11_SignedModulo_256: %d", num % 256);
	printf("test_11_SignedModulo_58441: %d", num % 0xE449);
	printf("test_11_SignedModulo_58442: %d", num % 0xE44A);
	printf("test_11_SignedModulo_58443: %d", num % 0xE44B);
	printf("test_11_SignedModulo_58444: %d", num % 0xE44C);
	printf("test_11_SignedModulo_58445: %d", num % 0xE44D);
	printf("test_11_SignedModulo_68441835: %d", num % 0x41456EB);
	printf("test_11_SignedModulo_68441836: %d", num % 0x41456EC);
	printf("test_11_SignedModulo_68441837: %d", num % 0x41456ED);
	printf("test_11_SignedModulo_68441838: %d", num % 0x41456EE);
	printf("test_11_SignedModulo_68441839: %d", num % 0x41456EF);
	printf("test_11_SignedModulo_68441840: %d", num % 0x41456F0);
	printf("test_11_SignedModulo_68441841: %d", num % 0x41456F1);
	printf("test_11_SignedModulo_68441842: %d", num % 0x41456F2);
	printf("test_11_SignedModulo_68441843: %d", num % 0x41456F3);
	return 11;
}

int __attribute__ ((noinline)) test_12_UnsignedModulo(void)
{
	unsigned int num;
	scanf("%d", &num);
	printf("test_12_UnsignedModulo_02: %d", num % 2);
	printf("test_12_UnsignedModulo_03: %d", num % 3);
	printf("test_12_UnsignedModulo_04: %d", num % 4);
	printf("test_12_UnsignedModulo_05: %d", num % 5);
	printf("test_12_UnsignedModulo_06: %d", num % 6);
	printf("test_12_UnsignedModulo_07: %d", num % 7);
	printf("test_12_UnsignedModulo_08: %d", num % 8);
	printf("test_12_UnsignedModulo_09: %d", num % 9);
	printf("test_12_UnsignedModulo_10: %d", num % 10);
	printf("test_12_UnsignedModulo_11: %d", num % 11);
	printf("test_12_UnsignedModulo_12: %d", num % 12);
	printf("test_12_UnsignedModulo_13: %d", num % 13);
	printf("test_12_UnsignedModulo_14: %d", num % 14);
	printf("test_12_UnsignedModulo_15: %d", num % 15);
	printf("test_12_UnsignedModulo_16: %d", num % 16);
	printf("test_12_UnsignedModulo_17: %d", num % 17);
	printf("test_12_UnsignedModulo_18: %d", num % 18);
	printf("test_12_UnsignedModulo_19: %d", num % 19);
	printf("test_12_UnsignedModulo_20: %d", num % 20);
	printf("test_12_UnsignedModulo_29: %d", num % 29);
	printf("test_12_UnsignedModulo_30: %d", num % 30);
	printf("test_12_UnsignedModulo_31: %d", num % 31);
	printf("test_12_UnsignedModulo_35: %d", num % 35);
	printf("test_12_UnsignedModulo_47: %d", num % 47);
	printf("test_12_UnsignedModulo_51: %d", num % 51);
	printf("test_12_UnsignedModulo_57: %d", num % 57);
	printf("test_12_UnsignedModulo_62: %d", num % 62);
	printf("test_12_UnsignedModulo_70: %d", num % 70);
	printf("test_12_UnsignedModulo_73: %d", num % 73);
	printf("test_12_UnsignedModulo_89: %d", num % 89);
	printf("test_12_UnsignedModulo_91: %d", num % 91);
	printf("test_12_UnsignedModulo_94: %d", num % 94);
	printf("test_12_UnsignedModulo_95: %d", num % 95);
	printf("test_12_UnsignedModulo_99: %d", num % 99);
	printf("test_12_UnsignedModulo_100: %d", num % 100);
	printf("test_12_UnsignedModulo_101: %d", num % 101);
	printf("test_12_UnsignedModulo_102: %d", num % 102);
	printf("test_12_UnsignedModulo_128: %d", num % 128);
	printf("test_12_UnsignedModulo_120: %d", num % 120);
	printf("test_12_UnsignedModulo_203: %d", num % 203);
	printf("test_12_UnsignedModulo_204: %d", num % 204);
	printf("test_12_UnsignedModulo_213: %d", num % 213);
	printf("test_12_UnsignedModulo_218: %d", num % 218);
	printf("test_12_UnsignedModulo_221: %d", num % 221);
	printf("test_12_UnsignedModulo_228: %d", num % 228);
	printf("test_12_UnsignedModulo_254: %d", num % 254);
	printf("test_12_UnsignedModulo_255: %d", num % 255);
	printf("test_12_UnsignedModulo_256: %d", num % 256);
	printf("test_12_UnsignedModulo_58441: %d", num % 0xE449);
	printf("test_12_UnsignedModulo_58442: %d", num % 0xE44A);
	printf("test_12_UnsignedModulo_58443: %d", num % 0xE44B);
	printf("test_12_UnsignedModulo_58444: %d", num % 0xE44C);
	printf("test_12_UnsignedModulo_58445: %d", num % 0xE44D);
	printf("test_12_UnsignedModulo_68441835: %d", num % 0x41456EB);
	printf("test_12_UnsignedModulo_68441836: %d", num % 0x41456EC);
	printf("test_12_UnsignedModulo_68441837: %d", num % 0x41456ED);
	printf("test_12_UnsignedModulo_68441838: %d", num % 0x41456EE);
	printf("test_12_UnsignedModulo_68441839: %d", num % 0x41456EF);
	printf("test_12_UnsignedModulo_68441840: %d", num % 0x41456F0);
	printf("test_12_UnsignedModulo_68441841: %d", num % 0x41456F1);
	printf("test_12_UnsignedModulo_68441842: %d", num % 0x41456F2);
	printf("test_12_UnsignedModulo_68441843: %d", num % 0x41456F3);
	return 12;
}

int __attribute__ ((noinline)) test_13_FloatNeg(void)
{
	float num;
	scanf("%f", &num);
	printf("test_13_FloatNeg: %f", -num);
	return 13;
}

int __attribute__ ((noinline)) test_14_CopySign(void)
{
	float a, m, c;
	scanf("%f %f %f", &a, &c, &m);
	a = copysign(m, c);
	printf("test_14_CopySign: %f", a);
	return 14;
}

int __attribute__ ((noinline)) test_15_FloatAbs(void)
{
	float num;
	scanf("%f", &num);
	num = fabs(num);
	printf("test_15_FloatAbs: %f", num);
	return 15;
}

int main(void)
{
	test_01_LessThanZero();
	test_02_GreaterEqualZero();
	test_03_XorAssignZero();
	test_04_BitShiftMult();
	test_05_DivByMinusTwo();
	test_06_BitShiftDiv();
	test_07_MagicDivSigned();
	test_08_MagicDivSignedNegative();
	test_09_MagicDivUnsinged();
	test_10_XorMinusOne();
	test_11_SignedModulo();
	test_12_UnsignedModulo();
	test_13_FloatNeg();
	test_14_CopySign();
	test_15_FloatAbs();
	return 0;
}
