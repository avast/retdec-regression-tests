/* File: tsthd.h    Version: 1.12    Date: 2002/11/08
 * CVSA, ANSI/ISO/FIPS-C and Classic C Validation Suite
 * Type: Scaffold
 * Copyright 1991 - 2001, PERENNIAL, All Rights Reserved
 */
/*--------------------------------------------------------------------*\
 * This is the include file for all tests developed for the PERENNIAL
 * ANSI/ISO/FIPS C  Validation Suite.  It should be included in any 
 * test that uses the support functions in scaffold.o.
\*--------------------------------------------------------------------*/
#if !defined (FREESTANDING)
#include <stdio.h>
#endif

/*--------------------------------------------------------------------*\
 * These next three macros should be changed if the implementation    *
 * has a perror string longer than 80 characters, or does not have    *
 * 8 bits per byte, or the U_BITS is not correct.                     *
\*--------------------------------------------------------------------*/
/* Bits per byte, this is normally 8.  */
#define BITS_PER_BYTE 8
/* the number of characters in the perror string */
#define P_BUF_SIZE    80
/* the number of bits in a unsigned int */
#define U_BITS ((int)floor((log(UINT_MAX)/log(2)) +.5))
 
/* Bounds Checking Macro */
/* A = Answer            */
/* B = Upper Bound Limit */
/* C = Lower Bound Limit */
#define INBOUND(A,B,C) ((A) <= (B) && (A) >= (C))

/*
* General Use
*/
#define  PASSED     0
#define  SUCCESS    0
#define  FAILED     1
#define  UNRESOLVED 2
#define  I_ERROR   -1
#define  FATAL     -2

#define  ACVS_OPEN_MAX  5
#define  MIN_EXP_LENGTH 2

#define  DFAIL  0
#define  DPASS  1
#define  DTERS  2
#define  DVERB  3
#define  DDEBUG 4
#define  PMODE 0644

#define LEN_ERR         1
#define SGN_ERR         2
#define MAN_ERR         3
#define NO_E_ERR        4
#define NO_P_ERR        4
#define MAT_P_ERR       5
#define MAT_E_ERR       5
#define LEN_E_ERR       6
#define XPO_ERR         7
#define LEN_T_ERR       8
#define TXT_ERR         9
#define PRFX_ERR       10
#define PRE_SPACE_ERR  11
#define X_ERR          12
#define NOT_HEX_ERR    13
#define DEC_ERR        14
#define PREC_ERR       15
#define P_ERR          16
#define E_SGN_ERR      17
#define POST_SPACE_ERR 18
#define ZERO_PAD_ERR   19

extern int blknum;
extern int connum;
extern int gloflg ;
extern int locflg ;

extern char tstnam[];
#if !defined (FREESTANDING)
extern char FileName[ACVS_OPEN_MAX][L_tmpnam];/* To hold the names of temp files. */
extern FILE *Filefp[];    /* An arry of pointers to the temp streams. */
extern FILE *logfp;
#endif


/*----------------------------------------------------------------*\
 * The support functions used in the test source files.           *
\*----------------------------------------------------------------*/
#ifdef __STDC__

   void setup( void );
   void blexit( void );
   void blenter( void );
   void errmesg(char *);
   void debug( void );
   void post( char *, ...);
   void ipost(int , int , char *);
   void opost(int , int , char *);
   void fpost(float , float , char *);
   void spost(char *, char *, char *);
   void lpost(long , long , char *);
   
#if !defined (FREESTANDING)
#endif

   int  anyfail( void );
   int  clsrmfil( int );

#else

   void setup( );
   void blexit( );
   void blenter( );
   void errmesg( );
   void debug( );
   void post( );
   void ipost( );
   void opost( );
   void fpost( );
   void spost( );
   void lpost( );

#if !defined (FREESTANDING)
   FILE *opnfil( );
#endif

   int  anyfail( );
   int  clsrmfil( );

#endif
