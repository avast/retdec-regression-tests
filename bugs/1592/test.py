from regression_tests import *

class ImportAndExportSameAddressTest(Test):
	settings=TestSettings(
		input='exports_doc.ex'
	)

	def test_all_function_calls(self):
		assert self.out_c.has_funcs('EntryPoint')
		assert self.out_c.funcs['EntryPoint'].calls('printf', 'ExitProcess')
		#assert self.out_c.has_string_literal(r' * PE with exports as internal documentation\n')
