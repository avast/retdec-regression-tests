from regression_tests import *

class TestSectionNames(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='malformed_section_names.ex',
        args='--verbose --json'
    )

    def issue_958_weird_section_names(self):
        assert self.fileinfo.succeeded
        sections = self.fileinfo.output['sectionTable']['sections']
        self.assertEqual(sections[0]['name'], "CODE\\x00\\x00\\x00\\x11")
        self.assertEqual(sections[1]['name'], "D\\x11TA")
        self.assertEqual(sections[2]['name'], "BSS\\x00\\x00\\x00\\x11")
        self.assertEqual(sections[3]['name'], "00000000")
        self.assertEqual(sections[4]['name'], "12311231")
        assert "name" not in sections[5]
        self.assertEqual(sections[6]['name'], "XXXXXXXX")
        self.assertEqual(sections[7]['name'], ".rsrc")
