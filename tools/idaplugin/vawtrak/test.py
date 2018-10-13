from regression_tests import *

base_settings = TestSettings(
    tool='idaplugin',
    input='vawtrak.dll',
    idb='vawtrak.idb'
)

class TestDecompile_xorByRND(Test):
    settings = TestSettings.from_settings(base_settings,
        args='--select 0x10010f90'
    )

    def test_has_only_selected_fnc(self):
        assert self.out_c.has_just_funcs('xorByRND')

    def test_xorByRND_properties(self):
        fnc = self.out_c.funcs['xorByRND']

        assert fnc.return_type.is_int(32)
        assert fnc.param_count == 3
        assert fnc.has_just_params('seed', 'str', 'strLen')
        assert fnc.params['seed'].type.is_int(32)
        assert fnc.params['str'].type.is_pointer()
        assert fnc.params['str'].type.pointed_type.is_char()
        assert fnc.params['strLen'].type.is_int(32)

        assert fnc.calls('rand16')
        #assert self.out_c.contains(r' \= rand16\(.*\)')  # rand16 call is returning something
        #assert self.out_c.contains(r'v. \^ rand16')  # there is a xor aoperation on two variables

    def test_has_called_function_as_declaration(self):
        # The function is user-defined, so its prototype is emitted as a
        # declaration.
        assert self.out_c.contains(r'int32_t rand16\(int32_t \* a1\);')

class TestDecompile_getNextRegValueOfFCkey(Test):
    settings = TestSettings.from_settings(base_settings,
        args='--select 0x1000dd3e'
    )

    def test_has_only_selected_fnc(self):
        assert self.out_c.has_just_funcs('getNextRegValueOfFCkey')

    def test_getNextRegValueOfFCkey_properties(self):
        fnc = self.out_c.funcs['getNextRegValueOfFCkey']

        assert fnc.return_type.is_pointer()
        assert fnc.return_type.pointed_type.is_struct()
        struct = fnc.return_type.pointed_type
        assert struct.member_count == 1
        assert struct.name == "HKEY__"
        assert struct.members[0].type.is_int()

        assert fnc.param_count == 3
        assert fnc.has_just_params('outSubKey', 'filename', 'pcbData')
        assert fnc.params['outSubKey'].type.is_pointer()
        assert fnc.params['outSubKey'].type.pointed_type.is_char()
        assert fnc.params['filename'].type.is_pointer()
        assert fnc.params['filename'].type.pointed_type.is_pointer()
        assert fnc.params['filename'].type.pointed_type.pointed_type.is_char()
        assert fnc.params['pcbData'].type.is_pointer()
        assert fnc.params['pcbData'].type.pointed_type.is_int(32)

        assert fnc.calls('lstrcpyA')
        assert self.out_c.contains(r'lstrcpyA\(outSubKey') or \
            (self.out_c.contains(r'lstrcpyA\(lpString1') and self.out_c.contains(r' lpString1 = \(int32_t\)outSubKey'))  # lstrcpyA is using 'outSubKey' in 'edx'

        assert fnc.calls('lstrcatA')
        assert self.out_c.contains(r'lstrcatA\(outSubKey') or \
            (self.out_c.contains(r'lstrcatA\(.*lpString1') and self.out_c.contains(r'lpString1 =.*outSubKey'))

        assert fnc.calls('sub_1001580D')
        assert fnc.calls('lstrlenA')
        assert fnc.calls('RegEnumValueA')
        assert fnc.calls('sub_10015C16')
        assert fnc.calls('StrCmpNIA')

        assert fnc.calls('sub_1000DC14')
        #assert self.out_c.contains(r'v[0-9]* \= sub_1000DC14\(outSubKey, .*filename,') or \
            #(self.out_c.contains(r'v[0-9]* \= sub_1000DC14\(.*lpString1, .*filename,') and self.out_c.contains(r'lpString1 =.*outSubKey')) or \
            #(self.out_c.contains(r'v[0-9]* \= sub_1000DC14\(.*lpValueName, .*filename,') and self.out_c.contains(r'lpValueName =.*outSubKey'))

        # TODO: check usega of the third parameter

        assert fnc.calls('sub_10010D1B')
        assert fnc.calls('RegCloseKey')

    def test_has_strings(self):
        assert self.out_c.has_string_literal('SOFTWARE\\\\')
        assert self.out_c.has_string_literal('#FC_')

class TestDecompile_sub_1000BB79(Test):
    settings = TestSettings.from_settings(base_settings,
        args='--select 0x1000bb79'
    )

    def test_has_only_selected_fnc(self):
        assert self.out_c.has_just_funcs('sub_1000BB79')

    def test_sub_1000BB79_properties(self):
        fnc = self.out_c.funcs['sub_1000BB79']

        assert fnc.return_type.is_int(32)
        assert fnc.param_count == 10
        assert fnc.params['lpString'].type.is_pointer()
        assert fnc.params['lpString'].type.pointed_type.is_char()

        assert fnc.calls('sub_1000EBE9','lstrlenA','wsprintfA','sub_10010D1B','sub_1000B98A','sub_1000EBFA','sub_10010C72')

        assert self.out_c.has_string_literal(' /bpmagic=')
        assert self.out_c.has_string_literal('%s%s%u')

    def test_has_called_function_as_external(self):
        assert self.out_c.has_comment_matching(r'.*int.*lstrlenA\(.*lpString.*')
        assert self.out_c.has_comment_matching(r'.*int.*wsprintfA\(.*...')

class TestDecompile_unregisterAutorun3(Test):
    settings = TestSettings.from_settings(base_settings,
        args='--select 0x1001880a'
    )

    def test_has_only_selected_fnc(self):
        assert self.out_c.has_just_funcs('unregisterAutorun3')

    def test_unregisterAutorun3_properties(self):
        fnc = self.out_c.funcs['unregisterAutorun3']

        assert fnc.return_type.is_int(32)
        assert fnc.param_count == 0

        assert fnc.calls('getApplicationDataFullPath','regOpenKeyAndCallProc')

        assert self.out_c.has_string_literal('Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run')

    def test_has_called_functions_as_declarations(self):
        # The functions are user-defined, so their prototypes are emitted as
        # declarations.
        assert self.out_c.contains(r'int32_t getApplicationDataFullPath\(.*\);')
        assert self.out_c.contains(r'int32_t regOpenKeyAndCallProc\(.*\);')

class TestDecompile_cyberDuck_grabPasswordsInFolders(Test):
    settings = TestSettings.from_settings(base_settings,
        args='--select 0x10021a1f'
    )

    def test_has_only_selected_fnc(self):
        assert self.out_c.has_just_funcs('cyberDuck_grabPasswordsInFolders')

    def test_grabPasswordsInFolders_properties(self):
        fnc = self.out_c.funcs['cyberDuck_grabPasswordsInFolders']

        assert fnc.return_type.is_int(32)
        assert fnc.param_count == 2
        assert fnc.has_just_params('csidl', 'heapStruct')
        assert fnc.params['csidl'].type.is_int(32)

        # TODO: regress tests can not check for structure at the moment.
        # Modify this check when it is possible.
        #
        assert fnc.params['heapStruct'].type.is_pointer()
        assert fnc.params['heapStruct'].type.pointed_type.is_struct()
        structure = fnc.params['heapStruct'].type.pointed_type
        assert structure.has_name()
        assert structure.name == 'HEAPSTRUCT'
        assert structure.member_count == 6
        #
        # TODO: check for real names once it s possible to generate element names.
        #
        assert structure.members[0].name == 'e0'
        assert structure.members[0].type.is_int(32)
        assert structure.members[5].name == 'e5'
        assert structure.members[5].type.is_int(32)

        assert fnc.calls('SHGetFolderPathA','lstrcatA','sub_1000FCDF')

        assert self.out_c.has_string_literal('\\\\Cyberduck')
        assert self.out_c.has_string_literal('user.config')

        # check return
        assert self.out_c.contains('result \= sub_1000FCDF\(.*\)')
        assert self.out_c.contains('return result')

    def test_has_called_function_as_external(self):
        assert self.out_c.has_comment_matching(r'.*lstrcatA\(.*')
        assert self.out_c.has_comment_matching(r'.*SHGetFolderPathA\(.*')

class TestDecompile_sub_1002243B(Test):
    settings = TestSettings.from_settings(base_settings,
        args='--select 0x1002243b'
    )

    def test_has_only_selected_fnc(self):
        assert self.out_c.has_just_funcs('sub_1002243B')

    def test_sub_1002243B_properties(self):
        fnc = self.out_c.funcs['sub_1002243B']

        assert fnc.return_type.is_int(32)
        assert fnc.param_count == 0

        # Do not check that fnc calls FreeLibrary because calls to FreeLibrary
        # are not recognized on Windows.
        assert fnc.calls('GetProcAddress', 'LoadLibraryA')

        assert self.out_c.has_string_literal('nss3.dll')
        assert self.out_c.has_string_literal('NSS_Init')
        assert self.out_c.has_string_literal('NSS_Shutdown')
        assert self.out_c.has_string_literal('NSSBase64_DecodeBuffer')
        assert self.out_c.has_string_literal('SECITEM_FreeItem')
        assert self.out_c.has_string_literal('PK11_GetInternalKeySlot')
        assert self.out_c.has_string_literal('PK11_Authenticate')
        assert self.out_c.has_string_literal('PK11SDR_Decrypt')
        assert self.out_c.has_string_literal('PK11_FreeSlot')
        assert self.out_c.has_string_literal('sqlite3.dll')
        assert self.out_c.has_string_literal('mozsqlite3.dll')
        assert self.out_c.has_string_literal('sqlite3_open')
        assert self.out_c.has_string_literal('sqlite3_close')
        assert self.out_c.has_string_literal('sqlite3_prepare')
        assert self.out_c.has_string_literal('sqlite3_step')
        assert self.out_c.has_string_literal('sqlite3_column_bytes')
        assert self.out_c.has_string_literal('sqlite3_column_blob')

    def test_global_variables(self):

        # these are int32_t
        #
        assert self.out_c.has_global_vars(
            'dword_100357B8',
            'dword_100357C0',
            'dword_100357C4',
            'dword_100357C8',
            'dword_100357CC',
            'dword_100357D4',
            'dword_100357D8',
            'dword_100357DC',
            'dword_100357E0',
            'dword_100357E8',
            'dword_100357EC',
            'dword_100357F4',
            'dword_100357F8',
            'dword_100357FC',
        )

        # these have some interesting types
        #
        #aFtp_ = self.out_c.global_vars['aFtp_']
        #assert aFtp_.type.is_array()
        #assert aFtp_.type.element_count == 5
        #assert aFtp_.type.element_type.is_int(32)
        #aSelectHostname = self.out_c.global_vars['aSelectHostname']
        #assert aSelectHostname.type.is_array()
        #assert aSelectHostname.type.element_count == 70
        #assert aSelectHostname.type.element_type.is_int(32)

        s1 = self.out_c.global_vars['dword_100357D0'].type.pointed_type
        s2 = self.out_c.global_vars['hModule'].type.pointed_type

        assert s1.name == 'HINSTANCE__'
        assert s2.name == 'HINSTANCE__'
        assert s1.member_count == 1
        assert s1.members[0].type.is_int()
        # Do not check that s1.members[0].name == 'e0' because on Windows,
        # Clang uses the definition of HINSTANCE__ from minwindef.h, which has
        # its element named 'unused'.

class TestDecompileAll(Test):
    settings = TestSettings.from_settings(base_settings)

    # whatever test -- we just want to check if it decompiles OK.
    #
    def test_have_some_fncs(self):
        assert self.out_c.has_funcs('xorByRND', 'getNextRegValueOfFCkey', 'sub_1000BB79', 'unregisterAutorun3', 'cyberDuck_grabPasswordsInFolders', 'sub_1002243B')
