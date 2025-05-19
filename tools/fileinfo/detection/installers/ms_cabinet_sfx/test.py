from regression_tests import *

class TestMsCabinet(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=['ms_cabinet_1.dat',
               'ms_cabinet_2.dat',
               'ms_cabinet_3.dat']
    )

    def test_detected_ms_cabinet(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'Microsoft Cabinet SFX')
