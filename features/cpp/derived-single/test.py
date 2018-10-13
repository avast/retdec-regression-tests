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
        assert self.out_c.has_string_literal_matching( r'Base::Base(\\n)?' )
        assert self.out_c.has_string_literal_matching( r'Base::~Base(\\n)?' )
        assert self.out_c.has_string_literal_matching( r'Base::method1 : %d(\\n)?' )
        assert self.out_c.has_string_literal_matching( r'Derived::~Derived(\\n)?' )
        assert self.out_c.has_string_literal_matching( r'Derived::method1 : %d %d(\\n)?' )
        assert self.out_c.has_string_literal_matching( r'Derived::method2 : %d %d(\\n)?' )
        assert self.out_c.has_string_literal_matching( r'Dump Base %d(\\n)?' )
        assert self.out_c.has_string_literal_matching( r'Dump Derived %d %d(\\n)?' )
        assert self.out_c.has_string_literal_matching( r'Base test:(\\n)?' )
        assert self.out_c.has_string_literal_matching( r'Derived test:(\\n)?' )

        # String is not found on many archs. Checking for it only on some would be
        # to difficult -> do not check for it at all right now.
        #assert self.out_c.has_string_literal_matching( r'Derived::Derived(\\n)?' )

    def test_for_vtables(self):
        assert self.out_config.vtable_count == 2

        vtable1 = self.out_config.vtables[0]
        vtable2 = self.out_config.vtables[1]

        assert vtable1.item_count == 3 or vtable1.item_count == 4

        if vtable1.item_count == 3:
            assert vtable2.item_count == 4
            base = vtable1
            derived = vtable2
        elif vtable1.item_count == 4:
            assert vtable2.item_count == 3
            base = vtable2
            derived = vtable1

        base_names = set([ x for x in base.item_target_names if "function_" not in x ])
        derived_names = set([ x for x in derived.item_target_names if "function_" not in x ])

        possible_base_names = [ ['_ZN4BaseD2Ev', '_ZN4BaseD0Ev', '_ZN4Base7method1Ev'],
                                ['__ZN4BaseD1Ev', '__ZN4BaseD0Ev', '__ZN4Base7method1Ev'],
                                ['___bid_truncdddf.5', '__ZN4BaseD0Ev', '__ZN4Base7method1Ev'],
                                ['___bid_truncdddf_63', '__ZN4BaseD0Ev', '__ZN4Base7method1Ev'],
                                ['___bid_truncdddf_12', '__ZN4BaseD0Ev', '__ZN4Base7method1Ev'],
                                ['__ZN4BaseD0Ev', '__ZN4Base7method1Ev'],
                                ['_ZN4BaseD1Ev', '_ZN4BaseD0Ev', '_ZN4Base7method1Ev'] ]

        possible_derived_names = [  ['_ZN7DerivedD2Ev', '_ZN7DerivedD0Ev', '_ZN7Derived7method1Ev', '_ZN7Derived7method2Ev'],
                                    ['__ZN7DerivedD1Ev', '__ZN7DerivedD0Ev', '__ZN7Derived7method1Ev', '__ZN7Derived7method2Ev'],
                                    ['___bid_truncdddf.7', '__ZN7DerivedD0Ev', '__ZN7Derived7method1Ev', '__ZN7Derived7method2Ev'],
                                    ['___bid_truncdddf_65', '__ZN7DerivedD0Ev', '__ZN7Derived7method1Ev', '__ZN7Derived7method2Ev'],
                                    ['___bid_truncdddf_14', '__ZN7DerivedD0Ev', '__ZN7Derived7method1Ev', '__ZN7Derived7method2Ev'],
                                    ['__ZN7DerivedD0Ev', '__ZN7Derived7method1Ev', '__ZN7Derived7method2Ev'],
                                    ['_ZN7DerivedD1Ev', '_ZN7DerivedD0Ev', '_ZN7Derived7method1Ev', '_ZN7Derived7method2Ev'] ]

        possible_base_names_set = set(frozenset(i) for i in possible_base_names)
        possible_derived_names_set = set(frozenset(i) for i in possible_derived_names)

        #print('[\'',end='');print(*base.item_target_names, sep='\', \'', end='\'');print(']')
        #print('[\'',end='');print(*derived.item_target_names, sep='\', \'', end='\'');print(']')

        self.assertIn(base_names, possible_base_names_set)
        self.assertIn(derived_names, possible_derived_names_set)

class TestAllStripped(TestBase):
    settings = TestSettings(
        input=files_in_dir('inputs/stripped'),
        args='-k'
    )

    def test_for_vtables(self):
        assert self.out_config.vtable_count == 2

        vtable1 = self.out_config.vtables[0]
        vtable2 = self.out_config.vtables[1]

        assert vtable1.item_count == 3 or vtable1.item_count == 4

        if vtable1.item_count == 3:
            assert vtable2.item_count == 4
            base = vtable1
            derived = vtable2
        elif vtable1.item_count == 4:
            assert vtable2.item_count == 3
            base = vtable2
            derived = vtable1

        base_names = set(base.item_target_names)
        derived_names = set(derived.item_target_names)

        # there are no empty base_names
        assert "" not in base_names
        assert "" not in derived_names

class TestMsvcDebug(TestBase):
    settings = TestSettings(
        input='inputs/msvc/derived-single-msvc-debug.ex',
        args='-k'
    )

class TestMsvcRelease(TestBase):
    settings = TestSettings(
        input='inputs/msvc/derived-single-msvc-release.ex',
        args='-k'
    )

    def test_for_string(self):
        assert self.out_c.has_string_literal( 'Dump Base %d\\n' )
        assert self.out_c.has_string_literal( 'Dump Derived %d %d\\n' )
        assert self.out_c.has_string_literal( 'Base test:\\n' )
        assert self.out_c.has_string_literal( 'Derived test:\\n' )
        assert self.out_c.has_string_literal( 'Base::Base\\n' )
        assert self.out_c.has_string_literal( 'Derived::Derived\\n' )
        assert self.out_c.has_string_literal( 'Derived::~Derived\\n' )
        assert self.out_c.has_string_literal( 'Derived::method1 : %d %d\\n' )
        assert self.out_c.has_string_literal( 'Derived::method2 : %d %d\\n' )
        assert self.out_c.has_string_literal( 'Base::~Base\\n' )
        assert self.out_c.has_string_literal( 'Base::method1 : %d\\n' )

    def test_for_vtables(self):
        assert self.out_config.vtable_count == 3
        assert self.out_config.has_just_vtables('vtable_40210c', 'vtable_4021ec', 'vtable_4021fc')

        vtable1 = self.out_config.vtables['vtable_40210c']
        assert vtable1.item_count == 1
        #assert vtable1.items[0].target_name == '_qm__qm__Etype_info__UAEPAXI_Z'

        vtable2 = self.out_config.vtables['vtable_4021ec']
        assert vtable2.item_count == 3
        assert vtable2.items[0].target_name == 'function_4010a0'
        assert vtable2.items[1].target_name == 'function_401060'
        assert vtable2.items[2].target_name == 'function_401080'

        vtable2 = self.out_config.vtables['vtable_4021fc']
        assert vtable2.item_count == 2
        assert vtable2.items[0].target_name == 'function_401020'
        assert vtable2.items[1].target_name == 'function_401000'
