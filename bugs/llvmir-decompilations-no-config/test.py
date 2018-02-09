
from regression_tests import *

class TestNoConfig(Test):
	settings = TestSettings(
		input='00A2.ll',
		args='--no-config'
	)

	def test_check_for_single_function(self):
		assert self.out_c.has_just_funcs( 'function_8048960' )

class TestConfigWithBadInputFile(Test):
	settings = TestSettings(
		input='00A2.ll',
		config='00A2.json',
	)

	def test_check_for_single_function(self):
		assert self.out_c.has_just_funcs( 'function_8048960' )
