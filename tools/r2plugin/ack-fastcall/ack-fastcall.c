#include <stdio.h>
#include <stdlib.h>

unsigned int __attribute__((fastcall)) ack(unsigned int m, unsigned int n) {
	if (m == 0)
		return n + 1;
	else if (n == 0)
		return ack(m - 1, 1);
	else
		return ack(m - 1, ack(m, n - 1));
}

int main(int argc,char *argv[])
{
 	unsigned int res = 0, x = 0, y = 0;


	scanf("%d %d",&x,&y);
	res = ack(x ,y);
	printf("ackerman( %d , %d ) = %d\n",x,y,res);
	return res;
}
