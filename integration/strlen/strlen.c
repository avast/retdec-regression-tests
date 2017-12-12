#include <stdlib.h>
#include <stdio.h>

size_t my_strlen(const char * str) {
    const char *s;
    for (s = str; *s; ++s);
    return(s - str);
}

int main(int argc,char *argv[])
{
	char text[256];
	scanf("%s",text);
	size_t len = my_strlen(text);
	printf("%d\n", len);
	return ( len );
}
