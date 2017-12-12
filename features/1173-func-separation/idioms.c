#include <stdio.h>
#include <math.h>

int __attribute__ ((noinline)) test_15_FloatAbs(void)
{
	float num;
	scanf("%f", &num);
	num = fabsf(num);
	printf("test_15_FloatAbs: %f", num);
	return 15;
}

int main(void)
{
	test_15_FloatAbs();
	return 0;
}
