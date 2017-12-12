from regression_tests import *

class Bug1456Test(Test):
	settings = TestSettings(
		tool='unpacker',
		input='ExportExcel.ex'
	)

	def test_overlay_copied_when_unpacked(self):
		assert self.unpacker.succeeded
		assert self.unpacker.output.contains('NRV2E')
		assert self.unpacker.output.contains('overlay with size of 0x19457')
