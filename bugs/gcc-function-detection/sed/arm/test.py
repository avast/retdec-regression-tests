from regression_tests import *

class Test(Test):
	settings = TestSettings(
		input='sed-strip',
		args='-k'
	)

	def test_check_for_all_currently_detected_strings(self):
		#assert self.out_c.has_string_literal( ' truncated to %d characters\\n' )
		#assert self.out_c.has_string_literal( '%02x' )
		#assert self.out_c.has_string_literal( 'r' )
		assert self.out_c.has_string_literal( 'sed: ' )
		assert self.out_c.has_string_literal( 'sed: RE error, %o\\n' )
		#assert self.out_c.has_string_literal( 'sed: RE too long: %s\\n' )
		#assert self.out_c.has_string_literal( "sed: can't open %s\\n" )
		#assert self.out_c.has_string_literal( 'sed: cannot create %s\\n' )
		#assert self.out_c.has_string_literal( 'sed: duplicate label %s\\n' )
		#assert self.out_c.has_string_literal( 'sed: garbled command %s\\n' )
		#assert self.out_c.has_string_literal( 'sed: no addresses allowed for %s\\n' )
		#assert self.out_c.has_string_literal( 'sed: only one address allowed for %s\\n' )
		#assert self.out_c.has_string_literal( 'sed: too many commands, last was %s\\n' )
		#assert self.out_c.has_string_literal( 'sed: too many labels: %s\\n' )
		#assert self.out_c.has_string_literal( "sed: too many {'s\\n" )
		#assert self.out_c.has_string_literal( "sed: too many }'s\\n" )
		#assert self.out_c.has_string_literal( 'sed: undefined label %s\\n' )
		#assert self.out_c.has_string_literal( 'w' )

		#assert self.out_c.has_string_literal( 'sed: too much text: %s\\n' )

	# Currently detected functions which have their named (from symbols) counterparts in not-stripped binary.
	#
	def test_check_for_all_currently_detected_functions(self):
		assert self.out_c.has_func( '_init' )  # _init, TODO: z nejakeho dovodu tam chyba kus kodu
		assert self.out_c.has_func( 'function_8020' )  # __do_global_dtors_aux, TODO: v nestrip verzii detekocane ako staticky linkovane
		assert self.out_c.has_func( 'function_80b0' )  # frame_dummy
		assert self.out_c.has_func( 'entry_point' )  # _mainCRTStartup
		assert self.out_c.has_func( 'function_8214' )  # rhscomp = function_8218
		#assert self.out_c.has_func( 'function_82bc' )  # TODO: ???
		assert self.out_c.has_func( 'function_8354' )  #
		assert self.out_c.has_func( 'function_8458' )  # resolve
		assert self.out_c.has_func( 'function_8510' )  # recomp
		assert self.out_c.has_func( 'function_8a84' )  # compile
		assert self.out_c.has_func( 'function_8aa8' )  # search
		assert self.out_c.has_func( 'main' )  #
		#assert self.out_c.has_func( 'function_97a4' )  # readout
		assert self.out_c.has_func( 'function_9918' )  # my_getline
		assert self.out_c.has_func( 'function_9988' )  # dumpto
		assert self.out_c.has_func( 'function_9a74' )  # listto
		assert self.out_c.has_func( 'function_9f74' )  # place
		assert self.out_c.has_func( 'function_9fe4' )  # dosub
		assert self.out_c.has_func( 'function_a18c' )  # truncated
		assert self.out_c.has_func( 'function_a214' )  # advance
		assert self.out_c.has_func( 'function_a54c' )  # match
		assert self.out_c.has_func( 'function_a68c' )  # substitute
		assert self.out_c.has_func( 'function_a710' )  # command
		assert self.out_c.has_func( 'function_afb4' )  # selected
		assert self.out_c.has_func( 'function_b0ec' )  # execute
		#assert self.out_c.has_func( 'function_d334' )  # __malloc_unlock
		#assert self.out_c.has_func( 'function_11fe8' )  # __errno
		assert self.out_c.has_func( 'function_14824' )  # __do_global_ctors_aux

	# Functions reported in #1050 as not detected.
	# TODO: matula, uncomment when fixed.
	#
	def test_check_for_functions_not_detected_before_1050_fix(self):
		assert self.out_c.has_func( 'function_89b0' )  # address
		assert self.out_c.has_func( 'function_8af8' )  # cmdline
		assert self.out_c.has_func( 'function_8c88' )  # cmdcomp
