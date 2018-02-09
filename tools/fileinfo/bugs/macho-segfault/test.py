from regression_tests import *

class Test0(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='cc4a24a56a545db9f5741e7372247386'
	)

	def test_symbol_table(self):
		assert self.fileinfo.succeeded
		self.assertEqual(len(self.fileinfo.output['symbolTables']), 1)
		self.assertEqual(len(self.fileinfo.output['symbolTables'][0]['symbols']), 1200)


class Test1(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='1c312adb9719098ebb1a5f4bcfc92820'
	)

	def test_symbol_table(self):
		assert self.fileinfo.succeeded
		self.assertEqual(len(self.fileinfo.output['symbolTables']), 1)
		self.assertEqual(len(self.fileinfo.output['symbolTables'][0]['symbols']), 2643)


class Test2(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='1dd619ef0cb56e2796d0fe57b85ee594'
	)

	def test_symbol_table(self):
		assert self.fileinfo.succeeded
		self.assertEqual(len(self.fileinfo.output['symbolTables']), 1)
		self.assertEqual(len(self.fileinfo.output['symbolTables'][0]['symbols']), 2654)


class Test3(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input=[
		    '885509c871133647cf2d4e846dfd7943',
		    'c8e599ab3db2fc71395f4a779b210fdb'
		]
	)

	def test_symbol_table(self):
		assert self.fileinfo.succeeded
		self.assertEqual(len(self.fileinfo.output['symbolTables']), 1)
		self.assertEqual(len(self.fileinfo.output['symbolTables'][0]['symbols']), 2582)
