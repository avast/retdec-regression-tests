from regression_tests import *

class OverlappedSegmentsTest(Test):
	settings = TestSettings(
		tool='fileinfo',
		args='-j -v',
		input='mips-elf-5fd5006a68f470706ac9289ea1664422'
	)

	def test_overlapped_segments(self):
		assert self.fileinfo.succeeded
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['baseAddress'], 16), 0x3f3fb4)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['numberOfSegments']), 1)

		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['name'], 'seg0001')
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][0]['address'], 16), 0x3f3fb4)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][0]['size'], 16), 0x1e0432c)
