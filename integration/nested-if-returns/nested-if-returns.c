#include <stdio.h>
#include <stdlib.h>



int func() {
	int x = 0, y = 0, z = 0;
	scanf("%d %d %d", &x, &y, &z);


	if (x) {
		if (y) {
			if (z) {
				printf("XYZ\n");
				return 4;
			}
			printf("XY\n");
			return 3;
		}
		printf("X\n");
		return 2;
	} else {
		if (y) {
			if (z) {
				printf("XYZ\n");
				return 4;
			}
			printf("XY\n");
			return 3;
		}
		printf("X\n");
		return 2;
	}
}

int main()
{
	return func();
}
