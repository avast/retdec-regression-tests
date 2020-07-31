#include <stdio.h>
#include <stdlib.h>

int g = 100;

int f1();
int f2();
int f3();

int main() {
	g = 100;
	f1();
	f2();
	f3();
	return 0;
}

int f1() {
	int i;
	for (i = 0; i < g; ++i) {
		printf("looping");
	}
	return 0;
}

int f2() {
	int i;
	for (i = 0; i < rand(); ++i) {
		printf("looping %d", i);
	}
	return 0;
}

int f3() {
	int i;
	for (i = 0; i < rand(); ++i) {
		printf("looping");
	}
	return 0;
}
