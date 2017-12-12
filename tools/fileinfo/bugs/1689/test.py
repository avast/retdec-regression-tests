from regression_tests import *

class Test(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input=[
			'79125fb768db2f1d7a7fce44cca30bca',
			'9dae44cc54e89a322e2a0178b631b385'
		]
	)

	def test_success(self):
		assert self.fileinfo.succeeded
