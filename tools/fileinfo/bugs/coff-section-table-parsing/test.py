from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='Driver.o'
    )

    def test_sections(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["sectionTable"]["numberOfSections"], "4")
        self.assertEqual(self.fileinfo.output["sectionTable"]["sections"][0]["name"], ".text")
        self.assertEqual(self.fileinfo.output["sectionTable"]["sections"][1]["name"], ".data")
        self.assertEqual(self.fileinfo.output["sectionTable"]["sections"][2]["name"], ".bss")
        self.assertEqual(self.fileinfo.output["sectionTable"]["sections"][3]["name"], ".comment")
