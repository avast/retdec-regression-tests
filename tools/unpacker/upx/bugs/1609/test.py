from regression_tests import *

class Test(Test):
	settings=TestSettings(
		tool='unpacker',
		input='locky.mem',
		run_fileinfo=True
	)

	def test_correct_sections(self):
		assert self.unpacker.succeeded
		self.assertEqual(self.fileinfo.output['sectionTable']['numberOfSections'], '5')
		self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['name'], '.text')
		self.assertEqual(self.fileinfo.output['sectionTable']['sections'][1]['name'], '.rdata')
		self.assertEqual(self.fileinfo.output['sectionTable']['sections'][2]['name'], '.data')
		self.assertEqual(self.fileinfo.output['sectionTable']['sections'][3]['name'], '.reloc')
		self.assertEqual(self.fileinfo.output['sectionTable']['sections'][4]['name'], 'gu_idata')
