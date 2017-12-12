#include <stdio.h>
#include <stdlib.h>

int gcd1(int a, int b) {
    while( 1 ) {
        a = a % b;
		if (a == 0)
			return b;
		b = b % a;

        if (b == 0)
			return a;
    }
}

int gcd2(int m, int n) {
  int t, r;

  if (m < n) {
    t = m;
    m = n;
    n = t;
  }

  r = m % n;

  if (r == 0) {
    return n;
  } else {
    return gcd2(n, r);
  }
}

int gcd3(int a, int b) {
	int remainder;

	while (b != 0) {
		remainder = a % b;
		a = b;
		b = remainder;
	}

	return a;
}
int main(int argc,char *argv[])
{
	int a = 0, b = 0;
	scanf("%d %d", &a, &b);
	int res1 = gcd1(a, b);
	printf("gcd1 %d %d = %d\n", a, b, res1);
	int res2 = gcd2(b, a);
	printf("gcd2 %d %d = %d\n", b, a, res2);
	int res3 = gcd3(b, a);
	printf("gcd3 %d %d = %d\n", b, a, res3);
	return  (res1 != res2) || (res1 != res3) ;
}
