from regression_tests import *

class TestNoEntryPoint(Test):
	settings=TestSettings(
		tool='unpacker',
		input='c544ff15f206b1a6864cfd865c909dc4'
	)

	def test_no_entry_point(self):
		self.assertEqual(self.unpacker.return_code, 2)
		assert self.unpacker.output.contains('No entry point segment found.')

class TestInvalidImportHints(Test):
	settings=TestSettings(
		tool='unpacker',
		input='ea4fee3ab95e4257651b632425f09198'
	)

	def test_invalid_import_hints(self):
		self.assertEqual(self.unpacker.return_code, 2)
		assert self.unpacker.output.contains('Invalid import hints detected.')
