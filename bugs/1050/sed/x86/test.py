from regression_tests import *

class Test(Test):
	settings = TestSettings(
		input='sed-strip',
		args='-k'
	)

	def test_check_for_all_currently_detected_strings(self):
		assert self.out_c.has_string_literal( ' truncated to %d characters\\n' )
		assert self.out_c.has_string_literal( '%02x' )
		assert self.out_c.has_string_literal( '%ld\\n' )
		assert self.out_c.has_string_literal( '%s\\n' )
		assert self.out_c.has_string_literal( 'line %D' )
		assert self.out_c.has_string_literal( 'r' )
		assert self.out_c.has_string_literal( 'sed: ' )
		assert self.out_c.has_string_literal( 'sed: RE error, %o\\n' )
		assert self.out_c.has_string_literal( 'sed: RE too long: %s\\n' )
		assert self.out_c.has_string_literal( "sed: can't open %s\\n" )
		assert self.out_c.has_string_literal( 'sed: cannot create %s\\n' )
		assert self.out_c.has_string_literal( 'sed: duplicate label %s\\n' )
		assert self.out_c.has_string_literal( 'sed: garbled command %s\\n' )
		assert self.out_c.has_string_literal( 'sed: line too long\\n' )
		assert self.out_c.has_string_literal( 'sed: no addresses allowed for %s\\n' )
		assert self.out_c.has_string_literal( 'sed: only one address allowed for %s\\n' )
		assert self.out_c.has_string_literal( 'sed: too many appends after line %ld\\n' )
		#assert self.out_c.has_string_literal( 'sed: too many commands, last was %s\\n' )
		assert self.out_c.has_string_literal( 'sed: too many labels: %s\\n' )
		assert self.out_c.has_string_literal( 'sed: too many reads after line %ld\\n' )
		assert self.out_c.has_string_literal( "sed: too many {'s\\n" )
		assert self.out_c.has_string_literal( "sed: too many }'s\\n" )
		assert self.out_c.has_string_literal( 'sed: too much text: %s\\n' )
		assert self.out_c.has_string_literal( 'sed: undefined label %s\\n' )
		assert self.out_c.has_string_literal( 'sed: unknown flag %c\\n' )
		#assert self.out_c.has_string_literal( 'w' )

		#assert self.out_c.has_string_literal('hold space')
		#assert self.out_c.has_string_literal('sed: cannot open command-file %s\\n')

	# Currently detected functions which have their named (from symbols) counterparts in not-stripped binary.
	#
	def test_check_for_all_currently_detected_functions(self):
		assert self.out_c.has_func( 'function_8048638' )  # _init
		assert self.out_c.has_func( 'entry_point' )  # _start
		assert self.out_c.has_func( 'function_80487a0' )  # __x86_get_pc_thunk_bx
		assert self.out_c.has_func( 'function_80487b0' )  # deregister_tm_clones
		assert self.out_c.has_func( 'function_80487e0' )  # register_tm_clones
		assert self.out_c.has_func( 'function_8048880' )  # frame_dummy
		assert self.out_c.has_func( 'function_80488b0' )  # rhscomp
		assert self.out_c.has_func( 'function_804892c' )  # recomp
		assert self.out_c.has_func( 'function_8048ef3' )  # compile
		assert self.out_c.has_func( 'advance' )  # advance
		assert self.out_c.has_func( 'function_8049cf6' )  # match
		assert self.out_c.has_func( 'function_8049de6' )  # selected
		assert self.out_c.has_func( 'function_8049ec1' )  # place
		assert self.out_c.has_func( 'function_8049f18' )  # dosub
		assert self.out_c.has_func( 'function_804a052' )  # substitute
		assert self.out_c.has_func( 'function_804a0dc' )  # listto
		assert self.out_c.has_func( 'function_804a1cf' )  # dumpto
		assert self.out_c.has_func( 'function_804a234' )  # truncated
		assert self.out_c.has_func( 'function_804a2b4' )  # my_getline
		assert self.out_c.has_func( 'function_804a2fb' )  # readout
		assert self.out_c.has_func( 'function_804a391' )  # command
		assert self.out_c.has_func( 'function_804a913' )  # execute
		assert self.out_c.has_func( 'function_804aad0' )  # __do_global_ctors_aux

	# Functions reported in #1050 as not detected.
	# TODO: matula, uncomment when fixed.
	#
	def test_check_for_functions_not_detected_before_1050_fix(self):
		assert self.out_c.has_func( 'function_8048d59' )  # cmdline
		assert self.out_c.has_func( 'function_8048e50' )  # address

		## Range not decoded.
		##
		assert self.out_c.has_func( 'function_8048f88' )  # search
		assert self.out_c.has_func( 'function_8048fce' )  # resolve
		assert self.out_c.has_func( 'function_804904d' )  # main
		assert self.out_c.has_func( 'function_8049279' )  # ycomp
		assert self.out_c.has_func( 'function_8049373' )  # cmdcomp

		## Not detected functions in decoded ranges.
		##
		assert self.out_c.has_func( 'function_804aa50' )  # __libc_csu_init
		#assert self.out_c.has_func( 'function_804aac0' )  # __libc_csu_fini
		assert self.out_c.has_func( 'function_804aafc' )  # _fini

	# Functions detected in stripped binary, that do not have their named (from symbols) counterparts in not-stripped binary.
	# TODO: matula, not sure how serious is this problem. if possible fix detection and uncomment this check.
	#
	def test_check_for_falsely_detected_functions_before_1050_fix(self):
		assert not self.out_c.has_func( 'function_80487db' )
		assert not self.out_c.has_func( 'function_8048818' )
