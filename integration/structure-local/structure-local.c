/**
 * structure-local.c
 * Integration test for detection of local structures and accesses into them.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * Basic structure.
 */
struct basic_t
{
	char c;
	int i;
	float f;
};

int fnc_basic_print(struct basic_t *basic)
{
	printf("%f %d %d\n", basic->f, basic->i, basic->c);
}

void fnc_basic()
{
	struct basic_t *basic = malloc( sizeof(struct basic_t) );

	char INc;
	scanf("%c", &INc);
	basic->c = INc;

	int INi;
	scanf("%d", &INi);
	basic->i = INi;

	// TODO: only mips can handle this at the moment, check arm,x86.
	// TODO: arm and x86 have it totally wrong, mips is ok, but float64_t is used and it screw up the number.
// 	float INf;
// 	scanf("%f", &INf);
// 	basic->f = INf;

	basic->f = 3.14;

	// TODO: this is not handled correctly right now.
// 	scanf("%c", &basic->c);
// 	scanf("%d", &basic->i);
// 	scanf("%f", &basic->f);

	// TODO: mips: there is some strange modulo if %c used, maybe some idiom? it causes segfault.
// 	printf("%c %d %f\n", basic->c, basic->i, basic->f);
	printf("%d %d %f\n", basic->c, basic->i, basic->f);
	fnc_basic_print(basic);
}

/*
 * Basic local structure -- it is not possible to reconstruct this without debug info.
 * TODO: not working.
 */
int fnc_basic_local_print(struct basic_t basic)
{
	printf("%c %d %f\n", basic.c, basic.i, basic.f);
}

int fnc_basic_local()
{
   struct basic_t basic;

   basic.c = 'a';
   basic.i = 1234;
   basic.f = 1.0;

   fnc_basic_local_print(basic);

   return 0;
}

/**
 *  Complex structure.
 */
#define COMPLEX_SIZE 5

struct complex_in_t
{
   int e1;
   int e2;
   int e3;
};

struct complex_t
{
   int b;
   char c;
   struct complex_in_t d[COMPLEX_SIZE];
   float f;
   float e[COMPLEX_SIZE];
};

void fnc_complex_print(struct complex_t *complex)
{
   printf("%d %d %f\n", complex->b, complex->c, complex->f);
   int i;
   for (i=0; i<COMPLEX_SIZE; i++)
   {
      printf("%d %d %d %f\n", complex->d[i].e1, complex->d[i].e2, complex->d[i].e3, complex->e[i]);
   }
}

int fnc_complex(void)
{
	struct complex_t *complex = (struct complex_t *) malloc( sizeof(struct complex_t) );

	complex->b = 123;
	complex->c = 'a';
	complex->f = 3.14;

	int i;
	for (i=0; i<COMPLEX_SIZE; i++)
	{
		complex->d[i].e1 = i+1;
		complex->d[i].e2 = i+2;
		complex->d[i].e3 = i+3;

		complex->e[i] = i * complex->f;
	}

	int j;
	for (j=0; j<COMPLEX_SIZE; j++)
	{
		complex->d[j].e1 += j;
		complex->d[j].e2 += j;
		complex->d[j].e3 += j;

		complex->e[j] += j;
	}

	fnc_complex_print(complex);

	return 0;
}

/**
 *  sasa - structure/array/structure/array.
 */
#define SASAS_SIZE 10

struct sasa_in_t
{
   int aa1[SASAS_SIZE];
   int ee1;
   int aa2[SASAS_SIZE];
};

struct sasa_t
{
   int e1;
   struct sasa_in_t a[SASAS_SIZE];
   int e2;
};

// TODO: this may be to complicated, but we should do it at least when there are debug infos.
void fnc_sasa_malloc(struct sasa_t **sasa)
{
	*sasa = (struct sasa_t *) malloc( sizeof(struct sasa_t) );
}

void fnc_sasa_fill(struct sasa_t *sasa)
{
	sasa->e1 = 123;
	sasa->e2 = 456;

	int i;
	int j;
	for (i=0; i<SASAS_SIZE; i++)
	{
		sasa->a[i].ee1 = i;

		for (j=0; j<SASAS_SIZE; j++)
		{
			sasa->a[i].aa1[j] = i+j+1;
			sasa->a[i].aa2[j] = i+j+2;
		}
	}
}

void fnc_sasa_print(struct sasa_t *sasa)
{
	int i;
	int j;

	printf("%d %d\n", sasa->e1, sasa->e2);

	for (i=0; i<SASAS_SIZE; i++)
	{
		printf("\n");
		printf("%d\n", sasa->a[i].ee1);

		int sum1 = 0;
		int sum2 = 0;
		for (j=0; j<SASAS_SIZE; j++)
		{
			sum1 += sasa->a[i].aa1[j];
			sum2 += sasa->a[i].aa2[j];
		}
		printf("%d\n", sum1);
		printf("%d\n", sum2);
	}
}

int fnc_sasa()
{
	struct sasa_t *sasa = (struct sasa_t *) malloc( sizeof(struct sasa_t) );

// 	struct sasa_t *sasa = NULL;
// 	fnc_sasa_malloc(&sasa);

	fnc_sasa_fill(sasa);
	fnc_sasa_print(sasa);

	return 0;
}

/*
 * Main function - just calls specific testing functions.
 */
int main()
{
	fnc_basic();
// 	fnc_basic_local();

	fnc_complex();
	fnc_sasa();

	return 0;
}
