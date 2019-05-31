from regression_tests import *

class Test1(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json',
        input='f56049df7e33162724c3f22a034b43be'
    )

    def test_entry_point_bytes_has_default_length(self):
        self.assertEqual(self.fileinfo.output['entryPoint']['bytes'], '558bec51c745fc01000000837d0c007510833d703c031000750733c0e9cc000000837d0c017406837d0c027542833dfc5703')

class Test2(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --ep-bytes=10',
        input='f56049df7e33162724c3f22a034b43be'
    )

    def test_entry_point_bytes_has_length_of_10(self):
        self.assertEqual(self.fileinfo.output['entryPoint']['bytes'], '558bec51c745fc010000')
