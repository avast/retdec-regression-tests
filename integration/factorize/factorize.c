#include <stdio.h>

/* Find out the prime factors of a given number and print them on the screen */
void factorize(int n) {
	if (n < 2)
		return;

	printf("Prime factors of '%d': ", n);
	/* while the factor being tested is lower than the number to factorize */
	int d = 2;
	while (d < n) {
		/* if valid prime factor */
		if (n % d == 0) {
			printf("%d x ", d);
			n /= d;
		}
		/* else: invalid prime factor */
		else {
			if (d == 2)
				d = 3;
			else
				d += 2;
		}
	}

	/* print last prime factor */
	printf("%d\n", d);
}

int main(int argc,char *argv[])
{
	int x;
	while( scanf("%d",&x) == 1 )
		factorize(x);
	return 0;
}
