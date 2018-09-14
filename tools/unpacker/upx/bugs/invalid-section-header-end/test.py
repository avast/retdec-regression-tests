from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='unpacker',
        input=[
            'd4740876fbe6d9af432ef04eaed7d262',
            'ef506d1488f7c18e9f369d945f268d2d'
        ]
    )

    def test_unpacker_fails(self):
        self.assertEqual(self.unpacker.return_code, 2)
        assert self.unpacker.output.contains('Original header contains corrupted data.')
