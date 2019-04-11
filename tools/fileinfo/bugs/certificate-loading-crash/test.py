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
        self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "aa03c799e7afac2858b79ed9710a63191032cc4099cec75653064b8facbd09a1")
        self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "a2bdf61928644d5a0f5ccc93c9b339e600ad1ad05e4682d86c1477ce39997cff")
