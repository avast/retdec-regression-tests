from regression_tests import *

class PeRegularGccTest(Test):
	settings = TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='pe_regular_gcc'
	)

	def test_pe_regular_gcc(self):
		assert self.fileinfo.succeeded
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['baseAddress'], 16), 0x400000)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['numberOfSegments']), 14)

class PeNamelessSectionTest(Test):
	settings = TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='nameless_section'
	)

	def test_pe_nameless_section(self):
		assert self.fileinfo.succeeded
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['baseAddress'], 16), 0x400000)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['numberOfSegments']), 1)
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['name'], 'seg0000')

class PeTinyNoSectionTest(Test):
	settings = TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='tiny_no_sections'
	)

	def test_pe_tiny_no_sections(self):
		assert self.fileinfo.succeeded
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['baseAddress'], 16), 0x400000)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['numberOfSegments']), 1)
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['name'], 'seg0000')
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][0]['address'], 16), 0x400000)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][0]['size'], 16), 0x10c)

class PeTinyTest(Test):
	settings = TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input=['tiny_hello_world', 'tiny_file_size_bigger']
	)

	def test_pe_tiny_no_sections(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output['loaderInfo']['baseAddress'], '0x400000')
		self.assertEqual(self.fileinfo.output['loaderInfo']['numberOfSegments'], '3')
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['index'], '0')
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['name'], '.text')
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['address'], '0x401000')
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['size'], '0x2f')
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['index'], '1')
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['name'], '.data')
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['address'], '0x402000')
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['size'], '0x16')
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][2]['index'], '2')
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][2]['name'], '.idata')
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][2]['address'], '0x403000')
		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][2]['size'], '0x82')
