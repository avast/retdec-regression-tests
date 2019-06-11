from regression_tests import *

class Test000(Test):
    settings=TestSettings(
        tool='fileinfo',
        timeout=10,
        input=[
            '000-correct-file-32bit.ex_',
            '000-correct-file-64bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_missing_deps(self):
        assert self.fileinfo.succeeded
        assert 'loaderError' not in self.fileinfo.output, 'unexpectedly found loader error'


class Test001(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '001-missing-deps-32bit.ex_',
            '001-missing-deps-64bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_missing_deps(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 42)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_MISSING_DEPENDENCY')
        self.assertEqual(self.fileinfo.output["missingDeps"]["count"], 2)
        self.assertEqual(self.fileinfo.output["missingDeps"]["items"][0]["name"], "ADVAPY32.dll")
        self.assertEqual(self.fileinfo.output["missingDeps"]["items"][1]["name"], "KERNUL32.dll")
