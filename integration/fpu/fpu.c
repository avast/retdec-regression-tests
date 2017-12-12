
#include <stdio.h>
#include <stdlib.h>

void comp_const_const()
{
	float f1 = 1.23;

	if (f1 > 3.14)
	{
		printf("#1 %f\n", f1);
	}
	else
	{
		printf("#2 %f\n", 3.14);
	}
}

void comp_scanf_const()
{
	float f1;
	scanf("%f", &f1);

	if (f1 > 3.14)
	{
		printf("%f\n", f1);
	}
	else
	{
		printf("%f\n", 3.14);
	}
}

void comp_scanf_scanf()
{
	float f1;
	float f2;
	scanf("%f", &f1);
	scanf("%f", &f2);

	if (f1 > f2)
	{
		printf("%f\n", f1);
	}
	else
	{
		printf("%f\n", f2);
	}
}

int main(void)
{
	comp_const_const();
	comp_scanf_const();
	comp_scanf_scanf();

	return 0;
}
