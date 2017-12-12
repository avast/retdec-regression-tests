
#include <stdio.h>
#include <stdlib.h>

unsigned fib(int x)                 /* compute fibonacci number recursively */
{
    if (x > 2)
        return (fib(x - 1) + fib(x - 2));
    else
        return (1);
}

int main(int argc, char *argv[])
{
	int i, numtimes = 0, number = 0;
	unsigned value;

	printf("Input number of iterations: ");
	scanf ("%d", &numtimes);
	for (i = 1; i <= numtimes; i++)
	{
		printf ("Input number: ");
		scanf ("%d", &number);
		value = fib(number);
		printf("fibonacci(%d) = %u\n", number, value);
	}
	return 0;
}

