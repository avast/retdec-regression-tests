from regression_tests import *


class TestVerified(Test):
    settings = TestSettings(
        input=[
            'VSTST-FileConverter.ex',
            'c339b87d932b3f86c298b1745db1a28b1214fb7635ba3805851ef8699290f9b8',
            'f77acb4e1523b882f5307864345e5f7d20a657a7f40863bd7ae41d2521703fec',
            'crashreporter.ex',
            'PdfConv_32.dll'
        ],
        tool='fileinfo',
        args='--json --verbose'
    )

    def test_signature_verified(self):
        assert self.fileinfo.succeeded

        for sig in self.fileinfo.output["certificateTable"]['signatures']:
            assert len(sig['warnings']) == 0


class TestNotVerified(Test):
    settings = TestSettings(
        input=[
            '64f3ff5bd6b0d4e1a128a729368ca01c7b98620994f5e297b069af11947d8785',
            'a6aebb7c1368f571206c60729264a6feeae4a497b7326fcdb6ace519765727aa',
            '35a9a6a687b44806ad08ce085b24c343fa5e0d724ae91807bac54f5d75674553',
            '81772d6bcf399835641a5e7003039b0f5424788f2d92e015640cabec66baef82',
            '26040ce394dbc956d61665100d81c94d604b2fc877ca46025cdd15444ed23966',
            '2fe9b1cca77ccb680351f311b98ba5af23a6d290327938a8bc5866f3ae068aaa',
            '5fb7e6b789cd10145d7c9de012033a3c203f66a06f2d1d81723d30542abfdda3'
        ],
        tool='fileinfo',
        args='--json --verbose'
    )

    def test_signature_not_verified(self):
        assert self.fileinfo.succeeded
        for sig in self.fileinfo.output["certificateTable"]['signatures']:
            assert len(sig['warnings']) != 0
