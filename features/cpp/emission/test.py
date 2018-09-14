from regression_tests import *

class Test(Test):
    """Checks that C++-related information is emitted into the C file."""

    settings = TestSettings(
        input='abstract-class.x86.gcc.O0.g.elf',
        args='-k'
    )

    def test_class_names_are_emitted_in_comments(self):
        assert self.out_c.contains('--- Classes ---')
        assert self.out_c.has_comment_matching(r'.* Polygon')
        assert self.out_c.has_comment_matching(r'.* Triangle \(base classes: Polygon\)')
        assert self.out_c.has_comment_matching(r'.* Rectangle \(base classes: Polygon\)')

    def test_funcs_have_class_info_emitted_in_comments(self):
        assert self.out_c.has_comment_matching(r'.* From class: * Polygon')
        assert self.out_c.has_comment_matching(r'.* From class: * Triangle')
        assert self.out_c.has_comment_matching(r'.* From class: * Rectangle')
        assert self.out_c.has_comment_matching(r'.* Type: * virtual member function')
        assert self.out_c.has_comment_matching(r'.* Type: * constructor')
