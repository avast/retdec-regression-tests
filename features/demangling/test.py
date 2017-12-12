from regression_tests import *

class FuncAndClassNamesTest(Test):
    """Checks that we emit demangled names of functions and classes in comments."""

    settings = TestSettings(
        input='abstract-class.x86.gcc.O0.elf',
        args='-k'
    )

    def test_demangled_function_names_are_emitted_in_comments(self):
        # Check only some of the names.
        assert self.out_c.has_comment_matching(r'.* Demangled: *Polygon::set_values\(int, int\)$')
        assert self.out_c.has_comment_matching(r'.* Demangled: *Triangle::area\(\)$')
        assert self.out_c.has_comment_matching(r'.* Demangled: *Triangle::Triangle\(\)$')

    def test_demangled_class_names_are_emitted_in_comments(self):
        assert self.out_c.has_comment_matching(r'.* Polygon')
        assert self.out_c.has_comment_matching(r'.* Triangle \(base classes: Polygon\)')
        assert self.out_c.has_comment_matching(r'.* Rectangle \(base classes: Polygon\)')

class FuncNamesFromConfigTest(Test):
    """Checks that we emit demangled names of functions set in input config file."""

    settings = TestSettings(
        input='abstract-class.x86.gcc.O0.elf',
        args='-k',
        config='abstract-class.json'
    )

    def test_demangled_function_names_are_emitted_in_comments(self):
        assert self.out_c.has_comment_matching(r'.*Demangled:     demangled value from input config$')

class FuncAndClassNamesFromDebugTest(Test):
    """Checks that we emit demangled names of functions and classes in comments."""

    settings = TestSettings(
        input='abstract-class.x86.gcc.O0.g.elf',
        args='-k'
    )

    def test_demangled_function_names_are_emitted_in_comments(self):
        assert self.out_c.has_comment_matching(r'.* Demangled: *Polygon::set_values\(int, int\)$')
        assert self.out_c.has_comment_matching(r'.* Demangled: *Triangle::area\(\)$')
        assert self.out_c.has_comment_matching(r'.* Demangled: *Triangle::Triangle\(\)$')

    def test_function_names_are_dwarf_linkage_names(self):
        assert self.out_c.has_func('_ZN7Polygon10set_valuesEii')
        assert self.out_c.has_func('_ZN8Triangle4areaEv')
        assert self.out_c.has_func('_ZN8TriangleC2Ev')
