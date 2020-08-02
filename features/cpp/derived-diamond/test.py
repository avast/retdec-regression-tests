from regression_tests import *

class TestBase(Test):
    def test_for_main(self):
        assert self.out_c.has_funcs('main') or self.out_c.has_funcs('entry_point')

    def test_check_main_is_not_ctor_or_dtor(self):
        for c in self.out_config.classes:
            assert "main" not in c.constructors
            assert "main" not in c.destructors

class TestAll(TestBase):
    settings = TestSettings(
        input=files_in_dir('inputs/symbols'),
        args='-k'
    )

    def test_for_string(self):
        # printf() is used -> '\n' at the end of the string
        # puts() is used -> no '\n' at the end of the string
        assert self.out_c.has_string_literal_matching( r'A::a\(\)(\\n)?' )

    def test_for_classes(self):
        assert self.out_config.classes_count == 4

class TestAllStripped(TestBase):
    settings = TestSettings(
        input=files_in_dir('inputs/stripped'),
        args='-k'
    )

    def test_for_classes(self):
        assert self.out_config.classes_count == 4

class TestMsvcDebug(TestBase):
    settings = TestSettings(
        input='inputs/msvc/derived-diamond-msvc-debug.ex',
        args='-k'
    )

    def test_for_classes(self):
        assert self.out_config.classes_count == 5

class TestMsvcRelease(TestBase):
    settings = TestSettings(
        input='inputs/msvc/derived-diamond-msvc-release.ex',
        args='-k'
    )

    def test_for_classes(self):
        assert self.out_config.classes_count == 5
