from regression_tests import *

# https://github.com/avast/retdec/issues/138
# Test for proper Visual Basic metadata parsing
class Test1(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='3e7126c600eb3d73c9b470aa98f2a416',
        args='--verbose --json'
    )

    def test_visual_basic_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['backupLanguageDLL'], '*')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['isPCode'], 'yes')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['languageDLL'], 'VB6DE.DLL')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['languageDLLPrimaryLCID'], 'German - Germany')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['languageDLLSecondaryLCID'], 'English - United States')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['projectDescription'], 'Projekt1')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['projectExeName'], 'my_st0re_loader_____')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['projectName'], 'muschmusch')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['projectPath'], 'C:\\Users\\Tix\\Desktop\\Sell_Tools\\iProtect\\load\\asdasd.vbp')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['projectPrimaryLCID'], 'English - United States')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['projectSecondaryLCID'], 'German - Austria')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['typeLibCLSID'], 'AB656C18-7E7D-2A48-90D0-CC26EBE49DE4')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['typeLibLCID'], 'Unspecified')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['typeLibMajorVersion'], '1')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['typeLibMinorVersion'], '0')

    def test_visual_basic_extern_table(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['externTable']['crc32'], '4647fd66')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['externTable']['md5'], '038528f5da1ca95d66de9ffb558a8fad')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['externTable']['sha256'], '8903e14d38862749270803180fc2240bce4610e28b2e4f4bfdaec55a6cfaa3ff')

        self.assertEqual(self.fileinfo.output['visualBasicInfo']['externTable']['externs'][0]['apiName'], 'ARgopzWRvwdj')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['externTable']['externs'][0]['moduleName'], 'netapi32')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['externTable']['externs'][1]['apiName'], 'PYZXczGNsFE')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['externTable']['externs'][1]['moduleName'], 'netapi32')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['externTable']['externs'][2]['apiName'], 'HMxqxbooEHKCbqjT')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['externTable']['externs'][2]['moduleName'], 'mapi32')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['externTable']['externs'][3]['apiName'], 'eiIwtnFCZvUZW')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['externTable']['externs'][3]['moduleName'], 'mapi32')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['externTable']['externs'][4]['apiName'], 'CallWindowProcW')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['externTable']['externs'][4]['moduleName'], 'UsEr32')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['externTable']['externs'][5]['apiName'], 'pNfrfdXpmJsDJFRi')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['externTable']['externs'][5]['moduleName'], 'netapi32')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['externTable']['externs'][6]['apiName'], 'KnSCymHxoCMv')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['externTable']['externs'][6]['moduleName'], 'netapi32')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['externTable']['externs'][7]['apiName'], 'zVWgpkOdwQje')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['externTable']['externs'][7]['moduleName'], 'shell32')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['externTable']['externs'][8]['apiName'], 'ylMihJrIuyYyKDWTq')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['externTable']['externs'][8]['moduleName'], 'version.dll')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['externTable']['externs'][9]['apiName'], 'BegNhmukPYZXczGN')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['externTable']['externs'][9]['moduleName'], 'mapi32')

    def test_visual_basic_object_table(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['objectTable']['guid'], '005CD394-A073-944E-8831-0A6EFC7D3AF0')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['objectTable']['crc32'], '0b86b7f1')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['objectTable']['md5'], 'f6c85535feafadb74306afc874c516a0')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['objectTable']['sha256'], 'ae05250c967d1f55105322454ada56db6990bd74a41a2cc63ce4e2f458a85616')

        self.assertEqual(self.fileinfo.output['visualBasicInfo']['objectTable']['objects'][0]['name'], 'acnaAA')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['objectTable']['objects'][0]['methods'][0], 'RunPE')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['objectTable']['objects'][0]['methods'][1], 'Invoke')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['objectTable']['objects'][0]['methods'][2], 'sDecryptName')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['objectTable']['objects'][0]['methods'][3], 'InjPath')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['objectTable']['objects'][0]['methods'][4], 'nand')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['objectTable']['objects'][0]['methods'][5], 'xori')


# Test for proper COM Visual Basic metadata parsing
class Test2(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='c4affaea94863009d90668c9d86291864cd6027d798a20085b5110f6473450b7',
        args='--verbose --json'
    )

    def test_visual_basic_com_data_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['comObjectCLSID'], '13A84C25-CDF1-F24D-9338-CEF08CAAF469')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['comObjectEventsCLSID'], '3490B97E-F7E7-8847-8A6F-97AB39FC9C97')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['comObjectInterfaceCLSID'], '1A2ADBEC-0944-C944-A046-F535D14B4E10')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['comObjectName'], 'usrReverseRelay')
        self.assertEqual(self.fileinfo.output['visualBasicInfo']['comObjectType'], 'ActiveXUserControl')
