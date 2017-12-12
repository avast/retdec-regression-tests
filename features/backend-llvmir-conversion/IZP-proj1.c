/*
 * Soubor:  proj1.c
 * Autor:   Petr Zemek, xzemek02@stud.fit.vutbr.cz
 * Projekt: IZP c. 1 - Ciselne soustavy
 * Popis:   Program prevadi zadane cislo mezi zadanymi ciselnymi soustavami.
 */

//
// TODO: unchecked decompiled output
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define NDEBUG 1
#include <assert.h>

/**
 * Maximalni jednociferna cislice (cifry jsou 0-9)
 */
#define MAX_CIFRA 9

/** Zaklad minimalni ciselne soustavy. */
const int MIN_ZAKLAD = 2;
/** Zaklad maximalni ciselne soustavy. */
const int MAX_ZAKLAD = 36;

/**
 * Struktura obsahujici hodnoty parametru prikazove radky.
 */
typedef struct params
{
  int zaklad1; /**< Zaklad ciselne soustavy vstupniho cisla. */
  int zaklad2; /**< Zaklad ciselne soustavy vystupniho cisla. */
} TParams;

/** Chybove kody - stavy. */
enum tstavy
{
  EOK,       /**< Bez chyby. */
  S_STEJNE,  /**< Zaklady byly navzajem stejne. */
  S_RUZNE,   /**< Zaklady byly navzajem ruzne. */
  CE_NC,     /**< Nezadano cislo. */
  CE_NZ,     /**< Neznamy znak. */
  CE_PN,     /**< Zadane pismeno neexistuje v dane soustave. */
  CE_CN,     /**< Zadane cislo neexistuje v dane soustave. */
};

/**
 * Vytiskne na standardni vystup text s napovedou.
 */

void printHelp(void)
{
  printf("Program Ciselne soustavy.\n"
         "Autor: Petr Zemek\n"
         "Program provadi prevody mezi ciselnymi soustavami. Cislo, ktere\n"
         "ma program zpracovat se nacita ze standardniho vstupu.\n"
         "Pouziti: proj1 -h\n"
         "         proj1 Z1 Z2\n"
         "Popis parametru:\n"
         "  -h    Vypise tuto obrazovku s napovedou.\n"
         "  Z1    Zaklad ciselne soustavy vstupniho cisla (2-36).\n"
         "  Z2    Zaklad ciselne soustavy vystupniho cisla (2-36).\n"
         );
}  // printHelp()

/**
 * Zpracuje argumenty prikazoveho radku a vrati je ve strukture TParams.
 * Pokud je format argumentu chybny, ukonci program s chybovym kodem.
 * @param argc Pocet argumentu.
 * @param argv Pole textovych retezcu s argumenty.
 * @return Vraci analyzovane argumenty prikazoveho radku.
 */
TParams getParams2(int argc, char *argv[]);
TParams getParams(int argc, char *argv[])
{
  TParams result =
  { // inicializace struktury
    .zaklad1 = 0,
    .zaklad2 = 0
  };

  // byl zadan pouze 1 parametr a byl to parametr -h
  if (argc == 2 && strcmp("-h", argv[1]) == 0)
  { // tisk napovedy
    printHelp();
    exit(EXIT_SUCCESS);
  }
  // byly zadany 2 parametry
  else if (argc == 3)
  { // pokus o prevedeni argumentu na cisla
    result.zaklad1 = atoi(argv[1]); // zaklad 1. soustavy
    result.zaklad2 = atoi(argv[2]); // zaklad 2. soustavy
  }
  // chybny pocet argumentu nebo jsou argumenty mimo rozsah
  if (argc != 3 ||
      result.zaklad1 < MIN_ZAKLAD || result.zaklad1 > MAX_ZAKLAD ||
      result.zaklad2 < MIN_ZAKLAD || result.zaklad2 > MAX_ZAKLAD)
  { // vypise na standardni chybovy vystup chybovou hlasku.
    fprintf(stderr, "Program byl spusten s chybnymi parametry!\n"
                    "Spustte program s parametrem -h pro napovedu.\n");
    exit(EXIT_FAILURE);
  }

  return result;
}  // getParams()

/**
 * Otestuje, zda posledni alokacni operace probehla v poradku. Pokud ne,
 * vypise chybovou hlasku a ukonci program s chybovym kodem.
 * @param ptr Ukazatel na posledne alokovanou pamet.
 */
//void testAlloc2(void *ptr);
void testAlloc2(void *ptr)
{
  if (ptr == NULL)
  { // vypise na standardni chybovy vystup chybovou hlasku.
    fprintf(stderr, "Nedostatek pameti!\n");
    exit(EXIT_FAILURE);
  }
} // testAlloc()

/**
 * Nacte radek ze standardniho vstupu. V nactenem retezci se nebude vyskytovat
 * znak konce radku '\n'.
 *
 * @param pLine Textovy retezec predavany odkazem. Pokud bude obsahovat NULL,
 *   funkce alokuje retezec sama. Jinak musi byt buffer spravne alokovany
 *   pomoci malloc() a parametr N musi obsahovat jeho rozmìr. Pokud se nacitany
 *   retezec do bufferu nevejde, funkce jej zvetsi pomoci realloc().
 * @param N Velikost bufferu *pLine predavana odkazem. Po skonceni funkce bude
 *   tento parametr obsahovat aktualni rozmer bufferu (ne retezce!).
 * @param stream Popisovac otevreneho streamu (souboru), ze ktereho se bude
 *   radek nacitat. Pro nacitani ze standardniho vstupu staci predat systemovou
 *   promennou stdin.
 * @return Vraci delku nacteneho retezce. Pokud na vstupu byly nulove znaky
 *   '\0', funkce strlen() nad ziskanym retezcem vrati jinou hodnotu!
 */
//unsigned int nactiCislo2(char **pLine, unsigned int *N, FILE *stream);
unsigned int nactiCislo(char **pLine, unsigned int *N, FILE *stream)
{
  // test, zda byly parametry predany odkazem v poradku
  assert(pLine != NULL);
  assert(N != NULL);
  assert(stream != NULL);

  const int B_INCREMENT = 16;
  int blockSize = *N;

  if (*pLine == NULL)
  { // uzivatel nic nealokoval
    blockSize = B_INCREMENT;
    *pLine = malloc(blockSize*sizeof(char));
     testAlloc2(*pLine);
  }

  int c;
  int i = 1; // citac

  // nacte radek ze standardniho vstupu
  while ((c = getc(stream)) != EOF && c != '\n')
  {
    (*pLine)[i] = c;
    i += 1;
    if ((i % blockSize) == 0)
    { // pokud je na konci bloku, je potreba jej natahnout
      blockSize += B_INCREMENT;
      *pLine = realloc(*pLine, blockSize);
      testAlloc2(*pLine);
    }
  }

  // Pozor! Pole predavane odkazem se musí indexovat takto. Bez závorky
  // bychom indexovali pole ukazatelu, protoze operator * ma nizsi prioritu
  // nez [].
  (*pLine)[i] = '\0'; // na zaver je potreba retezec spravne ukoncit

  *N = blockSize;

  return i+1; // vraci delku retezce
}  // nactiCislo()

/**
 * Funkce zjisti, zda zadane cislo zadane na vstupu existuje v dane soustave.
 * Pokud ne, vraci chybovy - stavovy kod.
 *
 * @param s1 Zaklad vstupni soustavy zadany jako parametr
 *   pri spusteni programu.
 * @param cislo[] Textovy retezec zadany na vstupu.
 *   (zadane cislo, ktere chceme zkontrolovat)
 * @return Vraci chybovy - stavovy kod
 */
int cisloExistuje(int s1, char cislo[])
{
  int i = 0; // citac

  // test, zda bylo neco zadano
  if (cislo[0] == '\0')
  {  // vrati chybovy kod
      return CE_NC; // Nezadano cislo.
  }

  // pokud bylo neco zadano, zjistime, zda je dane cislo ve spravnem formatu
  // a existuje v dane soustave
  while ((cislo[i]) != '\0')
  {
    // kontrola, zda nebyl zadan jako cislo neznamy znak
    if  (((cislo[i] < '0') || (cislo[i] > '9')) &&
         ((cislo[i] < 'A') || (cislo[i] > 'Z')))
    {  // vrati chybovy kod
      return CE_NZ; // Neznamy znak
    }
    // kontrola, zda dane cislo existuje v dane soustave
    // soustavy 11-36
    if ((cislo[i] >= 'A') && (cislo[i] <= 'Z') && ((cislo[i] - '7') >= s1))
    {  // vrati chybovy kod
      return CE_PN; // Zadane pismeno neexistuje v dane soustave.
    }
    // kontrola, zda dane cislo existuje v dane soustave
    // soustavy 2-10
    if ((cislo[i] >= '0') && (cislo[i] <= '9') && ((cislo[i] - '0') >= s1))
    {  // vrati chybovy kod
      return CE_CN; // Zadane cislo neexistuje v dane soustave.
    }
    i++;
  }

  return EOK; // bez chyby
} // cisloExistuje()


/**
 * Funkce zjisti, zda jsou zadane soustavy shodne ci nikoliv.
 * Pokud se shoduji, neni treba provadet zadne vypocty
 * a muzeme rovnou vypsat vysledek
 *
 * @param s1 Zaklad vstupni soustavy zadany jako parametr
 *   pri spusteni programu.
 * @param s2 Zaklad vystupni soustavy zadany jako parametr
 *   pri spusteni programu.
 * @param cislo[] Textovy retezec zadany na vstupu.
 * @return Vraci S_STEJNE pokud byly zaklady stejne a S_RUZNE pokud se lisi.
 */

int stejneZaklady(int s1, int s2, char cislo[])
{
  if (s1 == s2)
  {
    int i = 0; // citac

    while (cislo[i] != '\0')
    { // vytiskneme cislo (vysledek)
      fprintf(stdout, "%c", cislo[i]);
      i++;
    }

    return S_STEJNE; // soustavy byly stejne
  }
  return S_RUZNE; // soustavy maji ruzne zaklady
} // stejneZaklady()

/**
 * Funkce prevede dane cislo do desitkove soustavy.
 *
 * @param s1 Zaklad vstupni soustavy zadany jako parametr
 *   pri spusteni programu.
 * @param cislo[] Textovy retezec zadany na vstupu.
 *   (zadane cislo, ktere chceme prevest)
 * @param delka Delka retezce vcetne ukoncovaciho znaku '\0'
 * @return Vraci cislo v desitkove soustave.
 */
unsigned long int prevodDoDesitkove(int s1, char cislo[], unsigned int delka)
{
  unsigned int i; // citac
  unsigned int hodnota;
  unsigned long int desCislo = 0, zalozniVysledek;

  for (i = 0; i < (delka - 1); i++)
  { // prevod znaku na cislo
    if (cislo[i] < 'A') // ASCII kod = 65
      { // cislo
        hodnota = cislo[i] - '0';  // ASCII kod = 48
      }
    else
      { // znak
        hodnota = cislo[i] - '7';  // ASCII kod = 55
      }
    zalozniVysledek = desCislo; // uchovam si vysledek do pomocne promenne
    desCislo *= s1;
    desCislo += hodnota;
    // kontrola, zda nedoslo k preteceni
    if ((desCislo / s1) != zalozniVysledek)
     { // vypise na standardni chybovy vystup chybovou hlasku.
       fprintf(stderr, "Doslo k chybe preteceni.\n");
       free(cislo); // uvolnim pamet
       exit(EXIT_FAILURE);
     }
  }

  return desCislo; // vraci cislo v desitkove soustave
} // prevodDoDesitkove

/**
 * Funkce prevede cislo v desitkove soustave do vystupni soustavy soustavy.
 *
 * @param desCislo Cislo v desitkove soustave.
 * @param s2 Vystupni soustava, do ktere budeme prevadet cislo v des. soustave.
 */
void prevodDoVystupni(unsigned long int desCislo, int s2)
{
  int i = 0; // citac
  int zbytek;
  char *cislo = NULL; // zde budeme ukladat vysledek

  const int INCREMENT = 10;
  int velikostBloku = 0;

  // alokujeme pamet
  velikostBloku = INCREMENT;
  cislo = malloc(velikostBloku*sizeof(char));
  testAlloc2(cislo);

  // postupnym delenim a zapisem do pole dostanu vysledek
  // (zatim ale v opacnem poradi)
  do
  {
    zbytek  = desCislo % s2;
    desCislo = desCislo / s2;
    if (zbytek > MAX_CIFRA)
      cislo[i] =  zbytek + '7'; // ASCII kod = 55
    else
      cislo[i] =  zbytek + '0'; // ASCII kod = 48
    i++;
    if ((i % velikostBloku) == 0)
    { // pokud je na konci bloku, je potreba jej natahnout
      velikostBloku += INCREMENT;
      cislo = realloc(cislo, velikostBloku);
      testAlloc2(cislo);
    }
  } while (desCislo > 0);

  // vytiskneme cislo (musime tisknout od konce)
  for (i--; i >= 0; i--)
  {
	printf("%c", cislo[i]);
  }

  free(cislo); // uvolnim pamet
} // prevodDoVystupni

/**
 * Hlavni program
 */
int main(int argc, char *argv[])
{
  TParams params = getParams(argc, argv); // vyhodnotim parametry
  char *line = NULL;
  unsigned int buflen = 0;
  unsigned long int cisloDesitkova; // vysledek
  int stav;

  // nacte cislo
  unsigned int delkaCisla = nactiCislo(&line, &buflen, stdin);

  // overi, zda dane cislo existuje v dane soustave
  if ((stav = cisloExistuje(params.zaklad1, line)) != EOK)
  {
    switch (stav)
    {
      case CE_NC: // Nezadano cislo.
        fprintf(stderr, "Nezadal jsi zadne cislo.\n");
        break;
      case CE_NZ: // Neznamy znak.
        fprintf(stderr, "Neznamy znak.\n");
        break;
      case CE_PN: // Zadane pismeno neexistuje v dane soustave.
        fprintf(stderr, "Zadane pismeno neexistuje v dane soustave.\n");
        break;
      case CE_CN: // Zadane cislo neexistuje v dane soustave.
        fprintf(stderr, "Zadane cislo neexistuje v dane soustave.\n");
        break;
    }
   free(line); // uvolnim pamet
   return EXIT_FAILURE;
  }

  // pokud se shoduji obe soustavy, je zbytecne provadet jakekoliv funkce
  // a rovnou se vytiskne na standartni vystup vysledek
  if ((stav = stejneZaklady(params.zaklad1, params.zaklad2, line)) != EOK)
  {
    switch (stav)
    {
      case S_STEJNE: // stejne zaklady, cislo je vypsano -> ukoncim program
        free(line);  // uvolnim pamet
        return EXIT_SUCCESS;
      case S_RUZNE:  // ruzne zaklady, pokracuje se dale
        break;
    }
  }

  // prevede zadane cislo do desitkove soustavy
  // a ulozi ji do promenne cisloDesitkova
  cisloDesitkova = prevodDoDesitkove(params.zaklad1, line, delkaCisla);

  // prevede cislo z desitkove soustavy do dane vystupni soustavy
  prevodDoVystupni(cisloDesitkova, params.zaklad2);

  free(line); // uvolnim pamet
  return EXIT_SUCCESS;
}  // main()

