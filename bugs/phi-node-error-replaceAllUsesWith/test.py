from regression_tests import *

class TestSignedMod1IdiomARM(Test):
	settings = TestSettings(
		input='arm-elf-09923a6e40662aab0ad2a1096f802f08'
	)

	def test_check_for_detected_function_and_signedMod1_idiom(self):
		assert self.out_c.has_func( 'LzmaProps_Decode' )
		# check presence of '% 9' expression without any addition
		#assert self.out_c.contains(r'\(\S+ % 9\) % 256')

class TestSignedMod1IdiomPOWERPCClang(Test):
	settings = TestSettings(
		input='powerpc-elf-ackermann-clang'
	)

	def test_check_for_detected_function_and_signedMod1_idiom(self):
		assert self.out_c.has_func( 'naive_ackermann' )
		assert self.out_c.has_func( 'iterative_ackermann' )
		assert self.out_c.has_func( 'formula_ackermann' )
		assert self.out_c.has_func( 'main' )
		# check presence of '% x + 1' idioms
		assert self.out_c.contains(r'm % 4 \+ 1;')
		assert self.out_c.contains(r'n % 3 \+ 1;')

class TestSignedMod1IdiomPOWERPCGCC(Test):
	settings = TestSettings(
		input='powerpc-elf-ackermann-gcc'
	)

	def test_check_for_detected_function_and_signedMod1_idiom(self):
		assert self.out_c.has_func( 'naive_ackermann' )
		assert self.out_c.has_func( 'iterative_ackermann' )
		assert self.out_c.has_func( 'formula_ackermann' )
		assert self.out_c.has_func( 'main' )
		# check presence of '% x + 1' idioms
		assert self.out_c.contains(r'm % 4 \+ 1;')
		assert self.out_c.contains(r'n % 3 \+ 1;')

class TestSignedMod1IdiomThumbClang(Test):
	settings = TestSettings(
		input='thumb-elf-ackermann-clang'
	)

	def test_check_for_detected_function_and_signedMod1_idiom(self):
		assert self.out_c.has_func( 'naive_ackermann' )
		assert self.out_c.has_func( 'iterative_ackermann' )
		assert self.out_c.has_func( 'formula_ackermann' )
		assert self.out_c.has_func( 'main' )
		# check presence of '% x + 1' idioms
		assert self.out_c.contains(r'm % 4 \+ 1;')
		#assert self.out_c.contains(r'n % 3 \+ 1;')

class TestSignedMod1IdiomThumbGCC(Test):
	settings = TestSettings(
		input='thumb-elf-ackermann-gcc'
	)

	def test_check_for_detected_function_and_signedMod1_idiom(self):
		assert self.out_c.has_func( 'naive_ackermann' )
		assert self.out_c.has_func( 'iterative_ackermann' )
		assert self.out_c.has_func( 'formula_ackermann' )
		assert self.out_c.has_func( 'main' )
		# check presence of '% x + 1' idioms
		assert self.out_c.contains(r'm % 4 \+ 1;')
		assert self.out_c.contains(r'n % 3 \+ 1;')
