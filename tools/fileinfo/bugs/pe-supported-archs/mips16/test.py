from regression_tests import *

class Test(Test):
    settings_1 = TestSettings(
        tool='fileinfo',
        input=['13948eeb174146139516ccbb1b819b059186113d7b0ded59d32821622e486cde', '172674f2e23fd6ed01eb8f5d3cbfb8e4ced52ca70d4e6b4fa836e6038a463fa1', 'd151faccca8c47628635777f99853c8d50337e44015296a2009095be91af20b6']
    )

    def test_check_fileinfo_output(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains('PE')
        assert self.fileinfo.output.contains('MIPS')
        assert self.fileinfo.output.contains('Little endian')
