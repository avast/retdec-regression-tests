#include <stdio.h>
#include <stdlib.h>

int fib(int n) {
  if (n == 1) return 0;
  if (n == 2) return 1;
  return fib(n - 1) + fib(n - 2);
}

int main(int argc, char *argv[]) {
  int x = rand();
  int res = fib(x);
  printf("fib(%d) = %d\n", x, res);
  return res;
}
