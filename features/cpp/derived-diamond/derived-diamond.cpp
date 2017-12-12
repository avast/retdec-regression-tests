
#include <stdio.h>

class A
{
	public:
		virtual void a()    { printf("A::a()\n"); }
		virtual void aa()   { printf("A::aa()\n"); }
		virtual void aaa()  { printf("A::aaa()\n"); }
		virtual void aaaa() { printf("A::aaaa()\n"); }
};

class B : virtual public A
{
	public:
		virtual void a()  { printf("B::a()\n"); };

		void b()          { printf("B::b()\n"); }
		virtual void bb() { printf("B::bb()\n"); }
};

class C : virtual public A
{
	public:
		virtual void aa() { printf("C::aa()\n"); };

		void c()          { printf("C::c()\n"); };
		virtual void cc() { printf("C::cc()\n"); };
};

class D: virtual public B, virtual public C
{
	public:
		virtual void aaa() { printf("D::aaa()\n"); };

		void d()           { printf("D::d()\n"); };
		virtual void dd()  { printf("D::dd()\n"); };
};


int main(int argc, char *argv[])
{
	A* a = new D();
	a->a();
	a->aa();
	a->aaa();
	a->aaaa();

	if (B* b = dynamic_cast<B*>(a))
	{
		b->a();
		b->aa();
		b->aaa();
		b->aaaa();
		b->b();
		b->bb();
	}

	if (C* c = dynamic_cast<C*>(a))
	{
		c->a();
		c->aa();
		c->aaa();
		c->aaaa();
		c->c();
		c->cc();
	}

	if (D* d = dynamic_cast<D*>(a))
	{
		d->a();
		d->aa();
		d->aaa();
		d->aaaa();
		d->b();
		d->bb();
		d->c();
		d->cc();
		d->d();
		d->dd();
	}

	return 0;
}