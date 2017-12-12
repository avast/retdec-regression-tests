#include <stdio.h>
#include <stdlib.h>

int g = 100;

int f1();
int f2();
int f3();
int f4();
int f5();
int f6();
int f7();
int f8();
int f9();
int f10();

int main() {
	g = 100;
	f1();
	f2();
	f3();
	f4();
	f5();
	f6();
	f7();
	f8();
	f9();
	f10();
	return 0;
}

int f1() {
	int i;
	for (i = 0; i < 100; ++i) {
		printf("looping");
	}
	return 0;
}

int f2() {
	int i;
	for (i = 0; i < 100; ++i) {
		printf("looping %d", i);
	}
	return 0;
}

int f3() {
	int i;
	for (i = 1; i < 100; ++i) {
		printf("looping");
	}
	return 0;
}

int f4() {
	int i;
	for (i = 1; i < 100; ++i) {
		printf("looping %d", i);
	}
	return 0;
}

int f5() {
	int i;
	for (i = 0; i < g; ++i) {
		printf("looping");
	}
	return 0;
}

int f6() {
	int i;
	for (i = 0; i < g; ++i) {
		printf("looping %d", i);
	}
	return 0;
}

int f7() {
	int i;
	for (i = 0; i < rand(); ++i) {
		printf("looping %d", i);
	}
	return 0;
}

int f8() {
	int i;
	for (i = 0; i < rand(); ++i) {
		printf("looping");
	}
	return 0;
}

int f9() {
	int i;
	for (i = 100; i > 0; --i) {
		printf("looping");
	}
	return 0;
}

int f10() {
	int i;
	for (i = 100; i > 1; --i) {
		printf("looping %d", i);
	}
	return 0;
}
