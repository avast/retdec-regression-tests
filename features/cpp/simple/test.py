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
        assert self.out_c.has_string_literal_matching( r'ClassA::ClassA(\\n)?' )
        assert self.out_c.has_string_literal_matching( r'%i %i(\\n)?' )
        assert self.out_c.has_string_literal_matching( r'~ClassA::ClassA(\\n)?' )

    def test_for_vtables(self):
        assert self.out_config.vtable_count == 1

        vtable = self.out_config.vtables[0]
        assert vtable.item_count == 1
        assert "doSomething" in vtable.items[0].target_name

    def test_for_classes(self):
        assert self.out_config.classes_count == 1

        c = self.out_config.classes[0]

        assert len(c.constructors) == 2
        assert len(c.destructors) == 2
        assert len(c.virtualMethods) == 1

class TestAllStripped(TestBase):
    settings = TestSettings(
        input=files_in_dir('inputs/stripped'),
        args='-k'
    )

    def test_for_vtables(self):
        assert self.out_config.vtable_count == 1
        vtable = self.out_config.vtables[0]
        assert vtable.item_count == 1
        assert vtable.items[0].target_name # there is some (!empty) function name

    def test_for_classes(self):
        assert self.out_config.classes_count == 1

        c = self.out_config.classes[0]
        assert len(c.virtualMethods) == 1

        assert len(c.constructors) == 2
        assert len(c.destructors) == 2

class TestMsvc(TestBase):
    settings = TestSettings(
        input='inputs/msvc/simple-msvc-release.ex',
        args='-k'
    )

    settings_d = TestSettings(
        input='inputs/msvc/simple-msvc-debug.ex',
        args='-k'
    )

    def test_for_string(self):
        assert self.out_c.has_string_literal( 'ClassA::ClassA\\n' )
        assert self.out_c.has_string_literal( '~ClassA::ClassA\\n' )
        assert self.out_c.has_string_literal( '%i %i\\n' )

    def test_for_vtables(self):
        assert self.out_config.vtable_count == 2

        vtable1 = self.out_config.vtables[0]
        assert vtable1.item_count == 1

        vtable2 = self.out_config.vtables[0]
        assert vtable2.item_count == 1
