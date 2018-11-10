from regression_tests import *

class TestTypeRefNested(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='typeref_hash_nested',
        args='--verbose --json'
    )

    def test_correctly_analyzes_typerefs_nested(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][0]['libraryName'], 'System.Runtime')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][0]['name'], 'CompilationRelaxationsAttribute')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][0]['nameSpace'], 'System.Runtime.CompilerServices')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][1]['libraryName'], 'System.Runtime')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][1]['name'], 'RuntimeCompatibilityAttribute')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][1]['nameSpace'], 'System.Runtime.CompilerServices')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][2]['libraryName'], 'System.Runtime')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][2]['name'], 'DebuggableAttribute')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][2]['nameSpace'], 'System.Diagnostics')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][3]['libraryName'], 'System.Runtime')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][3]['name'], 'DebuggingModes.DebuggableAttribute')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][3]['nameSpace'], 'System.Diagnostics')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][4]['libraryName'], 'System.Runtime')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][4]['name'], 'TargetFrameworkAttribute')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][4]['nameSpace'], 'System.Runtime.Versioning')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][5]['libraryName'], 'System.Runtime')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][5]['name'], 'AssemblyCompanyAttribute')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][5]['nameSpace'], 'System.Reflection')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][6]['libraryName'], 'System.Runtime')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][6]['name'], 'AssemblyConfigurationAttribute')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][6]['nameSpace'], 'System.Reflection')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][7]['libraryName'], 'System.Runtime')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][7]['name'], 'AssemblyFileVersionAttribute')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][7]['nameSpace'], 'System.Reflection')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][8]['libraryName'], 'System.Runtime')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][8]['name'], 'AssemblyInformationalVersionAttribute')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][8]['nameSpace'], 'System.Reflection')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][9]['libraryName'], 'System.Runtime')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][9]['name'], 'AssemblyProductAttribute')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][9]['nameSpace'], 'System.Reflection')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][10]['libraryName'], 'System.Runtime')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][10]['name'], 'AssemblyTitleAttribute')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][10]['nameSpace'], 'System.Reflection')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][11]['libraryName'], 'System.Runtime')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][11]['name'], 'Object')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][11]['nameSpace'], 'System')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][12]['libraryName'], 'CustomLibrary')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][12]['name'], 'CustomClass1')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][12]['nameSpace'], 'CustomLibrary')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][13]['libraryName'], 'CustomLibrary')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][13]['name'], 'CustomClass2')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][13]['nameSpace'], 'CustomLibrary')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][14]['libraryName'], 'CustomLibrary')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][14]['name'], 'CustomSubClassA.CustomClass1')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][14]['nameSpace'], 'CustomLibrary')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][15]['libraryName'], 'CustomLibrary')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][15]['name'], 'CustomSubClassB.CustomClass2')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][15]['nameSpace'], 'CustomLibrary')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][16]['libraryName'], 'CustomLibrary')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][16]['name'], 'CustomSubSubClassX.CustomSubClassB.CustomClass2')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][16]['nameSpace'], 'CustomLibrary')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][17]['libraryName'], 'System.Console')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][17]['name'], 'Console')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['types'][17]['nameSpace'], 'System')

    def test_correctly_computes_typeref_hash(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['crc32'], '2553516c')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['md5'], '5742603226df6e720f055413ba924c2c')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['sha256'], 'c40e879174d85aaf426217ab5e39de04214245636550b82051a759d2946f15db')

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

        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['crc32'], 'bb390cc9')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['md5'], '93b7f964c87a94b07d1f6171f0b7d7c1')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['sha256'], '37a37a2d4cc651a9b6cf54da949cbb6c89fc1e6e9991628087741d51666c7f1b')

# VS nested class binary with cyclic referencing
class TestTypeRefHashNestedInfinite(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='typeref_hash_nested_infinite',
        args='--verbose --json'
    )

    def test_correctly_computes_typeref_hash(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['crc32'], '0c472e09')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['md5'], 'f8a9907a02d8a1bede13aa8dfc005269')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeRefTable']['sha256'], '9b327187b627a940bfe8645ca3df66500906f1822cfe08e279cbf23a7dd23660')
