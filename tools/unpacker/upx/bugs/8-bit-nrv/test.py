from regression_tests import *

class Test(Test):
	settings=TestSettings(
		tool='unpacker',
		input='arm-pe-1d777f7539e78c45f4cb55b245cbf09d',
		run_fileinfo=True
	)

	def test_unpacked_successfully(self):
		assert self.unpacker.succeeded
		self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['name'], '.text')
