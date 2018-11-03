from regression_tests import *

class TestTypeRefNested(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='typeref_hash_nested',
        args='--verbose --json'
    )

    def test_correctly_analyzes_typerefs_default(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][0]['libraryName'], 'System.Runtime')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][0]['name'], 'CompilationRelaxationsAttribute')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][1]['libraryName'], 'System.Runtime')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][1]['name'], 'RuntimeCompatibilityAttribute')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][2]['libraryName'], 'System.Runtime')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][2]['name'], 'DebuggableAttribute')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][3]['libraryName'], 'System.Runtime')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][3]['name'], 'DebuggingModes.DebuggableAttribute')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][4]['libraryName'], 'System.Runtime')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][4]['name'], 'TargetFrameworkAttribute')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][5]['libraryName'], 'System.Runtime')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][5]['name'], 'AssemblyCompanyAttribute')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][6]['libraryName'], 'System.Runtime')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][6]['name'], 'AssemblyConfigurationAttribute')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][7]['libraryName'], 'System.Runtime')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][7]['name'], 'AssemblyFileVersionAttribute')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][8]['libraryName'], 'System.Runtime')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][8]['name'], 'AssemblyInformationalVersionAttribute')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][9]['libraryName'], 'System.Runtime')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][9]['name'], 'AssemblyProductAttribute')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][10]['libraryName'], 'System.Runtime')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][10]['name'], 'AssemblyTitleAttribute')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][11]['libraryName'], 'System.Runtime')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][11]['name'], 'Object')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][12]['libraryName'], 'CustomLibrary')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][12]['name'], 'CustomClass1')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][13]['libraryName'], 'CustomLibrary')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][13]['name'], 'CustomClass2')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][14]['libraryName'], 'CustomLibrary')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][14]['name'], 'CustomSubClassA.CustomClass1')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][15]['libraryName'], 'CustomLibrary')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][15]['name'], 'CustomSubClassB.CustomClass2')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][16]['libraryName'], 'CustomLibrary')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][16]['name'], 'CustomSubSubClassX.CustomSubClassB.CustomClass2')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][17]['libraryName'], 'System.Console')
        self.assertEqual(self.fileinfo.output['typeRefTable']['dotnet imported classes'][17]['name'], 'Console')

    def test_correctly_computes_typeref_hash(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['typeRefTable']['crc32'], '2553516c')
        self.assertEqual(self.fileinfo.output['typeRefTable']['md5'], '5742603226df6e720f055413ba924c2c')
        self.assertEqual(self.fileinfo.output['typeRefTable']['sha256'], 'c40e879174d85aaf426217ab5e39de04214245636550b82051a759d2946f15db')

# https://github.com/avast-tl/retdec/issues/363
# Test typeref hashes for .NET files
# Default VS binary
class TestTypeRefHashDefault(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='typeref_hash_default',
        args='--verbose --json'
    )

    def test_correctly_computes_typeref_hash(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['typeRefTable']['crc32'], 'bb390cc9')
        self.assertEqual(self.fileinfo.output['typeRefTable']['md5'], '93b7f964c87a94b07d1f6171f0b7d7c1')
        self.assertEqual(self.fileinfo.output['typeRefTable']['sha256'], '37a37a2d4cc651a9b6cf54da949cbb6c89fc1e6e9991628087741d51666c7f1b')

# VS nested class binary with cyclic referencing
class TestTypeRefHashNestedInfinite(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='typeref_hash_nested_infinite',
        args='--verbose --json'
    )

    def test_correctly_computes_typeref_hash(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['typeRefTable']['crc32'], '0c472e09')
        self.assertEqual(self.fileinfo.output['typeRefTable']['md5'], 'f8a9907a02d8a1bede13aa8dfc005269')
        self.assertEqual(self.fileinfo.output['typeRefTable']['sha256'], '9b327187b627a940bfe8645ca3df66500906f1822cfe08e279cbf23a7dd23660')