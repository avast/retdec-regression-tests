
#include <stdio.h>

class Polygon
{
	public:
		void set_values (int w, int h) { width=w; height=h; }
		void printarea()               { printf("area %d\n", this->area()); }

		virtual int area() = 0; // pure virtual

	protected:
		int width;
		int height;
};

class Rectangle: public Polygon
{
	public:
		int area (void) { return (width * height); }
};

class Triangle: public Polygon
{
	public:
		int area (void) { return (width * height / 2); }
};

int main ()
{
	Rectangle rect;
	Triangle trgl;

	Polygon* ppoly1 = &rect;
	Polygon* ppoly2 = &trgl;

	ppoly1->set_values (4,5);
	ppoly2->set_values (4,5);

	ppoly1->printarea();
	ppoly2->printarea();

	return 0;
}
