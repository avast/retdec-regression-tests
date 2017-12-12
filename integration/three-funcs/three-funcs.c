// Three summing functions

#include <stdio.h>

int man(int a, int b) {
    return a + b;
}

int dan(int a, int b) {
    return a + b;
}

int zan(int a, int b) {
    return a + b;
}

int main(int argc, char **argv) __attribute__((optimize("-O0")));

int main(int argc, char **argv) {
    int a = 5;
    int b = 10;
    int c = man(a, b);
    int d = dan(a, c);
    int e = zan(c, d);
    return e;
}
