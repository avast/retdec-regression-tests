from regression_tests import *

class Test(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json',
		input='942699e2b6debfacec7ac278b947ce86'
	)

	def test_compiler_is_gcc_go(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'gc')
		self.assertEqual(self.fileinfo.output['languages'][0]['name'], 'Go')
