from regression_tests import *

class Test(Test):
	settings = TestSettings(
		input='sed-strip',
		args='-k'
	)

	def test_check_for_all_currently_detected_strings(self):
		assert self.out_c.has_string_literal( ' truncated to %d characters\\n' )
		assert self.out_c.has_string_literal( '%02x' )
		assert self.out_c.has_string_literal( 'hold space' )
		assert self.out_c.has_string_literal( 'line %D' )
		assert self.out_c.has_string_literal( 'r' )
		assert self.out_c.has_string_literal( 'sed: ' )
		assert self.out_c.has_string_literal( 'sed: RE error, %o\\n' )
		assert self.out_c.has_string_literal( 'sed: RE too long: %s\\n' )
		assert self.out_c.has_string_literal( "sed: can't open %s\\n" )
		assert self.out_c.has_string_literal( 'sed: garbled command %s\\n' )
		assert self.out_c.has_string_literal( 'sed: line too long\\n' )
		#assert self.out_c.has_string_literal( 'sed: too many commands, last was %s\\n' )
		assert self.out_c.has_string_literal( "sed: too many {'s\\n" )
		assert self.out_c.has_string_literal( 'sed: undefined label %s\\n' )
		assert self.out_c.has_string_literal( 'sed: too much text: %s\\n' )
		assert self.out_c.has_string_literal( 'sed: garbled address %s\\n' )
		assert self.out_c.has_string_literal( 'sed: first RE must be non-null\\n' )
		assert self.out_c.has_string_literal( 'ng garbage\\n' )
		assert self.out_c.has_string_literal( 'sed: no such command as %s\\n' )
		assert self.out_c.has_string_literal( 'sed: unknown flag %c\\n' )
		#assert self.out_c.has_string_literal( 'sed: cannot create %s\\n' )
		assert self.out_c.has_string_literal('sed: cannot open command-file %s\\n')

	# Currently detected functions which have their named (from symbols) counterparts in not-stripped binary.
	#
	def test_check_for_all_currently_detected_functions(self):
		assert self.out_c.has_func( 'function_10000638' )  # _init
		assert self.out_c.has_func( 'entry_point' )  # function_10000690 _start
		assert self.out_c.has_func( 'function_1000075c' )  # call___do_global_dtors_aux
		assert self.out_c.has_func( 'function_10000778' )  # frame_dummy
		assert self.out_c.has_func( 'function_100007c0' )  # call_frame_dummy
		assert self.out_c.has_func( 'function_100007dc' )  # rhscomp
		assert self.out_c.has_func( 'function_10000880' )  # recomp
		assert self.out_c.has_func( 'function_10001028' )  # compile
		assert self.out_c.has_func( 'function_10001468' )  # search
		assert self.out_c.has_func( 'function_100014e0' )  # resolve
		assert self.out_c.has_func( 'main' )  # main
		assert self.out_c.has_func( 'function_1000188c' )  # ycomp
		assert self.out_c.has_func( 'advance' )  # advance
		assert self.out_c.has_func( 'function_100025d8' )  # match
		assert self.out_c.has_func( 'function_10002750' )  # selected
		assert self.out_c.has_func( 'function_10002904' )  # place
		assert self.out_c.has_func( 'function_100029cc' )  # dosub
		assert self.out_c.has_func( 'function_10002bf8' )  # substitute
		assert self.out_c.has_func( 'function_10002cac' )  # listto
		assert self.out_c.has_func( 'function_10002ddc' )  # dumpto
		assert self.out_c.has_func( 'function_10002e84' )  # truncated
		assert self.out_c.has_func( 'function_10002f2c' )  # my_getline
		assert self.out_c.has_func( 'function_10002fb0' )  # readout
		assert self.out_c.has_func( 'function_10003094' )  # command
		assert self.out_c.has_func( 'function_10003750' )  # execute
		assert self.out_c.has_func( 'function_100039d4' )  # __do_global_ctors_aux

	# Functions reported in #1050 as not detected.
	# TODO: matula, uncomment when fixed.
	#
	def test_check_for_functions_not_detected_before_1050_fix(self):
		assert self.out_c.has_func( 'function_10000dec' ) # cmdline
		assert self.out_c.has_func( 'function_100019c8' ) # cmdcomp
		assert self.out_c.has_func( 'function_10001468' ) # search
		assert self.out_c.has_func( 'function_100014e0' ) # resolve
		assert self.out_c.has_func( 'main' ) # main
		assert self.out_c.has_func( 'function_1000391c' ) # __libc_csu_init
		assert self.out_c.has_func( 'function_10003a24' ) # call___do_global_ctors_aux

	def test_bug_1060(self):
		assert self.out_c.has_func( 'function_100006b4' )  # __do_global_dtors_aux
		assert self.out_c.has_func( 'function_10000f28' )  # address
		assert self.out_c.has_func( 'gettext' )  #
