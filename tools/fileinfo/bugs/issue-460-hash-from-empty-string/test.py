from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='000b1f22029c979c27c7310712cae66b8ade37378023487277ad7c86d59a34f6',
        args='--verbose --json'
    )

    def test_for_all_needed_libs(self):
        assert self.fileinfo.succeeded

        imports = self.fileinfo.output['importTable'];
        assert 'crc32' not in imports
        assert 'md5' not in imports
        assert 'sha256' not in imports
