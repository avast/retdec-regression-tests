from regression_tests import *

class Test(Test):
	"""Checks that fileinfo does not segfault in dwarfparserl."""

	settings=TestSettings(
		tool='fileinfo',
		input='33B6CCAB3504A2B6EF213ACBFE69B0C6EF225DFAFE5002A72D5C9687BE08097D.dat'
	)

	def test_fileinfo_succeeded(self):
		assert self.fileinfo.succeeded
