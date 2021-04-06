from regression_tests import *


class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='4A574145A442A211181B84AD99C71AA42C6F4200FC2131A18C7E380FF5F7762B.dat'
    )

    def test_output_does_not_contain_subject(self):
        assert self.fileinfo.succeeded
        self.assertEqual(len(self.fileinfo.output['certificateTable']
                             ['signatures'][0]['allCertificates'][0]['attributes']['subject']), 0)
