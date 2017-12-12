/* File: P61500.c	Version: 1.5	Date: 2001/10/31
 * CVSA, ANSI/ISO C Validation Suite
 * Type: Positive test for Clause 6 (Language)
 * Copyright 1997, PERENNIAL, All Rights Reserved
 */
/*--------------------------------------------------------------------*\
	------------------- TESTPLAN SEGMENT -------------------
>REFS:	ISO/ANSI C draft, X3J11/97-037: 6.5.7 Initialization

>WHAT:	00-09. When a union type that has static storage duration and
	has an initial arithmetic type member that is not initialized 
	explicitly, then its first named member is initialized to zero.
	6.5.7;10b (4)

>HOW:	00. Declare a static union with a float member which is not
	initialized as its first member.  Verify that the member is 
	initialized to zero.

	01. Declare a static union with a double member which is not
	initialized as its first member.  Verify that the member is 
	initialized to zero.

	02. Declare a static union with a long double member which
	is not initialized as its first member.  Verify that the member 
	is intialized to zero.

	03. Declare a static union with a signed char member which
	is not initialized as its first member.  Verify that the member 
	is initialized to zero.

	04. Declare a static union with an int member which is not
	intialized as its first member.  Verify that the member is 
	initialized to zero.

	05. Declare a static union with a union as its first member, 
	that has its own character type as its first member.  Verify 
	that the member of the union member is initialized to zero.

	06. Declare a static union with a union as its first member 
	that has its own short int type as its first member.  Verify 
	that the member of the union member is initialized to zero.

	07. Declare a static union with a union as its first member 
	that has its own long int type as its first member.  Verify 
	that the member of the union member is initialized to zero.

	08. Declare a static union with a union as its first member 
	that has its own unsigned short int as its first member.  
	Verify that the member of the union member is initialized to 
	zero.

	09. Declare a static union with a union as its first member that 
	has its own unsigned long int as its first member.  Verify 
	that the member of the union member is initialized to zero.

>NOTE:	This assertion comes from Defect Report #016 which caused a
	modification to ISO 9899:1990 in Technichal Corrigendum 1.
\*--------------------------------------------------------------------*/
#include <math.h>
#include "include/tsthd.h"
#include "include/scaffold.c"


static union {
	float f;
	char p;
}z;

static union {
	double du;
	int counter;
}y;

static union {
	long double ld;
	char *cstar;
}x;

static union {
	signed char sc;
	int *istar;
}w;

static union {
	int i;
	double danger;
}v;

static union {
	union {
		char ch;
		long day;
	}a;
	double jeopardy;
}u;

static union {
	union {
		short int si;
		long year;
	}b;
	char acter;
}t;

static union {
	union {
		long int li;
		int eger;
	}c;
	long ing;
}s;

static union {
	union {
		unsigned short int usi;
		short ening;
	}d;
	short changed;
}r;

static union {
	union {
		unsigned long int uli;
		char acterized;
	}e;
	char ity;
}q;

extern int locflg;

/*--------------------------------------------------------------------*/
char prgnam[] = "P61500.c";

int main(int argc, char *argv[])
{
	setup();

	post("ISO/ANSI C draft, X3J11/97-037: 6.5.7 Initialization\n");
/*--------------------------------------------------------------------*/
	blenter();	/* block 00 */

	if (z.f != 0){
		locflg = FAILED;
		post("float member not initialized to zero.\n");
	}

	blexit();
/*--------------------------------------------------------------------*/
	blenter();	/* block 01 */

	if (y.du != 0){
		locflg = FAILED;
		post("double member not initialized to zero.\n");
	}

	blexit();
/*--------------------------------------------------------------------*/
	blenter();	/* block 02 */

	if (x.ld != 0){
		locflg = FAILED;
		post("long double member not initialized to zero.\n");
	}

	blexit();
/*--------------------------------------------------------------------*/
	blenter();	/* block 03 */

	if (w.sc != 0){
		locflg = FAILED;
		post("signed char member not initialized to zero.\n");
	}

	blexit();
/*--------------------------------------------------------------------*/
	blenter();	/* block 04 */

	if (v.i != 0){
		locflg = FAILED;
		post("int member not initialized to zero.\n");
	}

	blexit();
/*--------------------------------------------------------------------*/
	blenter();	/* block 05 */

	if (u.a.ch != 0){
		locflg = FAILED;
		post("Char in union within union not initialized"
		" to zero.\n");
	}

	blexit();
/*--------------------------------------------------------------------*/
	blenter();	/* block 06 */

	if (t.b.si != 0){
		locflg = FAILED;
		post("short int in union within union not "
		"initialized to zero.\n");
	}

	blexit();
/*--------------------------------------------------------------------*/
	blenter();	/* block 07 */

	if (s.c.li != 0){
		locflg = FAILED;
		post("long int in union within union not "
		"initialized to zero.\n");
	}

	blexit();
/*--------------------------------------------------------------------*/
	blenter();	/* block 08 */

	if (r.d.usi != 0){
		locflg = FAILED;
		post("Unsigned short int in union within union "
		"not initialized to zero.\n");
	}

	blexit();
/*--------------------------------------------------------------------*/
	blenter();	/* block 09 */

	if (q.e.uli != 0){
		locflg = FAILED;
		post("Unsigned long int in union within union "
		"not initialized to zero.\n");
	}

	blexit();
/*--------------------------------------------------------------------*/
	return(anyfail());
}
