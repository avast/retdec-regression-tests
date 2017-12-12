
#include <stdio.h>


int pokus(int a, int b, int c, int d, int e, int f, int g, int h, int i, float j, char k)
{
	printf("DIV: %d, MOD: %d, MUL: %d, ADD: %d, SUB: %d, other: %d, %d, %d, %d, %f. Char: %c\n",
	       a, b, c, d, e, f, g, h, i, j, k);
	return a * b;
}


int main(int argc, char *arg[])
{
	int a = 1, b = 1;
	int count = scanf("%d %d", &a, &b);
	if (count != 2)
	{
		printf("Chyba vstupu, nacitanych %d\n", count);
		return 1;
	}
	printf("Mam %d a %d\n", a, b);

	int res = pokus(a / b, a % b, a * b, a + b, a - b, a * (b-2), a * (b-3), a * (b-4), a * (b-5), a * (b-6), 'X');
	printf("Special number: %d\n", res);
	return 0;
}

