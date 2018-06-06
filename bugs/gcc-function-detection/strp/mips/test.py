from regression_tests import *

class Test(Test):
	settings = TestSettings(
		input='strp-strip',
		args='-k'
	)

	def test_check_for_all_currently_detected_strings(self):
		assert self.out_c.has_string_literal( ' Copyright(c) 1996, 1998 by ' )
		assert self.out_c.has_string_literal( '%c' )
		assert self.out_c.has_string_literal( '%s%s%s%s' )
		assert self.out_c.has_string_literal( '%s: %s: %s\\n' )
		assert self.out_c.has_string_literal( '0.9' )
		assert self.out_c.has_string_literal( 'Cannot open file: %s for writing\\n' )
		assert self.out_c.has_string_literal( 'Cannot open tempfile %s for reading\\n' )
		assert self.out_c.has_string_literal( 'Eddie Buckley <eddie@sjfn.nb.ca>\\n' )
		assert self.out_c.has_string_literal( 'Error opening file: %s \\n' )
		assert self.out_c.has_string_literal( 'Fix line breaks in FILE(s), or standard input to standard output.' )
		assert self.out_c.has_string_literal( "Try `%s -h' for more information.\\n" )
		assert self.out_c.has_string_literal( 'Unable to create tempory file\\n' )
		assert self.out_c.has_string_literal( 'Usage: %s [OPTION] [FILE]...\\n' )
		assert self.out_c.has_string_literal( '\\nIf more than one command line option is present only the first one is used.' )
		assert self.out_c.has_string_literal( '\\nWith no FILE or when FILE is - read from standard input and write to standard\\n output.\\n' )
		assert self.out_c.has_string_literal( '\\n\\t-d\\tmake DOS format (CR-LF)' )
		assert self.out_c.has_string_literal( '\\t-h\\tshow this help and version number' )
		assert self.out_c.has_string_literal( '\\t-m\\tmake MAC/Amiga format (CR)' )
		assert self.out_c.has_string_literal( '\\t-u\\tmake UNIX format (LF)' )
		assert self.out_c.has_string_literal( '\\t-v\\tprint version number and exit' )
		assert self.out_c.has_string_literal( 'rb' )
		assert self.out_c.has_string_literal( 'removal of temp file failed\\n' )
		assert self.out_c.has_string_literal( 'strp' )
		assert self.out_c.has_string_literal( 'strp version ' )
		assert self.out_c.has_string_literal( 'usage %s %s\\n' )
		assert self.out_c.has_string_literal( 'wb' )

	# Currently detected functions which have their named (from symbols) counterparts in not-stripped binary.
	#
	def test_check_for_all_currently_detected_functions(self):
		assert self.out_c.has_func( 'function_8900018' )  # _init
		assert self.out_c.has_func( 'entry_point' )  # function_890003c
		assert self.out_c.has_func( 'function_8900180' )  # main
		assert self.out_c.has_func( 'function_8900228' )  # call___do_global_dtors_aux
		assert self.out_c.has_func( 'function_89002f8' )  # frame_dummy
		assert self.out_c.has_func( 'function_89004a0' )  # help
		assert self.out_c.has_func( 'function_8900514' )  # ver
		assert self.out_c.has_func( 'function_8900554' )  # arg_parse
		assert self.out_c.has_func( 'function_890060c' )  # isdir
		assert self.out_c.has_func( 'function_8900638' )  # usage
		assert self.out_c.has_func( 'function_8900668' )  # try
		assert self.out_c.has_func( 'main' )  # main
		assert self.out_c.has_func( 'function_89044c8' )  # rindex

	def test_check_for_some_static_functions(self):
		assert self.out_config.is_statically_linked('__errno', 0x8900d78)
		assert self.out_config.is_statically_linked('stat', 0x8904f9c)
		assert self.out_config.is_statically_linked('putchar', 0x8903ea4)
		assert self.out_config.is_statically_linked('fstat', 0x8904444)

	# Functions reported in #1050 as not detected.
	# TODO: matula, uncomment when fixed.
	#
	def test_check_for_functions_not_detected_before_1050_fix(self):
		assert self.out_c.has_func( 'function_8900354' )  # call_frame_dummy
		assert self.out_c.has_func( 'function_8900368' )  # to_unix
		assert self.out_c.has_func( 'function_89003cc' )  # to_dos
		assert self.out_c.has_func( 'function_8900444' )  # to_mac
		#assert self.out_c.has_func( 'function_8903eb8' )  # _putchar_r

		# TODO: there is many functions like this, they may not be used anywhere. they all start with something like:
		# 		addiu $sp, $sp, 0xfffffffffffffff8
		#assert self.out_c.has_func( 'function_8913ad0' )  # getpid
