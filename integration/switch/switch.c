// Switch test

#include <stdio.h>
#include <stdlib.h>

int x;

void func1a() {
	switch (x) {
		default:
			printf("%d", x);

		case 0:
			printf(" 0 ");
			break;

		case 1:
			printf(" 1 ");
			break;
	}
	printf("after");
}

void func1b() {
	switch (x) {
		default:
			printf("%d", x);
			break;

		case 0:
			printf(" 0 ");
			break;

		case 1:
			printf(" 1 ");
			break;
	}
	printf("after");
}

void func2a() {
	switch (x) {
		case 0:
			printf(" 0 ");
			break;

		case 1:
			printf(" 1 ");

		default:
			printf("%d", x);
	}
	printf("after");
}

void func2b() {
	switch (x) {
		case 0:
			printf(" 0 ");
			break;

		case 1:
			printf(" 1 ");

		default:
			printf("%d", x);
			break;
	}
	printf("after");
}

void func3a() {
	switch (x) {
		case 0:

			printf(" 0 ");
			break;

		case 1:
			printf(" 1 ");
			break;

		default:
			printf("%d", x);
	}
	printf("after");
}

void func3b() {
	switch (x) {
		case 0:
			printf(" 0 ");
			break;

		case 1:
			printf(" 1 ");
			break;

		default:
			printf("%d", x);
			break;
	}
	printf("after");
}

void func4() {
	switch (x) {
		case 0:
			printf(" 0 ");

		default:
			printf("%d", x);

		case 22:
			printf(" 22 ");
			break;
	}
	printf("after");
}

/**
 * Test switch with jump table.
 */
void jump_table() {
	printf(" before ");

	switch (x) {
		case 20:
			printf(" 20 "); break;
		case 21:
			printf(" 21 "); break;
		case 22:
			printf(" 22 "); break;
		case 23:
			printf(" 23 "); break;
		case 24:
			printf(" 24 "); break;
		case 25:
			printf(" 25 "); break;
		case 28:
			printf(" 28 "); break;
		default:
			printf(" %d ", x); break;
	}

	printf(" after ");
}

/**
 *
 */
void jump_table_2() {

	printf(" before jump table 2 ");

	switch (rand())
	{
		case 0:
			printf(" 0 \n"); break;
		case 2:
		case 3:
			printf(" 2, 3 \n"); break;
		case 5:
			printf(" 5 \n"); break;
		case 8:
			printf(" 8 \n"); break;
		case 57:
			printf(" 57 \n"); break;
		default:
			printf(" break \n"); break;
			break;
	}

	printf(" after jumpt table 2 ");
}

int main(int argc,char *argv[])
{
	x = 0;
	scanf("%d", &x);
	func1a();
	func1b();
	func2a();
	func2b();
	func3a();
	func3b();
	func4();
	jump_table();
//	jump_table_2();

	return 0;
}
