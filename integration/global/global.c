#include <stdio.h>

// variable only for read
const int g0 = 123456;
const int g2 = 456789;

// variable for read and write
int g3 = 654321;
int g1 = 987654;

int main() {
	printf("%d\n", g0);
	printf("%d\n", g2);

	printf("%d\n", g3);
	scanf("%d", &g3);
	printf("%d\n", g3);

	printf("%d\n", g1);
	scanf("%d", &g1);
	printf("%d\n", g1);

	return 0;
}
