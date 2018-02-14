from regression_tests import *

class Test(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='util2.obj'
	)

	def test_sections_loaded_correctly(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][2]['address'], '0x432e')
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][2]['size'], '0x280')
