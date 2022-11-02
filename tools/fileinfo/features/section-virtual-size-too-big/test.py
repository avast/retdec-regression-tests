from regression_tests import *

# https://github.com/avast/retdec/issues/415
# Test for proper anomaly scanning
class Test1(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=[
            '83e9cb2a6e78c742e1090292acf3c78baf76e82950d96548673795a1901db061',
            'a882bc57d078511c0fb15ea956d5655a626b508c91c4dc6d7a3ba467fc396b71',
        ],
        args='--verbose --json'
    )

    def test_loader_survives(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 30)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_INVALID_SECTION_VSIZE')
        self.assertEqual(self.fileinfo.output["loaderError"]["loadable_anyway"], 'false')
