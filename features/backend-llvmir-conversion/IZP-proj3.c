/*
 * Soubor:  proj3.c
 * Datum:   6.12.2005
 * Autor:   Petr Zemek, xzemek02@stud.fit.vutbr.cz
 * Projekt: IZP c. 3 - Maticove operace
 * Popis:   Program provadi operace s maticemi obecnych rozmeru pro cela cisla.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define NDEBUG 1
#include <assert.h>

//int strcmp(const char *s1, const char *s2);

/** Minimalni a maximalni pocet parametru (vyjma -h)*/
#define MIN_PARAM 3
#define MAX_PARAM 4

/** Struktura - Matice */
typedef struct tmatrix
{
  unsigned int rows, cols; /** Pocet radku a sloupcu */
  int **matrix;            /** Dvourozmerne pole pro ulozeni prvku matice */
} TMatrix;

/** Struktura obsahujici hodnoty parametru prikazove radky. */
typedef struct params
{
  int funkce;     /** Funkce, kterou budeme s maticemi provadet */
  int pocet;      /** Pocet souboru pro danou operaci */
  char *zdroj1;   /** 1. zdrojovy soubor */
  char *zdroj2;   /** 2. zdrojovy soubor */
} TParams;

/** Monotonnost matice - posloupnosti */
enum TypPosloupnosti
{
  MONO_NIC,
  MONO_NKLES,
  MONO_NROST,
  MONO_NENI
};

/** Definovane operace s maticemi */
enum Funkce
{
  ADDMATRIX,
  MULTMATRIX,
  MONOMATRIX,
  SPIRALMATRIX
};

/** Vycet chybovych/stavovych kodu */
typedef enum Errors
{
  EOK,
  YMONO, NMONO,
  ENEMV, EMATF, EROZM,
  EALLOC,
  EFOPEN, EFCLOSE,
  EPARAMS, EFCE, EPOCET
} ErrCode;

/** Chybove hlasky */
const char *ERRMSG[] =
{
  // bez chyby
  "",
  // matice je monotonni
  "1\n",
  // matice neni monotonni
  "#\n",
  // operace nema definovany vysledek
  "#\n",
  // spatny format matice
  "Data v souboru jsou ve spatnem formatu!\n",
  // prilis velke rozmery matice
  "Rozmery matice jsou mimo rozsah!\n",
  // chyba alokace pameti
  "Nedostatek pameti!\n",
  // chyby pri praci se soubory
  "Soubor se nepodarilo otevrit!\n",
  "Soubor se nepodarilo uzavrit!\n",
  // chyby parametru prikaz. radky
  "Program byl spusten s chybnymi parametry!\n",
  "Zadana funkce neexistuje!\n",
  "Nezadan spravny pocet souboru!\n",
};

/**
 * Vypise chybovou hlasku na standardni chybovy vystup
 * Pokud je kod 1 nebo #,tak je vysledek vypsan na standardni vystup
 * @param code Chybovy/stavovy kod
 */
void printMsg(ErrCode code)
{
  if (code == YMONO || code == NMONO || code == ENEMV)
    printf(ERRMSG[code]);
  else
    fprintf(stderr, ERRMSG[code]);
}

/** Vypisuje na stand. chyb. vystup oznameni o parametru -h */
void printRunHelp(void)
{
  fprintf(stderr, "Spustte program s parametrem -h pro napovedu.\n");
}

/**
 * Vytiskne na standardni vystup text s napovedou.
 */
void printHelp(void)
{
  printf("******************************************************************\n"
         "*    Program Maticove operace.                                   *\n"
         "*    Autor: Petr Zemek                                           *\n"
         "*    Program provadi operace s maticemi obecnych rozmeru         *\n"
         "*    pro cela cisla.                                             *\n"
         "*    Matice se nacitaji ze souboru, jehoz nazev je zadan         *\n"
         "*    jako parametr pri spusteni programu .                       *\n"
         "*    Pouziti: proj3 -h                                           *\n"
         "*             proj3 -operace soubor1.txt soubor2.txt             *\n"
         "*    Popis parametru:                                            *\n"
         "*      -h            Vypise tuto obrazovku s napovedou.          *\n"
         "*      -operace      Jakou operaci ma program provest.           *\n"
         "*      soubor1.txt   1. zdrojovy soubor                          *\n"
         "*      soubor2.txt   2. zdrojovy soubor (pokud je potreba)       *\n"
         "*    Moznosti parametru -operace jsou:                           *\n"
         "*      -add          Soucet dvou matic (2 soubory)               *\n"
         "*      -mult         Soucin dvou matic (2 soubory)               *\n"
         "*      -mono         Zjistuje monotonnost matice (1 soubor)      *\n"
         "*      -spiral       Vytiskne prvky po spirale (1 soubor)        *\n"
         "*                                                                *\n"
         "******************************************************************\n"
         );
}  // printHelp()

/**
 * Otestuje, zda posledni alokacni operace probehla v poradku. Pokud ne,
 * vypise chybovou hlasku a ukonci program.
 * @param ptr Ukazatel na posledne alokovanou pamet.
 */

void testAlloc(void *ptr)
{
  if (ptr == NULL)
  { // nastala chyba
    printMsg(EALLOC);
    exit(EXIT_FAILURE);
  }
} // testAlloc()

/**
 * Zpracuje argumenty prikazoveho radku a vrati je ve strukture TParams.
 * Pokud je format argumentu chybny, ukonci program a vypise chybovou hlasku.
 * @param argc Pocet argumentu.
 * @param argv Pole textovych retezcu s argumenty.
 * @return Vraci analyzovane argumenty prikazoveho radku.
 */

TParams getParams(int argc, char *argv[])
{
  TParams result =
  { // inicializace struktury
    .funkce = 0,
    .pocet = 0,
    .zdroj1 = NULL,
    .zdroj2 = NULL
  };

  // byl zadan pouze 1 parametr a byl to parametr -h
  if (argc == 2 && strcmp("-h", argv[1]) == 0)
  { // tisk napovedy
    printHelp();
    exit(EXIT_SUCCESS);
  }

  // test, zda nebylo zadano malo/moc parametru
  else if ((argc < MIN_PARAM) || (argc > MAX_PARAM))
  { // zadany spatny pocet parametru
    printMsg(EPARAMS);
    printRunHelp();
    exit(EXIT_FAILURE);
  }

  // test, zda nebyl zadany neexistujici parametr -funkce
  else if (!strcmp("-add", argv[1]))
  { // funkce Soucet matic
    result.funkce = ADDMATRIX;
    result.pocet = 2;
  }
  else if (!strcmp("-mult", argv[1]))
  { // funkce Nasobeni matic
    result.funkce = MULTMATRIX;
    result.pocet = 2;
  }
  else if (!strcmp("-mono", argv[1]))
  { // funkce Nasobeni matic
    result.funkce = MONOMATRIX;
    result.pocet = 1;
  }
  else if (!strcmp("-spiral", argv[1]))
  { // funkce Nasobeni matic
    result.funkce = SPIRALMATRIX;
    result.pocet = 1;
  }
  else
  { // zadana funkce neexistuje
    printMsg(EFCE);
    printRunHelp();
    exit(EXIT_FAILURE);
  }

  // test, zda byly zadany 1-2 nazvy zdrojovych souboru
  // a zda zadana funkce potrebuje 1 nebo 2 soubory
  if ((result.pocet == 1) && (argc == MIN_PARAM))
  { // funkce potrebuje 1 soubor
    result.zdroj1 = argv[2];
  }
  else if ((result.pocet == 2) && (argc == MAX_PARAM))
  { // funkce potrebuje 2 soubory
    result.zdroj1 = argv[2];
    result.zdroj2 = argv[3];
  }
  else
  { // spatny pocet souboru
    printMsg(EPOCET);
    printRunHelp();
    exit(EXIT_FAILURE);
  }

  return result;
}  // getParams()


/**
 * Nacte matici ze souboru predaneho odkazem.
 * Pokud nastane chyba, program vraci chybovy kod.
 * @param soubor Ukazatel na soubor
 * @param matice Ukazatel na matici
 * @return Vraci chybovy/stavovy kod
 */
int loadMatrix(FILE *soubor, TMatrix *matice)
{
  // test, zda byly parametry predany odkazem v poradku
  assert(soubor != NULL);
  assert(matice != NULL);

  // zjisteni poctu radku a sloupcu matice
  int stav = fscanf(soubor, "%u%u", &matice->rows, &matice->cols);
  // pocet radku/sloupcu nemuze byt nizsi nez 1
  if ((stav != 2) || ((int)matice->rows < 1) || ((int)matice->cols < 1))
  { // doslo k chybe
    return EMATF;
  }

  // preskoci dalsi pripadne znaky z 1. radku
  while (fgetc(soubor) != '\n')
  {
    fscanf(soubor, "%*s");
  }

  // alokace pameti pro matici - nejprve alokace pole ukazatelù na int
  matice->matrix = malloc(matice->rows*sizeof(int *));
  testAlloc(matice->matrix);
  // potom jednotlivé øádky
  unsigned int i;
  for (i = 0; i < matice->rows; i++)
  {
    matice->matrix[i] = malloc(matice->cols*sizeof(int));
    testAlloc(matice->matrix[i]);
  }

  // nacteni hodnot do prvku matice
  unsigned  int r, s;
  for (r = 0; r < matice->rows; r++)
  {
    for (s = 0; s < matice->cols; s++)
    {
      stav = fscanf(soubor, "%d", &matice->matrix[r][s]);
      if (stav != 1)
      { // doslo k chybe
        return EMATF;
      }
    }
  }

  return EOK;
} // loadMatrix()

/**
 * Secte dve matice predane odkazem a vysledek ulozi do prvni z nich
 * @param dest 1. matice (ukazatel)
 * @param add  2. matice (konst. ukazatel)
 * @return Vraci chybovy/stavovy kod
 */
int addMatrix(TMatrix *dest, const TMatrix *add);
int addMatrix(TMatrix *dest, const TMatrix *add)
{
  // test, zda byly parametry predany odkazem v poradku
  assert(dest != NULL);
  assert(add != NULL);

  // podminka
  if (dest->rows != add->rows || dest->cols != add->cols)
  { // doslo k chybe
    return ENEMV;
  }

  // vypocet a ulozeni vysledku do prvni matice
  unsigned  int r, s;
  for (r = 0; r < add->rows; r++)
  {
    for (s = 0; s < add->cols; s++)
    {
      dest->matrix[r][s] = dest->matrix[r][s] + add->matrix[r][s];
    }
  }

  return EOK;
} // addMatrix()

/**
 * Vynasobi dve matice predane odkazem a vysledek ulozi do prvni z nich
 * @param dest 1. matice (ukazatel)
 * @param mult 2. matice (konst. ukazatel)
 * @return Vraci chybovy/stavovy kod
 */
int multMatrix(const TMatrix *mult1, const TMatrix *mult2, TMatrix *dest);
int multMatrix(const TMatrix *mult1, const TMatrix *mult2, TMatrix *dest)
{
  // test, zda byly parametry predany odkazem v poradku
  assert(dest != NULL);
  assert(mult1 != NULL);
  assert(mult2 != NULL);

  // podminka
  if (mult1->cols != mult2->rows)
  { // doslo k chybe
    return ENEMV;
  }

  // alokuji treti matici pro uchovani vysledku
  dest->rows = mult1->rows;
  dest->cols = mult2->cols;
  dest->matrix = malloc(dest->rows*sizeof(int *));
  testAlloc(dest->matrix); // test alokace pameti
  unsigned  int i;
  for (i = 0; i < dest->rows; i++)
  {
    dest->matrix[i] = malloc(dest->cols*sizeof(int));
    testAlloc(dest->matrix[i]);
  }

  // vypocet
  unsigned  int r, s, t;
  for (r = 0; r < dest->rows; r++)
  {
    for (s = 0; s < dest->cols; s++)
    {
      dest->matrix[r][s] = 0; // vynulovani prvku pole
      for (t = 0; t < mult1->cols; t++)
      {  // vypocet skalarniho soucinu
         dest->matrix[r][s] += mult1->matrix[r][t] * mult2->matrix[t][s];
      }
    }
  }

  return EOK;
} // multMatrix()

/**
 * Test dvou prvku po sobe jdoucich, zda je splnena podminka,
 * ze posloupnost je (ne)klesajici/(ne)rostouci.
 * @return Vraci typ posloupnosti (MONO_NENI - matice neni monotonni)
 */

int testMono(int posloupnost, int *novy, int *stary)
{
  // test, zda byly parametry predany odkazem v poradku
  assert(novy != NULL);
  assert(stary != NULL);

  // test
  if (*stary == *novy)
    ; // hodnota je stejna - neprovede se nic
  else if (posloupnost == MONO_NIC)
  { // nebyla urcena posloupnost
    if (*novy > *stary)
      posloupnost = MONO_NKLES;
    else
      posloupnost = MONO_NROST;
  }
  else if ((*stary > *novy) && (posloupnost == MONO_NROST))
  { // (ne)rostouci posloupnost
    *novy = *stary;
  }
  else if ((*stary < *novy) && (posloupnost == MONO_NKLES))
  { // (ne)klesajici posloupnost
    *novy = *stary;
  }
  else
  { // matice neni monotonni
    posloupnost = MONO_NENI;
  }

  return posloupnost;
}

/**
 * Zjisti, zda je nactena matice monotonni
 * @param source Matice (ukazatel)
 * @return Vraci chybovy/stavovy kod
 */
int monoMatrix(const TMatrix *source);
int monoMatrix(const TMatrix *source)
{
  // test, zda byly parametry predany odkazem v poradku
  assert(source != NULL);

  // promenne
  int posloupnost = MONO_NIC; // posloupnost neni urcena
  int hodnota, novaH;         // hondnota prvku matice / stara hodnota

  // monotonost radku matice
  hodnota = source->matrix[0][0]; // priradim prvni prvek v matici

  // urceni monotonosti radku
  unsigned  int r, s;
  for (r = 0; r < source->rows; r++)
  {
    for (s = 0; s < source->cols; s++)
    {
      novaH = source->matrix[r][s];
      posloupnost = testMono(posloupnost, &novaH, &hodnota);
      if (posloupnost == MONO_NENI)
      {
        return NMONO;
      }
    }
    if (r < source->rows-1)
    { // nejsme v poslednim radku matice
      hodnota = source->matrix[r+1][0];
    }
  }

  // monotonost sloupcu matice
  posloupnost = MONO_NIC; // posloupnost neni urcena

  // priradim prvni prvek v matici
  hodnota = source->matrix[0][0];

  // urceni monotonosti sloupcu
  for (s = 0; s < source->cols; s++)
  {
    for (r = 0; r < source->rows; r++)
    {
      novaH = source->matrix[r][s];
      posloupnost = testMono(posloupnost, &novaH, &hodnota);
      if (posloupnost == MONO_NENI)
      {
        return NMONO;
      }
    }
      if (s < source->cols-1)
      { // nejsme v poslednim sloupci matice
        hodnota = source->matrix[0][s+1];
      }
   }

  // matice je monotonni
  return YMONO;
} // monoMatrix()

/**
 * Vypise prvky matice v tzv. poradi ve spirale
 * @param source Matice (ukazatel)
 * @return Vraci chybovy/stavovy kod
 */
int spiralMatrix(const TMatrix *source);
int spiralMatrix(const TMatrix *source)
{
  // test, zda byly parametry predany odkazem v poradku
  assert(source != NULL);

  // promenne
  int pocetCyklu;                    // celkovy pocet cyklu
  int pocetKroku = source->cols;     // pocet kroku
  int pocetKrokuR = pocetKroku;      // pocet kroku v radku
  int pocetKrokuS = source->rows-1;  // pocet kroku ve sloupci
  int hodnota, pom;                  // hodnota prvku v matici/pomocna promenna
  int odr = source->rows-1, odc = 0; // pozice v matici (start: levy dolni roh)
  int dr = 0, dc = 1;                // smery posunu

  // vypocet poctu cyklu v zavisloti na druhu matice
  if (source->rows <= source->cols)
  { // pocet radku je stejny nebo mensi nez pocet sloupcu
    pocetCyklu = 2*source->rows-1;
  }
  else
  {  // pocet radku je vetsi nez pocet sloupcu
    pocetCyklu = 2*source->cols;
  }

  // vypocet
  int i, j;
  for (i = 1; i < pocetCyklu+1; i++)
  {
    for (j = 0; j < pocetKroku; j++)
    {
      hodnota = source->matrix[odr+dr][odc+dc-1];
      printf("%d ", hodnota); // vypise hodnotu na danem miste v matici
      odr += dr;
      odc += dc;
    }
    // vypocet poctu kroku v zavisloti na rozmerech matice
    if (i%2 == 0)
    { // i je sude cislo
      pocetKrokuR--;
      pocetKroku = pocetKrokuR;
    }
    else
    { // i je liche cislo
      pocetKroku = pocetKrokuS;
      pocetKrokuS--;
    }
    // vymena smerovych hodnot
    pom = dr;
    dr = -dc;
    dc = pom;
  }

  // odradkuje na konci vypisu cisel
  printf("\n");

  return EOK;
} // spiralMatrix()

/**
 * Vypise matici na standartni vystup
 * @param matice Konst. ukazatel na matici
 */
void printMatrix(const TMatrix *matice);
void printMatrix(const TMatrix *matice)
{
  // test, zda byly parametry predany odkazem v poradku
  assert(matice != NULL);

  printf("%u %u\n", matice->rows, matice->cols);
  unsigned  int r, s;
  for (r = 0; r < matice->rows; r++)
  {
    for (s = 0; s < matice->cols; s++)
    {
      printf("%d ", matice->matrix[r][s]);
    }
    printf("\n");
  }
} // printMatrix()

/**
 * Uvolni pamet, ktera byla alokovana
 * @param matice Ukazatel na matici
 */

void freeMatrix(TMatrix *matice)
{
  // test, zda byly parametry predany odkazem v poradku
  assert(matice != NULL);

  // uvolni pamet
  unsigned  int i;
  for (i = 0; i < matice->rows; i++)
  {
    free(matice->matrix[i]);
  }
  free(matice->matrix);
}  // freeMatrix()

/**
 * Hlavni program
 */
int main(int argc, char *argv[])
{
  // vyhodnotim parametry
  TParams params = getParams(argc, argv);

  // promenne
  int stav;                // chybove - stavove kody
  FILE *soubor1, *soubor2; // ukazatele na soubory
  TMatrix m1, m2, m3;      // matice

  // otevreni 1. souboru a nacteni ukazatele na soubor
  soubor1 = fopen(params.zdroj1, "r");
  if (soubor1 == NULL)
  { // soubor se nepodarilo otevrit
    printMsg(EFOPEN);
    return EXIT_FAILURE;
  }
  // nacteni 1. matice ze souboru
  stav = loadMatrix(soubor1, &m1);
  if (stav != EOK)
  { // nastala chyba
    printMsg(stav);
    return EXIT_FAILURE;
  }
  // uzavreni 1. souboru
  stav = fclose(soubor1);
  if (stav == EOF)
  { // soubor se nepodarilo uzavrit
    // pokracuji dale, na funkcnost to nema vliv
    // printMsg(EFCLOSE);
    // freeMatrix(&m1)
    // return EXIT_FAILURE;
  }

  // zavislost funkce na poctu parametru
  if (params.pocet == 2) // funkce potrebuje 2 soubory
  {
    // otevreni 2 souboru a nacteni ukazatele na soubor
    soubor2 = fopen(params.zdroj2, "r");
    if (soubor2 == NULL)
    { // soubor se nepodarilo otevrit
      printMsg(EFOPEN);
      freeMatrix(&m1);
      return EXIT_FAILURE;
    }
    // nacteni 2. matice ze souboru
    stav = loadMatrix(soubor2, &m2);
    if (stav != EOK)
    { // nastala chyba
      printMsg(stav);
      freeMatrix(&m1);
      return EXIT_FAILURE;
    }
    // uzavreni 2. souboru
    stav = fclose(soubor2);
    if (stav == EOF)
    { // soubor se nepodarilo uzavrit
      // pokracuji dale, na funkcnost to nema vliv
      //  printMsg(EFCLOSE);
      //  freeMatrix(&m1);
      //  freeMatrix(&m2);
      //  return EXIT_FAILURE;
    }

    // podle zadane funkce provede danou operaci
    switch (params.funkce)
    { // provedeni operace
      case ADDMATRIX: stav = addMatrix(&m1, &m2);
                      break;
      case MULTMATRIX: stav = multMatrix(&m1, &m2, &m3);
                       // vymena ukazatelu a uvolneni pameti treti matice
                       // m1 bude ukazovat na vyslednou matici
                       if (stav == EOK)
                       {
                         TMatrix pom;
                         pom = m1;
                         m1 = m3;
                         m3 = pom;
                         freeMatrix(&m3);
                       }
                       break;
    }

    if (stav != EOK)
    { // doslo k chybe
      printMsg(stav);
      freeMatrix(&m1);
      freeMatrix(&m2);
      return EXIT_FAILURE;
    }

    // vypsani vysledku ulozeneho v 1. matici
    printMatrix(&m1);
    freeMatrix(&m1); //uvolneni pameti
    freeMatrix(&m2);
  }

  // zavislost funkce na poctu parametru
  if (params.pocet == 1) // funkce potrebuje 1 soubor
  {
    // podle zadane funkce provedem danou operaci
    switch (params.funkce)
    { // provedeni operace
      case MONOMATRIX: stav = monoMatrix(&m1);
                       break;
      case SPIRALMATRIX: stav = spiralMatrix(&m1);
                         break;
    }

    if (stav != EOK)
    { // doslo k chybe
      printMsg(stav);
      freeMatrix(&m1);
      return EXIT_FAILURE;
    }
    //uvolneni pameti
    freeMatrix(&m1);
  }

  return EXIT_SUCCESS;
}  // main()

/* konec souboru proj3.c */
