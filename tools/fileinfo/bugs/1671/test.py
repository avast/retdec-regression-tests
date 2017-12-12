from regression_tests import *

class Test(Test):
	settings = TestSettings(
		tool='fileinfo',
		input='x86-pe-036ff6f43fac0491dd827c4fb508cd4b',
		args='--json'
	)

	def test_fileinfo_succeeded(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
