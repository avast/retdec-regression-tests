from regression_tests import *

class DotNetEdgeCaseTest1(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=['DotNetSample32.exe_', 'DotNetSample32_NoDataDir.exe_']
    )

    def test_is_dotnet(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
        self.assertEqual(self.fileinfo.output['languages'][0]['name'], 'CIL/.NET')
        self.assertTrue(self.fileinfo.output['languages'][0]['bytecode'])
        self.assertEqual(self.fileinfo.output['dotnetInfo']['runtimeVersion'], '2.5')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['moduleVersionId'], 'e843efa5-5493-4098-8cd4-aa9a386da08e')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['classes'][0]['fullyQualifiedName'], 'TestNetAppForms.Program')

class DotNetEdgeCaseTest2(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=['TestDotNetInResources32.exe_', 'TestDotNetInResources64.exe_']
    )

    def test_is_not_dotnet(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
        self.assertFalse('languages' in self.fileinfo.output)
        self.assertFalse('dotnetInfo' in self.fileinfo.output)

