from regression_tests import *

class Test(Test):
	settings=TestSettings(
		tool='unpacker',
		input='1064CBD546A4E9D8D760EBF52465DE9EB12573DACC165A66A48C826824FE2CF3.dat'
	)

	def test_unpacker_succeeded(self):
		assert self.unpacker.succeeded
		assert self.unpacker.output.contains('Detected LZMA unpacking stub based on signature & metadata.')
		assert self.unpacker.output.contains('Unpacked data based on UPX metadata.')
