from regression_tests import *

class TestAdvancedInstaller(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=['5271aca29b7846bbdce71e830377406a629c9bc0e71d3514f971c33d1c23210d',
               'cd02e6062dd57491be5ae8fcbbccfbf620435cdc632f2004ee0e517fbd9d235c']
    )

    def test_detected_pyinstaller(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'Advanced Installer')
