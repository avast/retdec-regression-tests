from regression_tests import *

class Test(Test):
	settings = TestSettings(
		input='sgrep-strip',
		args='-k'  # TODO: matula, not sure if some functions are not called, or we just do not detect it.
	)

	def test_check_for_all_currently_detected_strings(self):
		assert self.out_c.has_string_literal( '                                    \\r' )
		assert self.out_c.has_string_literal( '                              \\r' )
		assert self.out_c.has_string_literal( '  -----------------------------------------\\n' )
		assert self.out_c.has_string_literal( " ] 'expr' [<files...>]\\n" )
		#assert self.out_c.has_string_literal( '%d' )
		assert self.out_c.has_string_literal( '%d\\n' )
		assert self.out_c.has_string_literal( '-' )
		assert self.out_c.has_string_literal( '--' )
		assert self.out_c.has_string_literal( '.sgreprc' )
		assert self.out_c.has_string_literal( '/use/local/lib/sgreprc' )
		assert self.out_c.has_string_literal( '0.99' )
		#assert self.out_c.has_string_literal( '<input exceeded>' )
		#assert self.out_c.has_string_literal( '<stdin>' )
		assert self.out_c.has_string_literal( 'Aug 28 2014' )
		assert self.out_c.has_string_literal( 'Basic expression expected\\n' )
		assert self.out_c.has_string_literal( "Can't read input from stdin, it's already used\\n" )
		assert self.out_c.has_string_literal( 'Copyright (C) 1996  University of Helsinki' )
		assert self.out_c.has_string_literal( 'Empty stdin\\n' )
		assert self.out_c.has_string_literal( 'HOME' )
		assert self.out_c.has_string_literal( 'If no files are given stdin is used instead.' )
		assert self.out_c.has_string_literal( 'Inbuilt preprocessor not implemented yet.\\n' )
		assert self.out_c.has_string_literal( 'Memory allocation failed.\\n' )
		assert self.out_c.has_string_literal( 'No files or expressions allowed in SGREPOPT\\n' )
		assert self.out_c.has_string_literal( 'No valid files\\n' )
		assert self.out_c.has_string_literal( 'Octal number expected' )
		assert self.out_c.has_string_literal( 'Options can also be specified with SGREPOPT environment variable' )
		assert self.out_c.has_string_literal( "Premature end of parsing. ( This shouldn't happen!! )\\n" )
		assert self.out_c.has_string_literal( 'Read command file' )
		assert self.out_c.has_string_literal( 'SGREPOPT' )
		assert self.out_c.has_string_literal( 'Short write to tempfile\\n' )
		assert self.out_c.has_string_literal( "Stdin already read, Can't read expressions from stdin\\n" )
		assert self.out_c.has_string_literal( 'Strange expression type\\n' )
		assert self.out_c.has_string_literal( 'Too complex SGREPOPT\\n' )
		assert self.out_c.has_string_literal( 'Unknown escape sequence' )
		assert self.out_c.has_string_literal( 'Unknown word' )
		assert self.out_c.has_string_literal( "Usage: sgrep <options> 'region expression' [<files...>]" )
		assert self.out_c.has_string_literal( 'Usage: sgrep [ -' )
		assert self.out_c.has_string_literal( 'Warning: region end point greater than input size detected\\n' )
		assert self.out_c.has_string_literal( 'Warning: region start point greater than input size detected\\n' )
		assert self.out_c.has_string_literal( "You have to give an expression line if you don't use -f or -e switch.\\n" )
		assert self.out_c.has_string_literal( "\\\\000 in phrase does'nt work (yet)\\n" )
		assert self.out_c.has_string_literal( '\\nCopyright (C) 1996 University of Helsinki. Use sgrep -C for details,\\n' )
		assert self.out_c.has_string_literal( '\\noptions are:' )
		assert self.out_c.has_string_literal( '\\t%s\\n' )
		assert self.out_c.has_string_literal( '\\t-%c %s\\t%s\\n' )
		assert self.out_c.has_string_literal( '\\t--\\t\\tno more options' )
		assert self.out_c.has_string_literal( 'acsearch' )
		assert self.out_c.has_string_literal( 'common.c' )
		assert self.out_c.has_string_literal( 'constant gc list must be sorted' )
		assert self.out_c.has_string_literal( 'containing' )
		assert self.out_c.has_string_literal( 'creating tempfile: open' )
		assert self.out_c.has_string_literal( 'equal' )
		assert self.out_c.has_string_literal( 'eval.c' )
		assert self.out_c.has_string_literal( 'evaluating' )
		assert self.out_c.has_string_literal( 'extracting' )
		assert self.out_c.has_string_literal( 'fork' )
		assert self.out_c.has_string_literal( 'lseek <stdin>' )
		assert self.out_c.has_string_literal( 'not equal' )
		assert self.out_c.has_string_literal( 'not in' )
		#assert self.out_c.has_string_literal( 'on line' )
		assert self.out_c.has_string_literal( 'optimize.c' )
		assert self.out_c.has_string_literal( 'output' )
		assert self.out_c.has_string_literal( 'output.c' )
		assert self.out_c.has_string_literal( 'parsing' )
		assert self.out_c.has_string_literal( 'pmatch.c' )
		assert self.out_c.has_string_literal( 'preprocessor' )
		assert self.out_c.has_string_literal( 'quote: invalid oper type\\n' )
		assert self.out_c.has_string_literal( 'read <stdin>' )
		assert self.out_c.has_string_literal( 'read stdin' )
		assert self.out_c.has_string_literal( 'sgrep -h for help\\n' )
		assert self.out_c.has_string_literal( 'sgrep version %s compiled at %s\\n' )
		assert self.out_c.has_string_literal( 'sgrep version 0.99 - search a file for structured pattern' )
		assert self.out_c.has_string_literal( 'sgrep: lseek tmpfile' )
		assert self.out_c.has_string_literal( 'short read <stdin>' )
		assert self.out_c.has_string_literal( 'total' )
		assert self.out_c.has_string_literal( 'write tempfile' )

	# Currently detected functions which have their named (from symbols) counterparts in not-stripped binary.
	#
	def test_check_for_all_currently_detected_functions(self):
		assert self.out_c.has_func( '_init' )  # @ 0x8000
		assert self.out_c.has_func( 'function_8020' )  #
		assert self.out_c.has_func( 'function_80b0' )  #
		assert self.out_c.has_func( 'entry_point' )  #
		assert self.out_c.has_func( 'function_8218' )  #
		assert self.out_c.has_func( 'function_8230' )  #
		assert self.out_c.has_func( 'function_826c' )  #
		assert self.out_c.has_func( 'function_8308' )  #
		assert self.out_c.has_func( 'function_8654' )  #
		assert self.out_c.has_func( 'function_86d4' )  #
		assert self.out_c.has_func( 'function_8770' )  #
		assert self.out_c.has_func( 'function_89e0' )  #
		assert self.out_c.has_func( 'function_8b00' )  #
		assert self.out_c.has_func( 'function_8ce8' )  #
		assert self.out_c.has_func( 'function_8e4c' )  #
		assert self.out_c.has_func( 'function_9010' )  #
		assert self.out_c.has_func( 'function_902c' )  #
		assert self.out_c.has_func( 'function_915c' )  #
		assert self.out_c.has_func( 'function_91b8' )  #
		assert self.out_c.has_func( 'function_925c' )  #
		assert self.out_c.has_func( 'function_9690' )  #
		assert self.out_c.has_func( 'function_9824' )  #
		assert self.out_c.has_func( 'function_9968' )  #
		assert self.out_c.has_func( 'main' )  #
		assert self.out_c.has_func( 'function_a1d8' )  #
		assert self.out_c.has_func( 'function_a2a0' )  #
		assert self.out_c.has_func( 'function_a388' )  #
		assert self.out_c.has_func( 'function_a548' )  #
		assert self.out_c.has_func( 'function_a704' )  #
		assert self.out_c.has_func( 'function_a860' )  #
		assert self.out_c.has_func( 'function_a910' )  #
		assert self.out_c.has_func( 'function_aa98' )  #
		assert self.out_c.has_func( 'function_ab04' )  #
		assert self.out_c.has_func( 'function_ab5c' )  #
		assert self.out_c.has_func( 'function_abac' )  #
		assert self.out_c.has_func( 'function_ac24' )  #
		assert self.out_c.has_func( 'function_ac98' )  #
		assert self.out_c.has_func( 'function_acf4' )  #
		assert self.out_c.has_func( 'function_aebc' )  #
		assert self.out_c.has_func( 'function_af00' )  #
		assert self.out_c.has_func( 'function_afa8' )  #
		assert self.out_c.has_func( 'function_b024' )  #
		assert self.out_c.has_func( 'function_b048' )  #
		assert self.out_c.has_func( 'function_b088' )  #
		assert self.out_c.has_func( 'function_b100' )  #
		assert self.out_c.has_func( 'function_b144' )  #
		assert self.out_c.has_func( 'function_b174' )  #
		assert self.out_c.has_func( 'function_b304' )  #
		assert self.out_c.has_func( 'function_bb48' )  #
		assert self.out_c.has_func( 'function_bc88' )  #
		assert self.out_c.has_func( 'function_be74' )  #
		assert self.out_c.has_func( 'function_becc' )  #
		assert self.out_c.has_func( 'function_c1f4' )  #
		assert self.out_c.has_func( 'function_c2b4' )  #
		assert self.out_c.has_func( 'function_c300' )  #
		assert self.out_c.has_func( 'function_c3ac' )  #
		assert self.out_c.has_func( 'function_c48c' )  #
		assert self.out_c.has_func( 'function_c53c' )  #
		assert self.out_c.has_func( 'function_c554' )  #
		assert self.out_c.has_func( 'function_c798' )  #
		assert self.out_c.has_func( 'function_c850' )  #
		assert self.out_c.has_func( 'function_c9c0' )  #
		assert self.out_c.has_func( 'function_ca04' )  #
		assert self.out_c.has_func( 'function_ca50' )  #
		assert self.out_c.has_func( 'function_cb64' )  #
		assert self.out_c.has_func( 'function_cbb4' )  #
		assert self.out_c.has_func( 'function_ccd8' )  #
		assert self.out_c.has_func( 'function_cd2c' )  #
		assert self.out_c.has_func( 'function_cf60' )  #
		assert self.out_c.has_func( 'function_d250' )  #
		assert self.out_c.has_func( 'function_d364' )  #
		assert self.out_c.has_func( 'function_d3e8' )  #
		assert self.out_c.has_func( 'function_d44c' )  #
		assert self.out_c.has_func( 'function_d698' )  #
		assert self.out_c.has_func( 'function_d898' )  #
		assert self.out_c.has_func( 'function_d9bc' )  #
		assert self.out_c.has_func( 'function_dd58' )  #
		assert self.out_c.has_func( 'function_e064' )  #
		assert self.out_c.has_func( 'function_e384' )  #
		assert self.out_c.has_func( 'function_e64c' )  #
		assert self.out_c.has_func( 'function_e83c' )  #
		assert self.out_c.has_func( 'function_ec70' )  #
		assert self.out_c.has_func( 'function_ef7c' )  #
		assert self.out_c.has_func( 'function_f0b0' )  #
		assert self.out_c.has_func( 'function_f24c' )  #
		assert self.out_c.has_func( 'function_f42c' )  #
		assert self.out_c.has_func( 'function_fa44' )  #
		assert self.out_c.has_func( 'function_fafc' )  #
		assert self.out_c.has_func( 'function_fbd8' )  #
		assert self.out_c.has_func( 'function_feac' )  #
		assert self.out_c.has_func( 'function_ff40' )  #
		assert self.out_c.has_func( 'function_102bc' )  #

		#assert self.out_c.has_func( 'function_11254' )  # @__errno
		#assert self.out_c.has_func( 'function_1305c' )  # @__malloc_lock
		#assert self.out_c.has_func( 'function_13060' )  # @__malloc_unlock
		#assert self.out_c.has_func( 'function_15840' )  # @__sigtramp_r.12
		#assert self.out_c.has_func( 'function_18ddc' )  # @abort
		#assert self.out_c.has_func( 'function_1a814' )  # @__env_lock
		#assert self.out_c.has_func( 'function_1bd90' )  #
		#assert self.out_c.has_func( 'function_1be00' )  # @_sprintf_r

		assert self.out_c.has_func( 'function_1e6ec' )  #

	# Functions reported in #1050 as not detected.
	# TODO: matula, uncomment when fixed.
	#
	def test_check_for_functions_not_detected_before_1050_fix(self):
		assert self.out_c.has_func( 'function_a2f0' )  # end_first
		assert self.out_c.has_func( 'function_a33c' )  # start_first
		assert self.out_c.has_func( 'function_a52c' )  # give_oper_name
		#assert self.out_c.has_func( 'function_' )  #

	# Functions detected in stripped binary, that do not have their named (from symbols) counterparts in not-stripped binary.
	# TODO: matula, not sure how serious is this problem. if possible fix detection and uncomment this check.
	#
	#def test_check_for_falsely_detected_functions_before_1050_fix(self):

		#assert not self.out_c.has_func( '' )
