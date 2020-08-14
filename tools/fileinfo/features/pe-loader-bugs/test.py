from regression_tests import *

class TestNoCrash(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '447360831D2F44DA6CB38D49812DA0921F18C37052FBBA424DE19290563250F8',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert 'errors' in self.fileinfo.output
