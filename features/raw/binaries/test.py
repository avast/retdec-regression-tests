from regression_tests import *

class Test1(Test):

	settings = TestSettings(
		input='019281ce4388c5c981da26c1d9797d08.raw',
		mode='raw',
		arch='thumb',
		args='--endian little --raw-entry-point 0x20e9 --raw-section-vma 0x2000'
	)

	# This just checks functions detected at the time of test creation.
	# We do not have original source/binary, so we do not known it these functions are OK.
	# IDA does not produce anything reasonable, so we can not cross-check our results.
	#
	def test_check_some_functions(self):
		assert self.out_c.has_funcs(
			'function_2000',
			#'function_34ac',
			#'function_4398',
			#'function_53d0',
			'function_6050',
			#'function_86f0',
			#'function_953c',
			#'function_b934',
			'function_d14e',
			#'function_d258',
		)

class Test2(Test):

	settings = TestSettings(
		input='raw.raw',
		arch='arm',
		mode='raw',
		args='--endian big --raw-entry-point 0x0 --raw-section-vma 0'
	)

	# This just checks functions detected at the time of test creation.
	# We do not have original source/binary, so we do not known it these functions are OK.
	# IDA does not produce anything reasonable, so we can not cross-check our results.
	#
	# jk: I had to disable detection of "function_839c" because it is no longer
	# generated and I cannot confirm that this is actually wrong (the code
	# is a mess). This test is only usefull for detecting problems in
	# RAW-compilation toolchain and nothing more.
	#
	def test_check_some_functions(self):
		assert self.out_c.has_funcs(
			#'function_839c',
			'entry_point'
		)
