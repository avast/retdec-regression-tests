#include <stdio.h>

class Base1
{
	public:
		Base1() : val1(0)      { printf("Base1::Base1()\n"); }
		Base1(int v) : val1(v) { printf("Base1::Base1(int v)\n"); }
		virtual ~Base1()       { printf("Base1::~Base1()\n"); }

		virtual void method1() { printf("Base1::method1()\n"); }
		virtual int  methodx() { printf("Base1::methodx() : val1=%d\n", val1); return val1; }

	public:
		int val1;
};

class Base2
{
	public:
		Base2() : val2(0)      { printf("Base2::Base2()\n"); }
		Base2(int v) : val2(v) { printf("Base2::Base2(int v)\n"); }
		virtual ~Base2()       { printf("Base2::~Base2()\n"); }

		virtual void method2() { printf("Base2::method2()\n"); }
		virtual int  methodx() { printf("Base2::methodx() : val2=%d\n", val2); return val2; }
		virtual void methody() { printf("Base2::methody() : val2=%d\n", val2); }

	public:
		char val2;
};

class Derived : public Base1, public Base2
{
	public:
		Derived() : val3(0)    { printf("Derived::Derived()\n"); }
		Derived(int v1, int v2, int v3) :
			Base1(v1),
			Base2(v2),
			val3(v3)           { printf("Derived::Derived(int v1, int v2, int v3)\n"); }
		virtual ~Derived()     { printf("Derived::~Derived()\n"); }

		virtual void method3() { printf("Derived::method3()\n"); }
		virtual int  methodx() { printf("Derived::methodx() : %d %d %d\n", val1, val2, val3); return val3; }
		virtual void methody() { printf("Derived::methody() : %d %d %d\n", val1, val2, val3); }

	public:
		char val3;
};

int main()
{
	printf("Base1 test:\n");
	Base1* b1 = new Base1(10);
	b1->method1();
	b1->methodx();
	delete b1;

	printf("Base2 test:\n");
	Base2* b2 = new Base2(20);
	b2->method2();
	b2->methodx();
	b2->methody();
	delete b2;

	printf("Derived test:\n");
	Derived* d = new Derived(10, 20, 30);
	d->method1();
	d->method2();
	d->method3();
	d->methodx();
	d->methody();

	printf("Down assignment to Base1:\n");
	b1 = d;
	b1->methodx();

	printf("Down assignment to Base2:\n");
	b2 = d;
	b2->methodx();

	return 0;
}