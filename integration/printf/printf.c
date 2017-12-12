#include <stdio.h>

int main() {
	printf("%.*s", 4, "abcd");
	printf("%*s", 4, "abcd");
	printf("%.*d", 4, 1);
	printf("%*d", 4, 1);
	printf("%#o", 1);
	printf("% d", 1);
	printf("%-d", 1);
	printf("%+d", 1);
	printf("% .4d", 1);
	printf("%-.44ho\n", 1);
	printf("%*.*s\n", 55, 66, "abcd");
	return 0;
}
