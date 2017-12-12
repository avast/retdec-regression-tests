
from regression_tests import *

class Test(Test):
	settings = TestSettings(
		input='x86-c96c707952ce5bf3334f97c3e76afba6'
	)

	def test_my_printf_calls_known_functions(self):
		pass
		# TODO Currently, decfront generates my_printf(), but it is not
		#      reachable from main(), so it is removed and the test fails. See
		#      #1066 for more details.
		# self.out_c.has_funcs('my_printf')
		# fnc = self.out_c.funcs['my_printf']
		# assert fnc.calls('write')
		# assert fnc.calls('strlen')
		# assert fnc.calls('strchr')
		# assert fnc.calls('memcpy')
		# assert fnc.calls('memset')
