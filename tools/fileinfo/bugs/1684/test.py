from regression_tests import *

class Test(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='76eb97b8f62dff2a621c946c565222ae'
	)

	def test_symbol_tables_not_in_output(self):
		assert self.fileinfo.succeeded
		assert "symbolTables" not in self.fileinfo.output
