/* File: scaffold.c	Version: 4.10	Date: 2007/11/21
 * CVSA, C Validation Suite
 * Type: Scaffold
 * Copyright 1984-2003, PERENNIAL, All Rights Reserved
 */
/*===========================================================================
	Included in this file are the support functions used in the
	test programs for the PERENNIAL ANSI/ISO/FIPS-C and Classic C
	Validation Suite:

		setup()    begin a test program
		blenter()  enter a block in a test program
		blexit()   exit a block in a test program
		anyfail()  end a test program
		errmesg()  exit test program with diagnostic
		debug()    useful during development
		ipost()    post an integer result in standard format
		fpost()    post a floating point result in standard format
		spost()    post a string result in standard format
		lpost()    post a long result in standard format
		opnfil()   initializes FileName using tmpnam, the opens a file.
		clsrmfil() close and remove the file associated with FileName.
		post()     write a message to the log file.

>NOTE:	When scaffold is built with NO_IO_SUPPORT defined, the driver
	configuration variable FREESTANDING needs to be set to Y.
 *===========================================================================*/
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>



#define  PASSED         0
#define  FAILED         1
#define  UNRESOLVED	2
#define  TRUE           1
#define  FALSE          0
#define  I_ERROR       -1

#define  WRITE         "w"
#define  WRITEPLUS     "w+"
#define  PMODE         0644
#define  ACVS_MAX_OPEN 5

/*-------------------------------------*
 *                                     *
 * block tracking states               *
 *                                     *
 *-------------------------------------*/

#define START  0
#define OUTBLK 1
#define INBLK  2
#define END    3
int state=START;

#define MAX_FILEPATH 300
//#define MAX_FILEPATH FILENAME_MAX


#define EXIT_SUCCESS   0
#define EXIT_FAILURE   1


extern char  prgnam[];


int locflg;      /* This flag is used in blocks to track failure. */

int blknum;      /* This identifys the current block */

int gloflg = PASSED;       /* Pass/Fail flag for the entire program */



char buffname[MAX_FILEPATH];
char tstnam[MAX_FILEPATH];
char cvsalogname[MAX_FILEPATH];

char *Extension = ".log";



void blenter( void );
void blexit( void );
void setup( void );
int  genlogfp( void );
void errmesg(char *);
int  anyfail( void );
void debug( void );
void ipost(int , int , char *);
void opost(int , int , char *);
void fpost(float , float , char *);
void spost(char *, char *, char *);
void lpost(long , long , char *);
int  clsrmfil( int );
void post(char *, ...);










/*----------------------------------------------------------------*\
 * FUNCTION:   blenter()                                          *
 * ARGUMENTS:  NONE                                               *
 * DESCRIPTION: A support function that is used to start each     *
 *              test case, or test block.                         *
 *           o Prints the current block number to the report file.*
 *           o Sets locflg to PASSED.                             *
 *           o Sets the error code to no error.                   *
 *           o Clears the condition number.                       *
 * RETURNS:  NONE                                                 *
\*----------------------------------------------------------------*/

void blenter( void )
{

   if (state != OUTBLK) {
      switch (state) {
      case INBLK: errmesg("Two successive calls to blenter().");
         break;
      case START: errmesg("The test did not call setup().");
         break;
      case END:   errmesg("blenter() is called after anyfail().");
         break;
      default:    errmesg("State machine in unknown state.");
      }
   }

   state=INBLK;

   post("Enter Block #%d \n",blknum);

   locflg = PASSED;


}

/*----------------------------------------------------------------*\
 * FUNCTION: blexit()                                             *
 * ARGUMENTS:  NONE                                               *
 * DESCRIPTION: A support function that is used to end, or exit   *
 *              each block.                                       *
 *           o Tests locflg and prints appropriate message to     *
 *             the test results report file.                      *
 * RETURNS:  NONE                                                 *
\*----------------------------------------------------------------*/

void blexit( void )
{

   if (state != INBLK) {
      switch (state) {
      case OUTBLK: errmesg("Two successive calls to blexit().");
         break;
      case START:  errmesg("The test did not call setup().");
         break;
      case END:    errmesg("blexit() is called after anyfail().");
         break;
      default:     errmesg("State machine in unknown state.");
      }
   }

   state=OUTBLK;


   post("Exit Block #%d ",blknum);

   blknum++;

   switch(locflg) {
      case PASSED:
         post("passed\n\n");
         break;
      case FAILED:
	 post("FAIL\n\n");
         gloflg = FAILED;
         break;
      default:
	 post("*** Internal error: exiting block %d\n", blknum);
         gloflg = I_ERROR;
         break;
   }

}
/*----------------------------------------------------------------*\
 * FUNCTION: void setup( void )                                   *
 * ARGUMENTS:  NONE                                               *
 * DESCRIPTION: A support function that initializes global        *
 *              variables, and opens the logfile for the          *
 *              test file that is to be used.                     *
 *           o Sets blknum to zero.                               *
 *           o Sets gloflg to PASSED.                             *
 *           o Builds a local string "name" that is concatenated  *
 *             to make the global "cvsalogname". ".log" is then       *
 *             attached to "cvsalogname".                             *
 *           o The "cvsalogname" is opened for write only, and the    *
 *             global string "prgnam" is written to the log       *
 *             file.                                              *
 *           o If any errors occur invoke exit(EXIT_FAILURE).     *
 * RETURNS:  NONE                                                 *
\*----------------------------------------------------------------*/

void setup( void )
{
   static int i;

   if (state != START)
      errmesg("setup() was called more than once");

   state=OUTBLK;

   blknum = 0;
   gloflg = PASSED;




   if (genlogfp() != 0)
	exit(EXIT_FAILURE);

   post("===%s\n",prgnam);
}
/*----------------------------------------------------------------*\
 * FUNCTION: int genlogfp( void )                                 *
 * ARGUMENTS:  NONE                                               *
 * DESCRIPTION: A support function that builds the cvsalogname, then  *
 *              opens the logfile for write.  If an error occurs  *
 *              return 1.                                         *
 * RETURNS:  0 - Success                                          *
 *           nonzero - Failure                                    *
\*----------------------------------------------------------------*/
int genlogfp()
{
   return(0);

}

/*----------------------------------------------------------------*\
 * FUNCTION: errmesg(message)                                     *
 * ARGUMENTS: message, a string to print to stderr, and write to  *
 *            the test report file.                               *
 * DESCRIPTION: A support function that is used to print a message*
 *            to stderr, and write the same message to the test   *
 *            results report file.                                *
 *            The support function "debug()" is called.           *
 * RETURNS:  NONE, exit(EXIT_FAILURE).                            *
\*----------------------------------------------------------------*/

void errmesg(char *message)
{

   exit(EXIT_FAILURE);
}

/*----------------------------------------------------------------*\
 * FUNCTION: anyfail()                                            *
 * ARGUMENTS: NONE                                                *
 * DESCRIPTION: A support function that checks the locflg and     *
 *              blknum, to determine if a setup error             *
 *              occurred.  If a setup error occurred the          *
 *              gloflg is set to NOPASS.  The gloflg              *
 *              is used to determine what is written to the       *
 *              test results file, and the stderr.  The test      *
 *              results file is closed.                           *
 * RETURNS:  o EXIT_SUCCESS;                                      *
 *           o EXIT_FAILURE;                                      *
\*----------------------------------------------------------------*/

int anyfail( void )
{

   static int s_a;

   if (state != OUTBLK) {
      switch (state) {
      case START: errmesg("setup() was never called.");
         break;
      case INBLK: errmesg("anyfail() was called before blexit().");
         break;
      case END:   errmesg("Two successive calls to anyfail().");
         break;
      default:    errmesg("State machine in unknown state.");
      }
   }

   state=END;

   switch(gloflg){
      case PASSED:
	 post("++++++++++++%s Passed\n",prgnam);

         s_a = EXIT_SUCCESS;
         break;

      case UNRESOLVED:
      case FAILED:
	 post("------------%s ******FAILED******\n",prgnam);

         s_a = EXIT_FAILURE;
         break;

      case I_ERROR:
	 post("***Internal Error");
         s_a = EXIT_FAILURE;
         break;
      default:
         post("Fatal Error in %s",tstnam);
         s_a = EXIT_FAILURE;
         break;
   }

   return( s_a );
}

/*----------------------------------------------------------------*\
 * FUNCTION:  debug()                                             *
 * ARGUMENTS:  NONE                                               *
 * DESCRIPTION: A support function that is used to write the      *
 *              following data to the test results file:          *
 *           o prgnam;                                            *
 *           o tstnam;                                            *
 *           o gloflg;                                            *
 *           o blknum;                                            *
 * RETURNS: NONE                                                  *
\*----------------------------------------------------------------*/

void debug()
{
    post("Debug function:\n");
    post("  name %s \n",prgnam);
    post("  test %s \n",tstnam);
    post("  gloflg %d \n",gloflg);
    post("  locflg %d \n",locflg);
    post("  blknum %d \n",blknum);
}

/*----------------------------------------------------------------*\
 * FUNCTION:  ipost()                                             *
 * ARGUMENTS: got - an integer that represents the value a test   *
 *                  case received.                                *
 *            expected - an integer that represents the value a   *
 *                       test case expected.                      *
 *            mesgstr  - a character string that will be written  *
 *                       to the .log file.  This string should    *
 *                       hold some meaningful information on the  *
 *                       test case.                               *
 * DESCRIPTION: A support function that is used to write the      *
 *              arguments explained above to the .log file.       *
 * RETURNS: NONE                                                  *
 *                                                                *
\*----------------------------------------------------------------*/

void ipost(int got, int expected, char *mesgstr)
{
    post("Got  %d Expected  %d %s \n",got ,expected, mesgstr);

}

/*----------------------------------------------------------------*\
 * FUNCTION:  opost()                                             *
 * ARGUMENTS: got - an integer that represents the value a test   *
 *                  case received. Written in Octal format.       *
 *            expected - an integer that represents the value a   *
 *                       test case expected. Written in Octal     *
 *                       format.                                  *
 *            mesgstr  - a character string that will be written  *
 *                       to the .log file.  This string should    *
 *                       hold some meaningful information on the  *
 *                       test case.                               *
 * DESCRIPTION: A support function that is used to write the      *
 *              arguments explained above to the .log file.       *
 * RETURNS: NONE                                                  *
 *                                                                *
\*----------------------------------------------------------------*/

void opost(int got, int expected, char *mesgstr)
{
    post("Got  %o Expected  %o %s \n",got ,expected, mesgstr);

}

/*----------------------------------------------------------------*\
 * FUNCTION:  fpost()                                             *
 * ARGUMENTS: got - a float that represents the value a test      *
 *                  case received.                                *
 *            expected - a float that represents the value a      *
 *                       test case expected.                      *
 *            mesgstr  - a character string that will be written  *
 *                       to the .log file.  This string should    *
 *                       hold some meaningful information on the  *
 *                       test case.                               *
 * DESCRIPTION: A support function that is used to write the      *
 *              arguments explained above to the .log file.       *
 * RETURNS: NONE                                                  *
 *                                                                *
\*----------------------------------------------------------------*/


void fpost(float got, float expected, char *mesgstr)
{
    //post("Got  %f Expected  %f %s \n",got ,expected, mesgstr);
}

/*----------------------------------------------------------------*\
 * FUNCTION:  spost()                                             *
 * ARGUMENTS: got - a string that represents the value a test     *
 *                  case received.                                *
 *            expected - a string that represents the value a     *
 *                       test case expected.                      *
 *            mesgstr  - a character string that will be written  *
 *                       to the .log file.  This string should    *
 *                       hold some meaningful information on the  *
 *                       test case.                               *
 * DESCRIPTION: A support function that is used to write the      *
 *              arguments explained above to the .log file.       *
 * RETURNS: NONE                                                  *
 *                                                                *
\*----------------------------------------------------------------*/

void spost(char *got, char *expected, char *mesgstr)
{
    post("Got  :%s: Expected  :%s: %s \n", got ,expected, mesgstr);
}

/*----------------------------------------------------------------*\
 * FUNCTION:  lpost()                                             *
 * ARGUMENTS: got - a long integer that represents the value a    *
 *                  test case received.                           *
 *            expected - a long integer that represents the       *
 *                       value a test case expected.              *
 *            mesgstr  - a character string that will be written  *
 *                       to the .log file.  This string should    *
 *                       hold some meaningful information on the  *
 *                       test case.                               *
 * DESCRIPTION: A support function that is used to write the      *
 *              arguments explained above to the .log file.       *
 * RETURNS: NONE                                                  *
 *                                                                *
\*----------------------------------------------------------------*/

void lpost(long got, long expected, char *mesgstr)
{
    post("Got %ld, Expected  %ld, %s\n", got, expected, mesgstr );
}
/*----------------------------------------------------------------*\
 * FUNCTION: opnfil()                                             *
 * ARGUMENTS:   n - An integer holding the index to the desired   *
 *                  file name and file pointer to close and       *
 *                  and remove.                                   *
 *                  n must be less than ACVS_MAX_OPEN.            *
 * DESCRIPTION: A support utility that is used to create a file   *
 *              with a call to the function tmpnam() to get a     *
 *              valid file name.  The file name and file pointer  *
 *              are stored in the global variables FileName[n]    *
 *              and Filefp[n].                                    *
 *              A total of ACVS_MAX_OPEN can be open at the same  *
 *              time.                                             *
 *              The support function "clsrmfil()" must be used to *
 *              close and remove the temporary file.              *
 * RETURNS: A valid FILE * that can be used to read or write the  *
 *          stream.                                               *
 *          NULL, if the file could not be opened, or an existing *
 *          file was open.                                        *
\*----------------------------------------------------------------*/
/*
FILE * opnfil( int n )
{
return null;

}
*/
/*----------------------------------------------------------------*\
 * FUNCTION: clsrmfil()                                           *
 * ARGUMENTS:   n - An integer holding the index to the desired   *
 *                  file name and file pointer to close and       *
 *                  and remove.                                   *
 *                  n must be less than ACVS_MAX_OPEN.            *
 * DESCRIPTION: A support function that is used to close and      *
 *              remove a file.                                    *
 * RETURNS:  0 - Success                                          *
 *           nonzero - Failure                                    *
\*----------------------------------------------------------------*/

int clsrmfil( int n )
{
	return(0);
}

/*----------------------------------------------------------------*\
 * FUNCTION: post()                                               *
 * ARGUMENTS:   s - A string that can hold format and text.       *
 *              ... - Data that should match the format commands  *
 *                    in s.                                       *
 *                                                                *
 * DESCRIPTION: A support function that is used to write text     *
 *              to the log file.                                  *
 * RETURNS:  None                                                 *
\*----------------------------------------------------------------*/

void post( char *s, ... )
{
	va_list ap;
	va_start(ap, s); /* Initialize the va_list */
	printf("POST: ");
	printf(s, ap);
	va_end(ap);
  	return;
}



