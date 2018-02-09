from regression_tests import *

class Test(Test):
	settings = TestSettings(
		input='gzip-strip',
		args='-k'  # TODO: matula, not sure if some functions are not called, or we just do not detect it.
	)

	def test_check_for_all_currently_detected_strings(self):
		assert self.out_c.has_string_literal( '%s: illegal option -- %c\\n' )
		assert self.out_c.has_string_literal( 'z' )
		assert self.out_c.has_string_literal( 'read from' )
		assert self.out_c.has_string_literal( '.gz' )
		#assert self.out_c.has_string_literal( ' -c --stdout      write on standard output, keep original files unchanged' )
		assert self.out_c.has_string_literal( '--' )
		assert self.out_c.has_string_literal( 'de' )
		assert self.out_c.has_string_literal( 'argc<=0' )
		#assert self.out_c.has_string_literal( '%s: -Z not supported in this version\\n' )
		assert self.out_c.has_string_literal( '%s: -r not supported on this system\\n' )
		assert self.out_c.has_string_literal( '\\n%s: %s: %s\\n' )
		assert self.out_c.has_string_literal( '%s: unexpected end of file\\n' )
		assert self.out_c.has_string_literal( '%5s %08lx %11s ' )
		assert self.out_c.has_string_literal( '.tar' )
		assert self.out_c.has_string_literal( ' (totals)' )
		assert self.out_c.has_string_literal( '%s: %s is encrypted -- get newer version of gzip\\n' )
		assert self.out_c.has_string_literal( 'NO_MEMORY_H ' )
		assert self.out_c.has_string_literal( '\\n%s: %s: not a valid zip file\\n' )
		assert self.out_c.has_string_literal( 'out of memory' )
		assert self.out_c.has_string_literal( 'method  crc     date  time  ' )
		assert self.out_c.has_string_literal( '%s: %s is a a multi-part gzip file -- get newer version of gzip\\n' )
		assert self.out_c.has_string_literal( '%s: %s: extra field of %u bytes ignored\\n' )
		assert self.out_c.has_string_literal( '%9ld %9ld ' )
		assert self.out_c.has_string_literal( 'compressed  uncompr. ratio uncompressed_name' )
		assert self.out_c.has_string_literal( 'name too short' )
		assert self.out_c.has_string_literal( '.exe' )
		assert self.out_c.has_string_literal( ' OK\\n' )
		assert self.out_c.has_string_literal( 'usage: %s [-%scdfhlLnN%stvV19] [-S suffix] [file ...]\\n' )
		assert self.out_c.has_string_literal( '%s: %s has flags 0x%x -- get newer version of gzip\\n' )
		assert self.out_c.has_string_literal( ' %s\\n' )
		assert self.out_c.has_string_literal( 'HAVE_UNISTD_H ' )
		assert self.out_c.has_string_literal( 'cat' )
		assert self.out_c.has_string_literal( 'gzcat' )
		assert self.out_c.has_string_literal( "%s: option `--%s' doesn't allow an argument\\n" )
		assert self.out_c.has_string_literal( '%2ld.%1ld%%' )
		# The following two strings are not found in the generated C after a
		# switch to LLVM 3.6. The reason is that opt generates slightly
		# different code that back-end does not restructure correctly. We
		# should improve the structuring, but this is a task for a more time
		# than we have at the moment.
		# assert self.out_c.has_string_literal( ' incomplete literal tree\\n' )
		# assert self.out_c.has_string_literal( ' incomplete distance tree\\n' )
		assert self.out_c.has_string_literal( "can't recover suffix\\n" )
		assert self.out_c.has_string_literal( 'For help, type: %s -h\\n' )
		assert self.out_c.has_string_literal( '.' )
		assert self.out_c.has_string_literal( '%s: %s: part number %u\\n' )
		assert self.out_c.has_string_literal( '\\n%s: ' )
		assert self.out_c.has_string_literal( 'GZIP' )
		assert self.out_c.has_string_literal( "%s: unrecognized option `%c%s'\\n" )
		assert self.out_c.has_string_literal( 'bad pack level' )
		assert self.out_c.has_string_literal( 'Bad table\\n' )
		assert self.out_c.has_string_literal( '                            %9lu %9lu ' )
		assert self.out_c.has_string_literal( ' \\t' )
		assert self.out_c.has_string_literal( "%s: option `%c%s' doesn't allow an argument\\n" )
		assert self.out_c.has_string_literal( 'gun' )
		assert self.out_c.has_string_literal( '%s: %s: unknown method %d -- get newer version of gzip\\n' )
		assert self.out_c.has_string_literal( 'un' )
		assert self.out_c.has_string_literal( "%s: option `%s' requires an argument\\n" )
		assert self.out_c.has_string_literal( 'fstat(stdin)' )
		assert self.out_c.has_string_literal( "%s: unrecognized option `--%s'\\n" )
		assert self.out_c.has_string_literal( 'POSIXLY_CORRECT' )
		assert self.out_c.has_string_literal( "%s: option `%s' is ambiguous\\n" )
		assert self.out_c.has_string_literal( '%s: option requires an argument -- %c\\n' )
		assert self.out_c.has_string_literal( '%s: compressed data not %s a terminal. Use -f to force %scompression.\\n' )
		assert self.out_c.has_string_literal( 'written to' )
		#assert self.out_c.has_string_literal( '   Copyright (C) 1992-1993 Jean-loup Gailly' )
		assert self.out_c.has_string_literal( 'ab:cdfhH?lLmMnNqrS:tvVZ123456789' )

	# Currently detected functions which have their named (from symbols) counterparts in not-stripped binary.
	#
	def test_check_for_all_currently_detected_functions(self):
		assert self.out_c.has_func( 'function_8900018' )  #
		assert self.out_c.has_func( 'entry_point' )  # function_890003c
		assert self.out_c.has_func( 'function_8900180' )  #
		assert self.out_c.has_func( 'function_8900228' )  #
		assert self.out_c.has_func( 'function_89002e4' )  #
		assert self.out_c.has_func( 'function_89002f8' )  #
		assert self.out_c.has_func( 'function_8900354' )  #
		assert self.out_c.has_func( 'function_8900368' )  #
		assert self.out_c.has_func( 'function_89003f4' )  #
		assert self.out_c.has_func( 'function_890046c' )  #
		assert self.out_c.has_func( 'function_89004ac' )  #
		assert self.out_c.has_func( 'function_89004e8' )  #
		assert self.out_c.has_func( 'function_890062c' )  #
		assert self.out_c.has_func( 'function_890066c' )  #
		assert self.out_c.has_func( 'function_8900734' )  #
		assert self.out_c.has_func( 'function_89008f8' )  #
		assert self.out_c.has_func( 'function_8901448' )  #
		assert self.out_c.has_func( 'function_8901788' )  #
		assert self.out_c.has_func( 'main' )  #
		assert self.out_c.has_func( 'function_89030d8' )  #
		assert self.out_c.has_func( 'function_8903728' )  #
		assert self.out_c.has_func( 'function_890393c' )  #
		assert self.out_c.has_func( 'function_8903b14' )  #
		assert self.out_c.has_func( 'function_89040f0' )  #
		assert self.out_c.has_func( 'function_8904270' )  #
		assert self.out_c.has_func( 'function_8904318' )  #
		assert self.out_c.has_func( 'function_8904458' )  #
		assert self.out_c.has_func( 'function_89045a8' )  #
		assert self.out_c.has_func( 'function_89047cc' )  #
		assert self.out_c.has_func( 'function_8904988' )  #
		assert self.out_c.has_func( 'function_8904ba8' )  #
		assert self.out_c.has_func( 'function_8904c54' )  #
		assert self.out_c.has_func( 'function_89051f8' )  #
		assert self.out_c.has_func( 'function_8905578' )  #
		assert self.out_c.has_func( 'function_890588c' )  #
		assert self.out_c.has_func( 'function_89058c4' )  #
		assert self.out_c.has_func( 'function_89058e8' )  #
		assert self.out_c.has_func( 'function_8905a14' )  #
		assert self.out_c.has_func( 'function_8905bf8' )  #
		assert self.out_c.has_func( 'function_8905d48' )  #
		assert self.out_c.has_func( 'function_8906474' )  #
		assert self.out_c.has_func( 'function_8906700' )  #
		assert self.out_c.has_func( 'function_8906ca8' )  #
		assert self.out_c.has_func( 'function_8906ce0' )  #
		assert self.out_c.has_func( 'function_8907394' )  #
		assert self.out_c.has_func( 'function_8907bdc' )  #
		assert self.out_c.has_func( 'function_8907d4c' )  #
		assert self.out_c.has_func( 'function_8907ef8' )  #
		assert self.out_c.has_func( 'function_8907f9c' )  #
		assert self.out_c.has_func( 'function_8907ff8' )  #
		assert self.out_c.has_func( 'function_8908024' )  #
		assert self.out_c.has_func( 'function_8908074' )  #
		assert self.out_c.has_func( 'function_89082a8' )  #
		assert self.out_c.has_func( 'function_89082ec' )  #
		assert self.out_c.has_func( 'function_8908330' )  #
		assert self.out_c.has_func( 'function_8908368' )  #
		assert self.out_c.has_func( 'function_89083e0' )  #
		assert self.out_c.has_func( 'function_8908634' )  #
		assert self.out_c.has_func( 'function_8908668' )  #
		assert self.out_c.has_func( 'function_89086e4' )  #
		assert self.out_c.has_func( 'function_890875c' )  #
		assert self.out_c.has_func( 'function_89087b0' )  #
		assert self.out_c.has_func( 'function_890979c' )  #
		assert self.out_c.has_func( 'function_89098d8' )  #
		assert self.out_c.has_func( 'function_8909910' )  #
		assert self.out_c.has_func( 'function_8909bf8' )  #
		assert self.out_c.has_func( 'function_890a344' )  #
		assert self.out_c.has_func( 'function_890a36c' )  #
		assert self.out_c.has_func( 'function_890a3ac' )  #
		assert self.out_c.has_func( 'function_890a4bc' )  #
		assert self.out_c.has_func( 'function_890ad88' )  #
		assert self.out_c.has_func( 'function_890ada4' )  #
		assert self.out_c.has_func( 'function_890aef0' )  #
		assert self.out_c.has_func( 'function_890af1c' )  #
		assert self.out_c.has_func( 'function_890b00c' )  #
		assert self.out_c.has_func( 'function_890c1c8' )  #
		assert self.out_c.has_func( 'function_890ef4c' )  #
		assert self.out_c.has_func( 'function_89134f8' )  #
		assert self.out_c.has_func( 'function_8920084' )  #
		assert self.out_c.has_func( 'function_89200d4' )  #
		assert self.out_c.has_func( 'function_89200e8' )  #
		assert self.out_c.has_func( 'function_8920104' )  #
		assert self.out_c.has_func( 'function_89201cc' )  #
		assert self.out_c.has_func( 'function_89201d4' )  #

	# Functions reported in #1050 as not detected.
	# TODO: matula, uncomment when fixed.
	#
	def test_check_for_functions_not_detected_before_1050_fix(self):
		#assert self.out_c.has_func( 'function_8903058' )  # file_read
		assert self.out_c.has_func( 'function_8905ee4' )  # unzip
		assert self.out_c.has_func( 'function_8908240' )  # warn
		assert self.out_c.has_func( 'function_89085dc' )  # make_simple_name
		assert self.out_c.has_func( 'function_890889c' )  # copy
		assert self.out_c.has_func( 'function_8908998' )  # lzw
		assert self.out_c.has_func( 'function_8908a0c' )  # unlzw
		assert self.out_c.has_func( 'function_8909130' )  # unpack
		assert self.out_c.has_func( 'function_8909e00' )  # unlzh
