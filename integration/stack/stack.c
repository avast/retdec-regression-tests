// Various summation functions

#include <stdio.h>

int my_sum1(int a) {
    int x = rand();
    int y = rand();
    int z = x - y;
    return (x + y) * (a + z);
}


int my_sum2(int a) {
    int x = rand();
    int y = rand();
    int z = x + y - 3;
    return 4 * z + a;
}

int main(int argc, char **argv) {
    int a = 0;
    int b = 0;
    int c = 0;
    int d = 0;
    scanf("%d %d %d", &a, &b, &d);

    if (a > b) {
        printf("hello");
        c = my_sum1(a);
    } else {
        printf("greetings");
        c = my_sum2(b);
    }

    return a - b - (c + d);
}
