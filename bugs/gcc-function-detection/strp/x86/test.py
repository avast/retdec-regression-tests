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
		assert self.out_c.has_string_literal( 'Eddie Buckley <eddie@sjfn.nb.ca>\\n' )
		assert self.out_c.has_string_literal( 'Error opening file: %s \\n' )
		assert self.out_c.has_string_literal( 'Fix line breaks in FILE(s), or standard input to standard output.' )
		assert self.out_c.has_string_literal( 'No files\\n' )
		assert self.out_c.has_string_literal( "Try `%s -h' for more information.\\n" )
		assert self.out_c.has_string_literal( 'Unable to create tempory file\\n' )
		assert self.out_c.has_string_literal( 'Usage: %s [OPTION] [FILE]...\\n' )
		assert self.out_c.has_string_literal( '[-d|-h|-m|-u|-v]' )
		assert self.out_c.has_string_literal( '\\nIf more than one command line option is present only the first one is used.' )
		assert self.out_c.has_string_literal( '\\nWith no FILE or when FILE is - read from standard input and write to standard\\n output.\\n' )
		assert self.out_c.has_string_literal( '\\n\\t-d\\tmake DOS format (CR-LF)' )
		assert self.out_c.has_string_literal( '\\t-h\\tshow this help and version number' )
		assert self.out_c.has_string_literal( '\\t-m\\tmake MAC/Amiga format (CR)' )
		assert self.out_c.has_string_literal( '\\t-u\\tmake UNIX format (LF)' )
		assert self.out_c.has_string_literal( '\\t-v\\tprint version number and exit' )
		assert self.out_c.has_string_literal( 'dhmuv' )
		assert self.out_c.has_string_literal( 'rb' )
		assert self.out_c.has_string_literal( 'strp' )
		assert self.out_c.has_string_literal( 'strp version ' )
		assert self.out_c.has_string_literal( 'usage %s %s\\n' )
		assert self.out_c.has_string_literal( 'wb' )
		assert self.out_c.has_string_literal( 'Cannot open file: %s for writing\\n' )
		assert self.out_c.has_string_literal( 'Cannot open tempfile %s for reading\\n' )

	# Currently detected functions which have their named (from symbols) counterparts in not-stripped binary.
	#
	def test_check_for_all_currently_detected_functions(self):
		assert self.out_c.has_func( 'function_80486d4' )  # _init
		assert self.out_c.has_func( 'entry_point' )  # entry_point
		assert self.out_c.has_func( 'function_80488c0' )  # __x86_get_pc_thunk_bx
		assert self.out_c.has_func( 'function_80488d0' )  # deregister_tm_clones
		assert self.out_c.has_func( 'function_80488d0' )  # deregister_tm_clones
		assert self.out_c.has_func( 'function_8048900' )  # register_tm_clones
		assert self.out_c.has_func( 'function_80489a0' )  # frame_dummy
		assert self.out_c.has_func( 'function_8048aba' )  # ver
		assert self.out_c.has_func( 'function_8048aed' )  # help
		assert self.out_c.has_func( 'function_8048b54' )  # arg_parse
		assert self.out_c.has_func( 'function_8048bc8' )  # isdir
		assert self.out_c.has_func( 'function_8048c10' )  # try
		assert self.out_c.has_func( 'function_8048c35' )  # usage
		assert self.out_c.has_func( 'function_8048c5a' )  # main # TODO: this was detected as main in Jakub's outputs, now it is function_8048c5a.
		assert self.out_c.has_func( 'function_8049300' )  # __do_global_ctors_aux
		#assert self.out_c.has_func( '' )  #

	# Functions reported in #1050 as not detected.
	# TODO: matula, uncomment when fixed.
	#
	def test_check_for_functions_not_detected_before_1050_fix(self):
		#assert self.out_c.has_func( 'function_80489d0' )  # to_unix
		assert self.out_c.has_func( 'function_8048a1c' )  # to_dos
		assert self.out_c.has_func( 'function_8048a6e' )  # to_mac
		assert self.out_c.has_func( 'function_8049280' )  # __libc_csu_init
		#assert self.out_c.has_func( 'function_80492f0' )  # __libc_csu_fini
		assert self.out_c.has_func( 'function_804932c' )  # _fini
