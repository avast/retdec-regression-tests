#include <stdio.h>

class ClassA
{
	public:
		ClassA() :  a(1), b(2)      { printf("ClassA::ClassA\n"); }
		~ClassA()                   { printf("~ClassA::ClassA\n"); }
		virtual void doSomething()  { printf("%i %i\n", a, b); }

	public:
		int a, b;
};

int main()
{
	ClassA *a = new ClassA();
	a->doSomething();
	a->a = 3;
	a->b = 4;
	a->doSomething();

	delete a;

	return 0;
}
