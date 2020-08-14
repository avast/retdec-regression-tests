from regression_tests import *

class TestValidPEWithoutCrash(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='x86-pe-036ff6f43fac0491dd827c4fb508cd4b',
        args='--json'
    )

    def test_fileinfo_succeeded(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')

class TestCorruptedPEWithoutCrash(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            # https://github.com/avast/retdec/issues/838
            '447360831D2F44DA6CB38D49812DA0921F18C37052FBBA424DE19290563250F8',
        ],
        args='--json'
    )

    def test_corrupted_pe(self):
        assert 'errors' in self.fileinfo.output
