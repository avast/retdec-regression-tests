from regression_tests import *

class Test(Test):
	settings = TestSettings(
		input='02024ca5cd7dde34189f8af770437c67',
		args='-k'
	)

	def test_check_for_all_currently_detected_strings(self):
		assert self.out_c.has_string_literal( 'Please crack Me :' )
		assert self.out_c.has_string_literal( '%s' )
		assert self.out_c.has_string_literal( '\\r\\n%s\\r\\n%s' )

	def test_check_for_functions(self):
		assert self.out_c.has_func( 'entry_point' )
		assert self.out_c.has_func( 'function_8048350' )
		assert self.out_c.has_func( 'function_80483b0' )
		assert self.out_c.has_func( 'function_8048436' )
		assert self.out_c.has_func( 'function_80488f0' )
		assert self.out_c.has_func( 'function_8048930' )
		assert self.out_c.has_func( 'function_8048940' )
		assert self.out_c.has_func( 'function_804899a' )
		assert self.out_c.has_func( 'function_80489a0' )
		assert self.out_c.has_func( 'function_80489d4' )  # _init_proc in IDA
		assert self.out_c.has_func( 'function_8048a04' )  # _term_proc in IDA

# TODO: tieto funkcie v IDA nie su
#
#function_8048a10
#function_80489e0
