from regression_tests import *

class Test1(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose --no-hashes',
        input='dotnet_gui.ex'
    )

    def test_no_hashes(self):
        assert 'crc32' not in self.fileinfo.output
        assert 'md5' not in self.fileinfo.output
        assert 'sha256' not in self.fileinfo.output
        assert 'crc32' not in self.fileinfo.output['importTable']
        assert 'md5' not in self.fileinfo.output['importTable']
        assert 'sha256' not in self.fileinfo.output['importTable']
        for resource in self.fileinfo.output['resourceTable']['resources']:
            assert 'crc32' not in resource
            assert 'md5' not in resource
            assert 'sha256' not in resource
        assert 'crc32' not in self.fileinfo.output['sectionTable']
        assert 'md5' not in self.fileinfo.output['sectionTable']
        assert 'sha256' not in self.fileinfo.output['sectionTable']
        for section in self.fileinfo.output['sectionTable']['sections']:
            assert 'crc32' not in section
            assert 'md5' not in section
            assert 'sha256' not in section

class Test2(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose --no-hashes=verbose',
        input='dotnet_gui.ex'
    )

    def test_only_file_hashes(self):
        assert 'crc32' in self.fileinfo.output
        assert 'md5' in self.fileinfo.output
        assert 'sha256' in self.fileinfo.output
        assert 'crc32' not in self.fileinfo.output['importTable']
        assert 'md5' not in self.fileinfo.output['importTable']
        assert 'sha256' not in self.fileinfo.output['importTable']
        for resource in self.fileinfo.output['resourceTable']['resources']:
            assert 'crc32' not in resource
            assert 'md5' not in resource
            assert 'sha256' not in resource
        assert 'crc32' not in self.fileinfo.output['sectionTable']
        assert 'md5' not in self.fileinfo.output['sectionTable']
        assert 'sha256' not in self.fileinfo.output['sectionTable']
        for section in self.fileinfo.output['sectionTable']['sections']:
            assert 'crc32' not in section
            assert 'md5' not in section
            assert 'sha256' not in section

class Test3(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose --no-hashes=file',
        input='dotnet_gui.ex'
    )

    def test_only_verbose_hashes(self):
        assert 'crc32' not in self.fileinfo.output
        assert 'md5' not in self.fileinfo.output
        assert 'sha256' not in self.fileinfo.output
        assert 'crc32' in self.fileinfo.output['importTable']
        assert 'md5' in self.fileinfo.output['importTable']
        assert 'sha256' in self.fileinfo.output['importTable']
        for resource in self.fileinfo.output['resourceTable']['resources']:
            assert 'crc32' in resource
            assert 'md5' in resource
            assert 'sha256' in resource
        assert 'crc32' in self.fileinfo.output['sectionTable']
        assert 'md5' in self.fileinfo.output['sectionTable']
        assert 'sha256' in self.fileinfo.output['sectionTable']
        for section in self.fileinfo.output['sectionTable']['sections']:
            assert 'crc32' in section
            assert 'md5' in section
            assert 'sha256' in section
