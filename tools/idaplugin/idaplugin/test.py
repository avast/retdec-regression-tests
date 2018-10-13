from regression_tests import *

base_settings = TestSettings(
    tool='idaplugin',
    input='idaplugin.ex'
)

class TestDecompileMainDecodeOnly(Test):
    settings = TestSettings.from_settings(base_settings,
        args='--select 0x40159a'
    )

    def test_fnc_properties(self):
        assert self.out_c.has_just_funcs('_main')
        fnc = self.out_c.funcs['_main']

        assert fnc.return_type.is_int()
        assert fnc.has_just_params('argc', 'argv', 'envp')

        assert fnc.params['argc'].type.is_int()
        assert fnc.params['argv'].type.is_pointer()
        assert fnc.params['argv'].type.pointed_type.is_pointer()
        assert fnc.params['argv'].type.pointed_type.pointed_type.is_char()

        assert fnc.calls('___main', '_addRet', '_addNoRet', '_fAddRet', '_fAddNoRet', '_printf', '_rand')

class TestDecompile_addRet(Test):
    settings = TestSettings.from_settings(base_settings,
        args='--select 0x401560'
    )

    def test_fnc_properties(self):
        assert self.out_c.has_just_funcs('_addRet')
        fnc = self.out_c.funcs['_addRet']

        assert fnc.return_type.is_int(32)
        assert fnc.has_just_params('a1', 'a2')

        assert fnc.params['a1'].type.is_int(32)
        assert fnc.params['a2'].type.is_int(32)

        assert self.out_c.contains(r'return a2 \+ a1;')

class TestDecompile_addNoRet(Test):
    settings = TestSettings.from_settings(base_settings,
        args='--select 0x40156d'
    )

    def test_fnc_properties(self):
        assert self.out_c.has_just_funcs('_addNoRet')
        fnc = self.out_c.funcs['_addNoRet']

        assert fnc.return_type.is_int(32)
        assert fnc.has_just_params('a1', 'a2', 'a3')

        assert fnc.params['a1'].type.is_int(32)
        assert fnc.params['a2'].type.is_int(32)
        assert fnc.params['a3'].type.is_int(32)

        assert self.out_c.contains(r'a3 \= a. \+ a.;')

class TestDecompile_fAddRet(Test):
    settings = TestSettings.from_settings(base_settings,
        args='--select 0x40157f'
    )

    def test_fnc_properties(self):
        assert self.out_c.has_just_funcs('_fAddRet')
        fnc = self.out_c.funcs['_fAddRet']

        assert fnc.return_type.is_int(32)
        assert fnc.has_just_params('a1', 'a2')

        assert fnc.params['a1'].type.is_float(32)
        assert fnc.params['a2'].type.is_float(32)

        # TODO: tu sa z nejakeho dovodu nevykona sucet a nie je pouzity v returne.
        #assert self.out_c.contains(r'return a2 \+ a1;')

class TestDecompile_fAddNoRet(Test):
    settings = TestSettings.from_settings(base_settings,
        args='--select 0x40158a'
    )

    def test_fnc_properties(self):
        assert self.out_c.has_just_funcs('_fAddNoRet')
        fnc = self.out_c.funcs['_fAddNoRet']

        assert fnc.has_just_params('a1', 'a2', 'a3')

        assert fnc.params['a1'].type.is_float(32)
        assert fnc.params['a2'].type.is_float(32)
        #assert fnc.params['a3'].type.is_float(32) # TODO: this is int32_t, but it comes like that from IDA, so there is nothing we can doright now.

        assert self.out_c.contains(r'a3 \= a. \+ a.;')

class TestDecompileAll(Test):
    settings = TestSettings.from_settings(base_settings)

    # Names are from config. Therefore, this also tests that IDA names are applied.
    #
    def test_only_reachable(self):
        assert self.out_c.has_funcs('_addRet', '_addNoRet', '_fAddRet', '_fAddNoRet', '_main')
