from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input=[
            'pbmsrch_large.arm.gcc.O0.s.exe',
            'pbmsrch_large.mips.gcc.O0.s.elf',
            'pbmsrch_large.x86.gcc.O0.s.exe',
            'pbmsrch_large.x86.gcc.O0.s.elf',
        ],
    )

    def test_for_main(self):
        assert self.out_c.has_funcs('main') or self.out_c.has_funcs('entry_point')

    def test_arrays_are_detected(self):
        found_find_strings = False
        found_search_strings = False

        for gv in self.out_c.global_vars:
            if (gv.type.is_array() and gv.type.element_type.is_pointer()
                    and gv.type.element_type.pointed_type.is_char()):
                if gv.type.element_count == 1332:
                    # Check only some of the strings in the initializer.
                    self.assertEqual(gv.initializer[0], 'Kur')
                    self.assertEqual(gv.initializer[1], 'gent')
                    self.assertEqual(gv.initializer[-2], 'more')
                    self.assertEqual(gv.initializer[-1], 'me')
                    found_find_strings = True
                elif gv.type.element_count == 21699:
                    # Check only some of the strings in the initializer.
                    self.assertEqual(gv.initializer[0], 'Kurt Vonneguts Commencement Address at')
                    self.assertEqual(gv.initializer[1], 'MIT Ladies and gentlemen of')
                    self.assertEqual(gv.initializer[-2], 'zygote')
                    # The last string ('') on position -1 is not detected on
                    # some combinations, so do not check for it here.
                    found_search_strings = True

        assert found_find_strings
        assert found_search_strings

    def test_strings_are_detected(self):
        assert self.out_c.has_string_literal_matching( r'Kur' ) # first find_strings
        assert self.out_c.has_string_literal_matching( r'Politicians' ) # mid find_strings
        assert self.out_c.has_string_literal_matching( r'me' ) # last find_strings

        assert self.out_c.has_string_literal_matching( r'Kurt Vonneguts Commencement Address at' ) # first search_strings
        assert self.out_c.has_string_literal_matching( r'fructose' ) # mid search_strings
        assert self.out_c.has_string_literal_matching( r'zygote' ) # one before last search_strings
        assert self.out_c.has_string_literal_matching( r'' ) # last search_strings
