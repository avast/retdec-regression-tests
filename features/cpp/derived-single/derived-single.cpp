#include <stdio.h>

class Base
{
	public:
		Base()                 { printf("Base::Base\n"); }
		virtual ~Base()        { printf("Base::~Base\n"); }
		virtual void method1() { printf("Base::method1 : %d\n", a); }

	public:
		int a;
};

class Derived : public Base
{
	public:
		Derived()              { printf("Derived::Derived\n"); }
		~Derived()             { printf("Derived::~Derived\n"); }
		virtual void method1() { printf("Derived::method1 : %d %d\n", a, b); }
		virtual void method2() { printf("Derived::method2 : %d %d\n", a, b); }

	public:
		int b;
};

void dumpBase(Base* b)
{
	printf("Dump Base %d\n", b->a);
}


void dumpDerived(Derived* d)
{
	printf("Dump Derived %d %d\n", d->a, d->b);
}

int main()
{
	printf("Base test:\n");
	Base* b = new Base();
	b->a = 1;
	b->method1();
	dumpBase(b);
	delete b;

	printf("Derived test:\n");
	Derived* d = new Derived();
	d->a = 2;
	d->b = 3;
	d->method1();
	d->method2();
	dumpBase(d);
	dumpDerived(d);
	delete d;

	Base* bb = new Derived();
	if (Derived* dd = dynamic_cast<Derived*>(bb))
	{
		bb->method1();
		dd->method1();
	}
	delete bb;

	return 0;
}
