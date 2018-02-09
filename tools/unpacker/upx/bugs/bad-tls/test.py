from regression_tests import *

class Bug1412Test(Test):
	settings = TestSettings(
		tool='unpacker',
		input='InjectPACKED.ex'
	)

	def test_tls_correctly_unpacked(self):
		assert self.unpacker.succeeded
		assert self.unpacker.output.contains('NRV2E')
		assert self.unpacker.output.contains('Original TLS directory found at RVA 0x152000 with size 0x18')
