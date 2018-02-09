//
// The input source file of lib.so.
//
// Compilation:
//
//    gcc -m32 -shared -o lib.so lib.c
//

#include <stdio.h>

// Will be marked as exported.
void my_func() {
	printf("my_func");
}

int main() {
	return 0;
}
