from regression_tests import *


class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=[
            'A71BD8DF3C08B676D26F1F898F2F89D5EF7D25F80158B2D896AEF90DE3029EEF',
            '7FF922215186F4B33AD7733CC59C9F39CDC1F6D5A5F5CB31B779CFFE2F3590E0',
            'A21A3FC4BDDD48948258743A91E614F1173CFF68ED144CA71310645502A0DDE0'
        ]
    )

    def test_signature_verified(self):
        assert self.fileinfo.succeeded
        self.assertEqual(
            len(self.fileinfo.output['certificateTable']['signatures'][0]['warnings']), 0)
