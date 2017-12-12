#include <stdio.h>

int func() {
	int i = printf("%s\n");
	return i;
}

int main() {
	return func();
}
