from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json',
        input='broken'
    )

    def test_correct_error_handling(self):
        self.assertEqual(self.fileinfo.return_code, 6)
        self.assertEqual(
            self.fileinfo.output['errors'][0],
            "Failed to parse the input file (it is probably corrupted)."
            " Detected format is: Mach-O."
        )
