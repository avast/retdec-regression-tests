from regression_tests import *

class Test(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='c2ee13fd028448d80ed59b445fd647e2'
	)

	def test_certificates_are_present(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output["certificateTable"]["numberOfCertificates"], "2")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "AA03C799E7AFAC2858B79ED9710A63191032CC4099CEC75653064B8FACBD09A1")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "A2BDF61928644D5A0F5CCC93C9B339E600AD1AD05E4682D86C1477CE39997CFF")
