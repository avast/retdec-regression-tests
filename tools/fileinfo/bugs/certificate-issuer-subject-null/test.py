from regression_tests import *


class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='808f3264d9810942473173cd1210fc3a'
    )

    def test_common_name_is_set(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["certificateTable"]["signatures"][0]['allCertificates']
                         [0]["attributes"]["subject"]["commonName"], R"\x00@\x00B\x00y\x00E\x00L\x00D\x00I")
