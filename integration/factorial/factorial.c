

#include <stdio.h>

int factorial(int n) {
    if (n == 0)
        return 1;
    return n*factorial(n-1);
}


int main(int argc,char *argv[])
{
	int x;
	while(scanf("%d", &x) == 1)
	{
		int res = factorial(x);
		printf("factorial( %d ) = %d\n", x, res);
	}
	return 0;
}
