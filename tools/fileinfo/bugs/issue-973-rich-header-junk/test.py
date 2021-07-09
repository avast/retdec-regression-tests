from regression_tests import *


class Test1(Test):
    # Tests case where there is junk data between DOS header/stub and Rich header
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='2acd2ff9c70ba9398221cf2265b2fddaceae3e31a29883594bcce545f02be6a3'
    )

    def test_correctly_ignore_junk_data(self):
        assert self.fileinfo.succeeded

        richHeader = self.fileinfo.output['richHeader']
        assert richHeader['offset'] == "0x37800"
        assert richHeader['key'] == "0x89de3436"
        assert richHeader['signature'] == "000c1c7b00000003000000000000001400131f62" \
            "0000000f00010000000001ac000e1c830000001d000a" \
            "263600000092000606c700000001000b263600000067"
        assert richHeader['sha256'] == "55c6385307557217e657085ba194" \
            "17f1c333e59fb57e9b79bade22b6792b19db"
        assert richHeader['crc32'] == "fd8a1133"
        assert richHeader['md5'] == "ac68f848eb80cdaabf9ae94c6e58deb4"
        assert richHeader['numberOfRecords'] == "8"
        assert len(richHeader['richHeaderRecords']) == 8


class Test2(Test):
    # Tests case where there is junk data between DOS header/stub and Rich header
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='7f29a26f830eee42a80a1a35169d9f616ca9823e386316f5eccfe36f90a8fe4b'
    )

    def test_correctly_ignore_junk_data(self):
        assert self.fileinfo.succeeded

        richHeader = self.fileinfo.output['richHeader']
        assert richHeader['offset'] == "0x34288"
        assert richHeader['key'] == "0xef888e60"
        assert richHeader['sha256'] == "c78049b5ffbb9c443f2652e2bff4ab547dc6b64955e86e8e0fb09c2839409b3a"
        assert richHeader['numberOfRecords'] == "15"
