

#include <stdio.h>
#include <stdlib.h> /* atoi() */

static unsigned int calls;


unsigned int naive_ackermann(unsigned int m, unsigned int n) {
    calls++;
    if (m == 0)
        return n + 1;
    else if (n == 0)
        return naive_ackermann(m - 1, 1);
    else
        return naive_ackermann(m - 1, naive_ackermann(m, n - 1));
}


unsigned int iterative_ackermann(unsigned int m, unsigned int n) {
    calls++;
    while (m != 0) {
        if (n == 0) {
            n = 1;
        } else {
            n = iterative_ackermann(m, n - 1);
        }
        m--;
    }
    return n + 1;
}


unsigned int formula_ackermann(unsigned int m, unsigned int n) {
    calls++;
    while(1) {

// Matula:
// Old implementation was using switch, which is not handled on some architectures.
// New implementation is using if-then-else, which should work everywhere.
//
//         switch(m) {
//         case 0:  return n + 1;
//         case 1:  return n + 2;
//         case 2:  return (n << 1) + 3;
//         case 3:  return (1 << (n+3)) - 3;
//         default:
//             if (n == 0) {
//                 n = 1;
//             } else {
//                 n = formula_ackermann(m, n - 1);
//             }
//             m--;
//             break;
//         }

        if (m == 0)
        {
            return n + 1;
        }
        else if (m == 1)
        {
            return n + 2;
        }
        else if (m == 2)
        {
            return (n << 1) + 3;
        }
        else if (m == 3)
        {
            return (1 << (n+3)) - 3;
        }
        else
        {
            if (n == 0) {
                n = 1;
            } else {
                n = formula_ackermann(m, n - 1);
            }
            m--;
        }
    }
}


int main(int argc, char* argv[]) {
	unsigned int m, n, result;

	scanf("%d %d",&m,&n);

	m = m % 4 + 1;
	n = n % 3 + 1;

	calls = 0;
	result = naive_ackermann(m, n);
	printf("Naive:     %u (%u calls)\n", result, calls);

	calls = 0;
	result = iterative_ackermann(m, n);
	printf("Iterative: %u (%u calls)\n", result, calls);

	calls = 0;
	result = formula_ackermann(m, n);
	printf("Formula:   %u (%u calls)\n", result, calls);

	return 0;
}

