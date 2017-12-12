
#include <stdio.h>


float op1(int a, int b)
{
	printf("mul by %f\n", 3.789);
	return a + b * 3.789;
}

float op2(int a, int b)
{
	printf("div\n");
	// TODO: try 1.5 here. It behaves differently on ARM. The number is created
	// by assigning its part into registers 2:3. We are not able to reconstruct
	// such a constant now. Moreover the order of registers differs on PE and ELF
	return a / (b * 1.6);
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
	printf("%d a %d\n", a, b);

	float f = op1(a, b);
	printf("Result1 : %.2f\n", f);
	
	float f2 = op2(b, a);
	printf("Result2 : %f\n", f2);
	
	printf("%d / 2.33 = %.2f\n", a, a / 2.33);
	
	return 0;
}

