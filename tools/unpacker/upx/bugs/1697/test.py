from regression_tests import *

class Test(Test):
	settings=TestSettings(
		tool='unpacker',
		input='97c21e0c8032fc118b9cb85e28b91394d9ab74de542e172019dc9ddcea874322',
		run_fileinfo=True
	)

	def test_unpacker_succeeded_no_imports(self):
		assert self.unpacker.succeeded
		assert self.fileinfo.succeeded
		assert "importTable" not in self.fileinfo.output
