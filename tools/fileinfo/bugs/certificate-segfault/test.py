from regression_tests import *

class Test1(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='c1ae78a9681fd2c6dac9501258ee8f69'
	)

	def test_certificate_table_present(self):
		assert self.fileinfo.succeeded
		assert 'signerCertificateIndex' not in self.fileinfo.output['certificateTable']
		self.assertEqual(self.fileinfo.output['certificateTable']['numberOfCertificates'], '2')
		self.assertEqual(self.fileinfo.output['certificateTable']['certificates'][0]['sha256'], '8815DFF787F21FA8106760CB89C5B4493F4BD45E2CE801D2A4FE1F61DEE0C039')
		self.assertEqual(self.fileinfo.output['certificateTable']['certificates'][1]['sha256'], '1C1983300C10FB262C0B2304B7BE15AABA10AE356EBBBB177583DC44774EB080')


class Test2(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='d4744d78e0b4c1f50bc081eff41b69d6'
	)

	def test_certificate_table_present(self):
		assert self.fileinfo.succeeded
		assert 'signerCertificateIndex' not in self.fileinfo.output['certificateTable']
		self.assertEqual(self.fileinfo.output['certificateTable']['numberOfCertificates'], '1')
		self.assertEqual(self.fileinfo.output['certificateTable']['certificates'][0]['sha256'], 'CED5AB020125966499A067ABFB138434281BC5B00C90D5D74D31529FF5169BF2')
