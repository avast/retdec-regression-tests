from regression_tests import *

class Test(Test):
    """Checks that we do not generate classes with invalid names (see #1404).
    """

    settings = TestSettings(
        input='mips-elf-df0691c'
    )

    def test_no_class_with_invalid_name_is_generated(self):
        # Before the fix, two classes with invalid names were generated. Now,
        # no class should be generated.
        self.assertEqual(self.out_config.classes_count, 0)
