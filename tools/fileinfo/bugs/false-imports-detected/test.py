from regression_tests import *

class IatWithoutNullTerminatorTest(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='1203acaa8d611be94e080293bbe31231'
	)

	def test_iat_without_null_terminator(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '68')

class DelayedImportsWithHighRvaTest(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='bf1ef4df4e7f59e708d767391830a63756b081986adb3f54cd8c6cb5cbd1d036_vonteera'
	)

	def test_delayed_imports_with_high_rva(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '635')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][598]['index'], '598')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][598]['name'], 'GetLogicalProcessorInformation')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][598]['libraryName'], 'kernel32.dll')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][598]['address'], '0x804c38')
