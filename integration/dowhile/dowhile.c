#include <stdio.h>


int main(int argc, char *argv[])
{
	int a = 1;
	int b = 0;

	scanf("%d", &b);
	printf("Read %d\n", b);
	do {
		if (b == 2)
		  break;
		a++;
		b++;
	} while(a < 10);
	printf("Return %d\n", a);
	return a;
}
