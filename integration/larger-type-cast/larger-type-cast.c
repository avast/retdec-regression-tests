#include <stdio.h>
#include <stdint.h>

int16_t u = 3;

int main()
{
	scanf("%hd", &u);
	printf("You typed %d\n", (int32_t)u);

	return 0;
}
