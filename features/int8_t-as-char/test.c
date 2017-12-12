#include <stdio.h>

// In the test, we check that the type of the parameter is char *.
void print(char *s) {
	printf("%s\n", s);
}

int main() {
	print("hello world");
	return 0;
}
