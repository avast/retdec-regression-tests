from regression_tests import *


class Test1(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='097a0f8b8c3f2b90f5360f27da5ef8e5a7406c6f211c8d3e56a1671933508bc1',
        args='--json --verbose'
    )

    def test_ignore_junk_resource_type_name(self):
        assert self.fileinfo.succeeded

        # Type name strings are absurdly long indicating random junk RVA and thus ignored
        resourceTable = self.fileinfo.output['resourceTable']
        assert resourceTable['numberOfResources'] == '17'

        assert resourceTable['resources'][0]['index'] == '0'
        assert resourceTable['resources'][0]['nameId'] == '105'
        assert 'type' not in resourceTable['resources'][0]
        assert resourceTable['resources'][0]['language'] == 'English'
        assert resourceTable['resources'][0]['languageId'] == '9'
        assert resourceTable['resources'][0]['sublanguageId'] == '1'
        assert resourceTable['resources'][0]['offset'] == '0x2abb8'
        assert resourceTable['resources'][0]['size'] == '0xba00'
        assert resourceTable['resources'][0]['crc32'] == '68ffcc23'
        assert resourceTable['resources'][0]['md5'] == 'df481717dd02990dbea545d80cd2c090'
        assert resourceTable['resources'][0]['sha256'] == 'a4b82e3e2250d7838d45e5110d964fa89aebd81e9eae2a1c34418a0e78f6d991'

        assert resourceTable['resources'][1]['index'] == '1'
        assert resourceTable['resources'][1]['nameId'] == '164'
        assert 'type' not in resourceTable['resources'][0]
        assert resourceTable['resources'][1]['language'] == 'English'
        assert resourceTable['resources'][1]['languageId'] == '9'
        assert resourceTable['resources'][1]['sublanguageId'] == '1'
        assert resourceTable['resources'][1]['offset'] == '0x365b8'
        assert resourceTable['resources'][1]['size'] == '0x9edb'


class Test2(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='7004f68f9142737b2d6c144df6b6d165c5db518e4f06a9fb1a93d1ff129cefa3',
        args='--json --verbose'
    )

    def test_ignore_junk_resource_type_name(self):
        assert self.fileinfo.succeeded

        # Type name strings are absurdly long indicating random junk RVA and thus ignored
        resourceTable = self.fileinfo.output['resourceTable']
        assert resourceTable['numberOfResources'] == '64'

        assert resourceTable['resources'][0]['index'] == '0'
        assert resourceTable['resources'][0]['nameId'] == '1'
        assert 'type' not in resourceTable['resources'][0]
        assert resourceTable['resources'][0]['language'] == 'English'
        assert resourceTable['resources'][0]['languageId'] == '9'
        assert resourceTable['resources'][0]['sublanguageId'] == '1'
        assert resourceTable['resources'][0]['offset'] == '0xffffffffffffff60'
        assert resourceTable['resources'][0]['size'] == '0x80800080'
