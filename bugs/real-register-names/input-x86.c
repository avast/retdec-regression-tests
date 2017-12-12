// Input file for input-x86.exe.
//
// Decompilation:
//
//   decompile.sh input.c

__attribute__((fastcall)) int func(int a) {
	printf("%d\n", a);
}

int main(int argc, char **argv) {
	func(argc);
	return 0;
}
