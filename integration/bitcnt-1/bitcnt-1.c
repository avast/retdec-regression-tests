
#include <stdio.h>


int  bit_count(long x)
{
        int n = 0;
/*
** The loop will execute once for each bit of x set, this is in average
** twice as fast as the shift/test method.
*/
        if (x) do
              n++;
        while (0 != (x = x&(x-1))) ;
        return(n);
}


#include <stdlib.h>


int main(int argc, char *argv[])
{
      int n = 0;

      while(scanf("%d", &n)==1)
      {
            int i = bit_count(n);
            printf("%d contains %d bit set\n", n, i);
      }
      return 0;
}


