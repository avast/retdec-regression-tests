from regression_tests import *

class Test(Test):
	settings=TestSettings(
		input=[
			'x86-pe-38ffdd8526b8410583219f3cf298c13b',
			'x86-pe-43f2453fee2432955b2953088814f341'
		]
	)

	def test_decompiles_successfully(self):
		assert self.decompiler.succeeded
