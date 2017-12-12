//
// Source code for debug-info.exe.
// decompile.sh debug-info.c -g -C -O0
//

#include <stdio.h>

int g = 1;

int func(int a) {
	int c = a + rand();
	printf("%d\n", c);
	return g + c + a;
}

int main() {
	int h = rand();
	func(h);
	func(h);
	return g;
}
