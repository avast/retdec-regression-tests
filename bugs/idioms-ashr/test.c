//
// Created from https://github.com/avast/retdec/issues/724
// Author: adahsuzixin
//

#include <stdio.h>

char getSecondByte(long long a);

int main(void)
{
	long long a;
	scanf("%llx", &a);
	char res = getSecondByte(a);
	printf("getSecondByte( %llx ) = %d\n",a,res);
	return res;
}

char getSecondByte(long long a) {
	return (a >> 8) & 0xff;
}
