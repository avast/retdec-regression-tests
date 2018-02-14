from regression_tests import *

class IltWithInvalidAddress1Test(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='33f2fa32b29e8fecff9b92da47d8b154a44d3fe3d6c96ca4ac50c7cc6627b064_ctblocker'
	)

	def test_iat_without_null_terminator(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '180')

class IltWithInvalidAddress2Test(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='4ae64579fa0efd0be978c6797efe05d31517985b28ebd95dcadfacf3bb551f56.ex_cryptowall-v4'
	)

	def test_delayed_imports_with_high_rva(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '247')
