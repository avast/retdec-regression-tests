from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input='subject.exe',
    )

    def test_the_reported_problem(self):
        assert self.out_c.contains(r'// 0x8048437\n\s+if \(g[0-9] != 0\) {\n\s+// 0x8048457\n\s+puts\("then/else block 3"\);\n\s+|\n\s+// 0x8048439\n\s+puts("return block");\n\s+return')

    def test_for_strings(self):
        assert self.out_c.has_string_literal('return block')
        assert self.out_c.has_string_literal('then/else block 3')
        assert self.out_c.has_string_literal('then/else block 4')
        assert self.out_c.has_string_literal('then/else block 5')
        assert self.out_c.has_string_literal('then/else block 6')
        assert self.out_c.has_string_literal('then/else block 7')
        assert self.out_c.has_string_literal('then/else block 8')
