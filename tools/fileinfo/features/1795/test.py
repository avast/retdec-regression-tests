from regression_tests import *

class TestMachAr(Test):
    settings=TestSettings(
        tool='fileinfo',
        input='machoAr'
    )

    def test_error_message(self):
        assert "Error: File is a fat Mach-O binary with archives. Extract objects before using fileinfo." in self.fileinfo.output