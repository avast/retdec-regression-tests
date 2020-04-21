from regression_tests import *

class EzirizDotnetTest_001(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=[
            'sample_4.0.0.0_dotnet.exe_',
            'sample_4.5.0.0_dotnet.exe_',
            'sample_5.0.0.0_dotnet.exe_',
            'sample_5.9.8.0_dotnet.exe_',
            'sample_6.0.0.0_dotnet.exe_',
            'x86-pe-08f9c6c1cfb53ece69025050c95fcd5e-eziriz5']
    )

    def test_fileinfo_json_output_is_correctly_parsed(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'Eziriz .NET Reactor')
        self.assertEqual(self.fileinfo.output['tools'][0]['version'], '4.0.0.0 - 6.0.0.0')
        self.assertEqual(self.fileinfo.output['languages'][0]['name'], 'CIL/.NET')
        self.assertTrue(self.fileinfo.output['languages'][0]['bytecode'])

class EzirizDotnetTest_002(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=[
            'sample_6.2.0.0_dotnet.exe_',
            'sample_6.2.9.2_dotnet.exe_']
    )

    def test_fileinfo_json_output_is_correctly_parsed(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'Eziriz .NET Reactor')
        self.assertEqual(self.fileinfo.output['tools'][0]['version'], '6.2.0.0 or newer')
        self.assertEqual(self.fileinfo.output['languages'][0]['name'], 'CIL/.NET')
        self.assertTrue(self.fileinfo.output['languages'][0]['bytecode'])


class EzirizNativeTest_001(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=['sample_4.0.0.0_native.exe_',
               'x86-pe-d5a674ff381b95f36f3f4ef3e5a8d0c4-eziriz42',
               'x86-pe-ff10e014c94cbc89f9e653bc647b6d5a']
    )

    def test_fileinfo_json_output_is_correctly_parsed(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'Eziriz .NET Reactor')
        self.assertEqual(self.fileinfo.output['tools'][0]['version'], '4.0.0.0 - 4.4.7.5')

class EzirizNativeTest_002(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=[
            'sample_4.5.0.0_native.exe_',
            'sample_5.0.0.0_native.exe_',
            'sample_5.9.8.0_native.exe_',
            'sample_6.2.0.0_native.exe_',
            'sample_6.2.9.2_native.exe_']
    )

    def test_fileinfo_json_output_is_correctly_parsed(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'Eziriz .NET Reactor')
        self.assertEqual(self.fileinfo.output['tools'][0]['version'], '4.5.0.0 - 6.2.9.2')
