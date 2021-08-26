from regression_tests import *


class Test1(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='8a8154c36977c3f47a65c329a6dd93c58b8aff6050a4a748f4c610310daf0d8b',
        args='--json --verbose'
    )

    def test_check_ignored_invalid_offsets(self):
        assert self.fileinfo.succeeded

        resourceTable = self.fileinfo.output['resourceTable']
        self.assertEqual(resourceTable['numberOfResources'], "1896")
        for idx, resource in enumerate(resourceTable['resources']):
            if idx < 970 or idx > 1892:
                assert 'offset' in resource
            else:
                assert 'offset' not in resource
