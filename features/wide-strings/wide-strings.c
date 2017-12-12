
#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include <wchar.h>

#define BUFFER_SIZE 1024

int main()
{
    FILE* f;
    wchar_t str[BUFFER_SIZE];
    size_t  strSize;

    if ((f = fopen( "d:\\1.txt", "wb")) == NULL) // C4996
    {
        wprintf(L"fopen failed!\n");
        return(0);
    }

    if (fclose(f))
    {
        wprintf(L"fclose failed!\n");
    }

    wprintf(L"");
    wprintf(L"ab");
    wprintf(L"X č \n");

    return 0;
}
