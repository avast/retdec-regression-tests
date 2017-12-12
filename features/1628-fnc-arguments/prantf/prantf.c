//
// To create test binaries this needs to be compiled and manually modified by
// hex editor -- change all "printf" strings to "prantf" strings to prevent
// correct LTI signature application.
//

#include <stdio.h>

int main(int argc, char **argv) {
    printf("My number is %d.", 1);
    return 0;
}
