from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=[
            'COD4-Advantage-Tool',
            'The-Advantage-Tool'
        ]
    )

    def test_segments_are_loaded(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['name'], '__TEXT')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['name'], '__DATA')
