from regression_tests import *

class TestCcg(Test):
    settings=TestSettings(
        input='9e1a2139135145dcde4d62abe2d6956a3e0cdba6001ece8d80b915c4811bf915',
        tool='fileinfo',
        args='--json'
    )

    def test_heuristic_works(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['tools'][1]['heuristics'], True)
        self.assertEqual(self.fileinfo.output['tools'][1]['name'], 'CCG packer')

class TestGentee(Test):
    settings=TestSettings(
        input='b801907ad9452a1bb5f849729fda6b16fd186ef271d5dd5d4f580d62feca2502',
        tool='fileinfo',
        args='--json'
    )

    def test_heuristic_works(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['tools'][0]['heuristics'], True)
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'Gentee')

class TestKkrunchy(Test):
    settings=TestSettings(
        input='1d4a9f15704e980f9f073e22eda71411e921b4897c653b39533a5fae7182e848',
        tool='fileinfo',
        args='--json'
    )

    def test_heuristic_works(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['tools'][0]['heuristics'], True)
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'kkrunchy')

class TestProcrypt(Test):
    settings=TestSettings(
        input='39f47d15730e9189a3f1982778dfb30d9efc1eefabe608a8df01066a23e912f1',
        tool='fileinfo',
        args='--json'
    )

    def test_heuristic_works(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['tools'][0]['heuristics'], True)
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'ProCrypt')

class TestTSULoader(Test):
    settings=TestSettings(
        input='4cb6f3563107054610512dfedb951930d2bc799d478e51727fa9d77fe70415d1',
        tool='fileinfo',
        args='--json'
    )

    def test_heuristic_works(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['tools'][1]['heuristics'], True)
        self.assertEqual(self.fileinfo.output['tools'][1]['name'], 'TSULoader')

class TestWinZipLoader(Test):
    settings=TestSettings(
        input='8caf3f512894c65da63f10eaeb8e2fa8858d0a67ffc8e940266a4ec6f676ea60',
        tool='fileinfo',
        args='--json'
    )

    def test_heuristic_works(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['tools'][0]['heuristics'], True)
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'WinZip SFX')
