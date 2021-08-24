from regression_tests import *

class Test001(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--verbose --json',
        input='dropped.ex'
    )

    def test_delayed_imports_detection(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '80')
        self.assertEqual(self.fileinfo.output['importTable']['md5'], '6f94503e98785a3637bc2177cce10427')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][69]['index'], '69')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][72]['index'], '72')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][73]['index'], '73')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][74]['index'], '74')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][75]['index'], '75')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][76]['index'], '76')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][77]['index'], '77')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][78]['index'], '78')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][79]['index'], '79')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][72]['name'], 'GetInputState')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][73]['name'], 'wsprintfA')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][74]['name'], 'PostThreadMessageA')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][75]['name'], 'GetMessageA')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][76]['name'], 'GetDesktopWindow')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][77]['name'], 'RegOpenKeyExA')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][78]['name'], 'RegCloseKey')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][79]['name'], 'RegQueryValueExA')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][69]['libraryName'], 'WS2_32.dll')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][72]['libraryName'], 'USER32.dll')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][73]['libraryName'], 'USER32.dll')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][74]['libraryName'], 'USER32.dll')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][75]['libraryName'], 'USER32.dll')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][76]['libraryName'], 'USER32.dll')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][77]['libraryName'], 'ADVAPI32.dll')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][78]['libraryName'], 'ADVAPI32.dll')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][79]['libraryName'], 'ADVAPI32.dll')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][69]['address'], '0x40911c')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][72]['address'], '0x4020ae')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][73]['address'], '0x402078')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][74]['address'], '0x40209c')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][75]['address'], '0x40208a')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][76]['address'], '0x402058')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][77]['address'], '0x4020f2')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][78]['address'], '0x4020c0')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][79]['address'], '0x4020e0')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][69]['name'], 'sendto')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][69]['ordinalNumber'], '20')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][69]['delayed'], 'false')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][72]['delayed'], 'true')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][73]['delayed'], 'true')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][74]['delayed'], 'true')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][75]['delayed'], 'true')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][76]['delayed'], 'true')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][77]['delayed'], 'true')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][78]['delayed'], 'true')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][79]['delayed'], 'true')

class Test002(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--verbose --json',
        input='delay_loaded_dlls_by_va_32bit.ex_'
    )

    def test_delayled_imports_detection(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '31')
        self.assertEqual(self.fileinfo.output['importTable']['md5'], 'c64d18c2324195b6f30e544ac4d0793a')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['index'], '0')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['libraryName'], 'KERNEL32.dll')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['address'], '0x400a00')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['name'], 'GetModuleHandleA')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['delayed'], 'false')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][25]['index'], '25')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][25]['libraryName'], 'COMCTL32.dll')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][25]['address'], '0x400708')
        assert 'name' not in self.fileinfo.output['importTable']['imports'][25]
        self.assertEqual(self.fileinfo.output['importTable']['imports'][25]['ordinalNumber'], '17')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][25]['delayed'], 'true')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][26]['index'], '26')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][26]['libraryName'], 'COMCTL32.dll')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][26]['address'], '0x4006e8')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][26]['name'], 'InitCommonControlsEx')
        assert 'ordinalNumber' not in self.fileinfo.output['importTable']['imports'][26]
        self.assertEqual(self.fileinfo.output['importTable']['imports'][26]['delayed'], 'true')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][27]['index'], '27')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][27]['libraryName'], 'WS2_32.dll')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][27]['address'], '0x40075e')
        assert 'name' not in self.fileinfo.output['importTable']['imports'][27]
        self.assertEqual(self.fileinfo.output['importTable']['imports'][27]['ordinalNumber'], '115')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][27]['delayed'], 'true')

class Test003(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--verbose --json',
        input='delay_loaded_dlls_rva_32bit.ex_'
    )

    def test_delayed_imports_detection(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '31')
        self.assertEqual(self.fileinfo.output['importTable']['md5'], '7877a03959578abdcfd18f857518208c')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['index'], '0')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['libraryName'], 'KERNEL32.dll')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['address'], '0x400c00')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['name'], 'WaitForSingleObject')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['delayed'], 'false')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][25]['index'], '25')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][25]['libraryName'], 'COMCTL32.dll')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][25]['address'], '0x4006ec')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][25]['name'], 'InitCommonControlsEx')
        assert 'ordinalNumber' not in self.fileinfo.output['importTable']['imports'][25]
        self.assertEqual(self.fileinfo.output['importTable']['imports'][25]['delayed'], 'true')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][26]['index'], '26')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][26]['libraryName'], 'COMCTL32.dll')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][26]['address'], '0x4006d1')
        assert 'name' not in self.fileinfo.output['importTable']['imports'][26]
        self.assertEqual(self.fileinfo.output['importTable']['imports'][26]['ordinalNumber'], '17')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][26]['delayed'], 'true')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][27]['index'], '27')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][27]['libraryName'], 'WS2_32.dll')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][27]['address'], '0x400727')
        assert 'name' not in self.fileinfo.output['importTable']['imports'][27]
        self.assertEqual(self.fileinfo.output['importTable']['imports'][27]['ordinalNumber'], '115')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][27]['delayed'], 'true')

class Test004(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--verbose --json',
        input='delay_loaded_dlls_rva_64bit.ex_'
    )

    def test_delayed_imports_detection(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '30')
        self.assertEqual(self.fileinfo.output['importTable']['md5'], '68592d0426806874d10b4c28d9c5cd40')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['index'], '0')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['libraryName'], 'KERNEL32.dll')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['address'], '0x140001000')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['name'], 'WaitForSingleObject')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][24]['index'], '24')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][24]['libraryName'], 'COMCTL32.dll')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][24]['address'], '0x1400009b7')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][24]['name'], 'InitCommonControlsEx')
        assert 'ordinalNumber' not in self.fileinfo.output['importTable']['imports'][24]
        self.assertEqual(self.fileinfo.output['importTable']['imports'][24]['delayed'], 'true')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][25]['index'], '25')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][25]['libraryName'], 'COMCTL32.dll')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][25]['address'], '0x140000932')
        assert 'name' not in self.fileinfo.output['importTable']['imports'][25]
        self.assertEqual(self.fileinfo.output['importTable']['imports'][25]['ordinalNumber'], '17')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][25]['delayed'], 'true')

        self.assertEqual(self.fileinfo.output['importTable']['imports'][26]['index'], '26')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][26]['libraryName'], 'WS2_32.dll')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][26]['address'], '0x140000a60')
        assert 'name' not in self.fileinfo.output['importTable']['imports'][26]
        self.assertEqual(self.fileinfo.output['importTable']['imports'][26]['ordinalNumber'], '115')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][26]['delayed'], 'true')

class Test005(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--verbose --json',
        input='delayimports.ex'
    )

    def test_delayed_imports_detection(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '4')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][3]['address'], '0x401150')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][3]['index'],   '3')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][3]['libraryName'], 'msvcrt.dll')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][3]['name'], 'printf')
        self.assertEqual(self.fileinfo.output['importTable']['imports'][3]['delayed'], 'true')
        self.assertEqual(self.fileinfo.output['importTable']['md5'], '4e7b7b5b63ae609e9707b4896498325d')
