from regression_tests import *


class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='JustRichHeader.ex'
    )

    def test_rich_header_raw_bytes_are_presented(self):
        self.assertEqual(self.fileinfo.output['richHeader']['rawBytes'], (
            'DanS\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x09x\\x93\\x00\\x0a\\x00\\x00\\x00\\x13f'
            '\\x01\\x01\\x03\\x00\\x00\\x00\\x13f\\x03\\x01\\x01\\x00\\x00\\x00\\x13f\\x05\\x01\\x12\\x00\\x00\\x00\\x13f'
            '\\x04\\x01\\x0c\\x00\\x00\\x00od\\x01\\x01\\x02\\x00\\x00\\x00\\x00\\x00\\x01\\x00+\\x00\\x00\\x00<g\\x09\\x01'
            '\\x02\\x00\\x00\\x00<g\\xff\\x00\\x01\\x00\\x00\\x00<g\\x02\\x01\\x01\\x00\\x00\\x00'
        ))
