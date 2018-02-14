from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input='IntelliJIDEALicenseServer_openbsd_386',
        tool='unpacker',
        run_fileinfo=True
    )

    def test_unpacking_successful(self):
        assert self.unpacker.succeeded
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['sectionTable']['numberOfSections'], '13')
