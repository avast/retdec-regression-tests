from regression_tests import *

class CoffTest(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='sehsupp.obj'
	)

	def test_coff(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output['loaderInfo']['baseAddress'], '0')
		self.assertEqual(self.fileinfo.output['loaderInfo']['numberOfSegments'], '7')
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['address'], '0')
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['address'], '0x23b')
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][2]['address'], '0x27d')
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][3]['address'], '0x381')
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][4]['address'], '0x38d')
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][5]['address'], '0x391')
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][6]['address'], '0x3a1')


class CoffWithBssTest(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='debug.obj'
	)

	def test_coff_with_bss(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output['loaderInfo']['baseAddress'], '0')
		self.assertEqual(self.fileinfo.output['loaderInfo']['numberOfSegments'], '19')
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][15]['address'], '0x14bc')
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][16]['address'], '0x14c4')
