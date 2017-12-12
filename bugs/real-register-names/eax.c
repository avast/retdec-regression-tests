
// test.c
#include <stdio.h>

int ebx = 1;
int _ebx = 2;
int __ebx = 3;

int eax() {
    printf("hello %d", ebx);
}

int _eax() {
    printf("hello %d", _ebx);
}

int __eax() {
    printf("hello %d", __ebx);
}

int main(int argc, char **argv) {
    eax();
    _eax();
    __eax();
    return 0;
}

