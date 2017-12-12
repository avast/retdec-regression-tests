#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// This piece of code tests that variables are allocated before they are used
// in a function call.
double func(double x) {
   double fracPart, intPart;

   fracPart = modf(x, &intPart);
   return fabs(intPart);
}

int main(int argc,char *argv[])
{
	double res ,x ;
#ifdef PIC32
	scanf("%f", &x);
#else
	scanf("%lf", &x);
#endif
	res = func(x);
	printf("func( %.3lf ) = %lf\n", x, res);
	return res;
}
