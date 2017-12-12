#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define  MAXLEN 256

void rev(char* source, char* destination)
{
  char* tmp = destination + strlen(source);
  for (*tmp-- = 0; *source; *tmp-- = *source++)
    ;
}

int main(int argc, char**argv)
{
  char* original = NULL;
  char* reverse = NULL;

  original = malloc( sizeof(char)*MAXLEN );
  reverse  = malloc( sizeof(char)*MAXLEN );

  while( scanf("%s",original) == 1 )
  {
     rev(original, reverse);
     if (0 == strcmp(original, reverse))
     {
        printf("%s is a palindrome\n", original);
     }
     else
     {
        printf("Try again! (%s)\n", original);
     }
   }

   free(original);
   free(reverse);

   return 0;
}
