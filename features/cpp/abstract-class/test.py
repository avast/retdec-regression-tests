from regression_tests import *

class TestBase(Test):
    def test_for_main(self):
        assert self.out_c.has_funcs('main') or self.out_c.has_funcs('entry_point')

    def test_check_main_is_not_ctor_or_dtor(self):
        for c in self.out_config.classes:
            assert "main" not in c.constructors
            assert "main" not in c.destructors

class TestAll(TestBase):
    settings = CriticalTestSettings(
        input=files_in_dir('inputs/symbols'),
        args='-k'
    )

    def test_for_string(self):
        # printf() is used -> '\n' at the end of the string
        # puts() is used -> no '\n' at the end of the string
        assert self.out_c.has_string_literal_matching( r'area %d(\\n)?' )

    def test_for_classes(self):
        assert self.out_config.classes_count == 3

class TestAllStripped(TestBase):
    settings = CriticalTestSettings(
        input=files_in_dir('inputs/stripped'),
        args='-k'
    )

    def test_for_classes(self):
        assert self.out_config.classes_count == 3

class TestMsvcDebug(TestBase):
    settings = CriticalTestSettings(
        input='inputs/msvc/abstract-class-msvc-debug.ex',
        args='-k'
    )

    def test_for_classes(self):
        assert self.out_config.classes_count == 4

class TestMsvcRelease(TestBase):
    settings = CriticalTestSettings(
        input='inputs/msvc/abstract-class-msvc-release.ex',
        args='-k'
    )

    def test_for_classes(self):
        assert self.out_config.classes_count == 4
