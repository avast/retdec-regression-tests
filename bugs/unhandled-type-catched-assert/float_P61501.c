/* File: P61501.c	Version: 1.5	Date: 2001/10/31
 * CVSA, ANSI/ISO C Validation Suite
 * Type: Positive test for Clause 6 (Language)
 * Copyright 1997, PERENNIAL, All Rights Reserved
 */
/*--------------------------------------------------------------------*\
	------------------- TESTPLAN SEGMENT -------------------
>REFS:	ISO/ANSI C draft, X3J11/97-037: 6.5.7 Initialization

>WHAT:	00-09. When an aggregate type that has static storage duration
	is not initialized explicitly, then its arithmetic type members
	are initialized to zero. 6.5.7;10b (2)

>HOW:	00. Declare a static structure with a float member which is not
	initialized.  Verify that the member is initialized to zero.

	01. Declare a static structure with a double member which is not
	initialized.  Verify that the member is initialized to zero.

	02. Declare a static structure with a long double member which
	is not initialized.  Verify that the member is intialized to
	zero.

	03. Declare a static structure with a signed char member which
	is not initialized.  Verify that the member is initialized to
	zero.

	04. Declare a static structure with an int member which is not
	intialized.  Verify that the member is initialized to zero.

	05. Declare a static structure with a structure member that
	has its own character type member.  Verify that the member of
	the structure member is initialized to zero.

	06. Declare a static structure with a structure member that has
	its own short int type member.  Verify that the member of the
	structure member is initialized to zero.

	07. Declare a static structure with a structure member that has
	its own long int type member.  Verify that the member of the
	structure member is initialized to zero.

	08. Declare a static structure with a structure member that has
	its own unsigned short int member.  Verify that the member of
	the structure member is initialized to zero.

	09. Declare a static structure with a structure member that has
	its own unsigned long int member.  Verify that the member of the
	structure member is initialized to zero.

>NOTE:	This assertion comes from Defect Report #016 which caused a
	modification to ISO 9899:1990 in Technichal Corrigendum 1.
\*--------------------------------------------------------------------*/
#include <math.h>
#include "include/tsthd.h"
#include "include/scaffold.c"


static struct {
	float f;
	double d;
	long double ld;
	signed char sc;
	int i;
	struct {
		char c;
		short int si;
		long int li;
		unsigned short int usi;
		unsigned long int uli;
	}b;
}a;

extern int locflg;

/*--------------------------------------------------------------------*/
char prgnam[] = "P61501.c";

int main(int argc, char *argv[])
{
	setup();

	post("ISO/ANSI C draft, X3J11/97-037: 6.5.7 Initialization\n");
/*--------------------------------------------------------------------*/
	blenter();	/* block 00 */

	if (a.f != 0){
		locflg = FAILED;
		post("float member not initialized to zero.\n");
	}

	blexit();
/*--------------------------------------------------------------------*/
	blenter();	/* block 01 */

	if (a.d != 0){
		locflg = FAILED;
		post("double member not initialized to zero.\n");
	}

	blexit();
/*--------------------------------------------------------------------*/
	blenter();	/* block 02 */

	if (a.ld != 0){
		locflg = FAILED;
		post("long double member not initialized to zero.\n");
	}

	blexit();
/*--------------------------------------------------------------------*/
	blenter();	/* block 03 */

	if (a.sc != 0){
		locflg = FAILED;
		post("signed char member not initialized to zero.\n");
	}

	blexit();
/*--------------------------------------------------------------------*/
	blenter();	/* block 04 */

	if (a.i != 0){
		locflg = FAILED;
		post("int member not initialized to zero.\n");
	}

	blexit();
/*--------------------------------------------------------------------*/
	blenter();	/* block 05 */

	if (a.b.c != 0){
		locflg = FAILED;
		post("Char in structure within structure not initialized"
		" to zero.\n");
	}

	blexit();
/*--------------------------------------------------------------------*/
	blenter();	/* block 06 */

	if (a.b.si != 0){
		locflg = FAILED;
		post("short int in structure within structure not "
		"initialized to zero.\n");
	}

	blexit();
/*--------------------------------------------------------------------*/
	blenter();	/* block 07 */

	if (a.b.li != 0){
		locflg = FAILED;
		post("long int in structure within structure not "
		"initialized to zero.\n");
	}

	blexit();
/*--------------------------------------------------------------------*/
	blenter();	/* block 08 */

	if (a.b.usi != 0){
		locflg = FAILED;
		post("Unsigned short int in structure within structure "
		"not initialized to zero.\n");
	}

	blexit();
/*--------------------------------------------------------------------*/
	blenter();	/* block 09 */

	if (a.b.uli != 0){
		locflg = FAILED;
		post("Unsigned long int in structure within structure "
		"not initialized to zero.\n");
	}

	blexit();
/*--------------------------------------------------------------------*/
	return(anyfail());
}
