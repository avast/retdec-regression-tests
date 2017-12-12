#include <stdio.h>

void gpr0(int i) {
    printf("%d\n", i);
}

int main(int argc, char **argv) {
    gpr0(argc);
    return 0;
}
