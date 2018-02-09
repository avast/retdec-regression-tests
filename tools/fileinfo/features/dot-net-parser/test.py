from regression_tests import *

class Test1(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='0722edffa07cb4562dd1c5ca13e73a1769c192bab9f977bdc06c59125438f659'
    )

    def test_dotnet_info_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['dotnetInfo']['moduleVersionId'], '58c3c375-97de-49a2-b66a-fcdbac11b89d')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeLibId'], '934936d9-122c-4d8f-ada3-f37f498e412a')

class Test2(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='1b5f23409592d63e803c5966e2bbaaaa35f93bf87002c72f8b289e330ed59535'
    )

    def test_dotnet_info_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['dotnetInfo']['moduleVersionId'], '1caec189-fda7-4605-9ce9-4b87411459f7')

class Test3(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='1e2152fa2571cf849e92f69cce953e6edc858e0361d888ff5c7d22fa1d609f0f'
    )

    def test_dotnet_info_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['dotnetInfo']['moduleVersionId'], '800736b5-1a3e-46ba-bdc1-a84e67cfc330')

class Test4(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='23cd54a532e55e4f2de5c9277296e8485c65a69bc32af279372c448704f4850f'
    )

    def test_dotnet_info_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['dotnetInfo']['moduleVersionId'], '25089c43-f0e1-41e1-8a70-842fd39f2a32')

class Test5(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='338fed20bfa8f7f23feb7b0399b7105fcf3d985529dd88e86ed89620aa7e402f'
    )

    def test_dotnet_info_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['dotnetInfo']['moduleVersionId'], '7b88569a-4aae-4c6b-9b2b-7beee9223319')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeLibId'], 'c66c1da0-8ab1-4802-990d-36f49a1dfd1a')

class Test6(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='3ac594d4fdb8da1b61f772b3c551059f05cf32b10f77f5d86d9a04b639f2ed46'
    )

    def test_dotnet_info_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['dotnetInfo']['moduleVersionId'], '1f694a41-398f-47c2-8962-ff119d462e8b')

class Test7(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='45356051128baf68b6f16b420a60fc1149bdea619306ede80251a9acda410725'
    )

    def test_dotnet_info_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['dotnetInfo']['moduleVersionId'], '07f51536-ac3e-491d-8b11-bc6fcfae94c3')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeLibId'], 'f1e111b9-fb05-47ea-8e97-a6fdc2141789')

class Test8(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='7afe2a2067eeadcdd8a25fd7111afb865f4e3ea3df17244e10659d58cd17a8af'
    )

    def test_dotnet_info_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['dotnetInfo']['moduleVersionId'], '73d66795-8ac3-41c0-9448-c4d78bf30c88')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeLibId'], '671fa318-5f63-4ed2-9d8f-33b5f586401d')

class Test9(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='7fb46407e9e9649d59f7fb852eb9c87484401e5a8c219796a6f2d42d0f3515a2'
    )

    def test_dotnet_info_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['dotnetInfo']['moduleVersionId'], '03bcf251-0af6-4052-b006-d0d9dfa37fc1')

class Test10(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='90038806ec5b4e52d494fa28dcc50d5af03904aacd990dbceba7d2eb17f5273c'
    )

    def test_dotnet_info_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['dotnetInfo']['moduleVersionId'], '728fa6c8-0fc4-4a69-9305-df3cabad14e0')

class Test11(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='954bbeccdf6e6bf26c4c416f765ea25fb797d4c82f7ec532b464929db7083dd2'
    )

    def test_dotnet_info_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['dotnetInfo']['moduleVersionId'], '0eec1f37-2fa8-478b-989e-111773e6d8c9')

class Test12(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='983ec4ca259d216994f52e2208220985726bca357261a6741ac53745b22512e1'
    )

    def test_dotnet_info_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['dotnetInfo']['moduleVersionId'], '4d4bbbc3-69cd-4e98-b0de-95a1688b4335')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeLibId'], '975ed32c-4326-4801-8b46-ba49b3115cb4')

class Test13(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='a308f8a89b33903b12ead27fcb6308de332272cf0fada8f2dc6f7ee0a51c849a'
    )

    def test_dotnet_info_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['dotnetInfo']['moduleVersionId'], 'a3fb1dc8-6fad-4208-9efd-f993388c12e2')

class Test14(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='a411f2df9f9a403d7b77c1df644f3bbae9d7e3ea7d7b64619c1fec5649c420b6'
    )

    def test_dotnet_info_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['dotnetInfo']['moduleVersionId'], '20be3d5c-6579-41d0-80b9-0c5bc3a96c0a')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeLibId'], 'd71f54f2-2fff-47aa-8a17-bd7edd1af32b')

class Test15(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='a57305f45c2e03957077b63d28199f9946ab06a0796813924e9ab8d998408bcb'
    )

    def test_dotnet_info_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['dotnetInfo']['moduleVersionId'], 'f468dfdc-2ca7-4f26-8d01-1fdd4f2f47bb')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeLibId'], '81fe7d95-cef5-49ee-a0f4-2be368a8ac09')

class Test16(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='a5f7b787521430bc663cd7e3cbac8fe17cf53609071fc0b336dc5c8ead7a847c'
    )

    def test_dotnet_info_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['dotnetInfo']['moduleVersionId'], '3e4b4012-6a41-47a6-8a33-5886169c1251')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeLibId'], '2aa946ae-59cc-4400-b995-cd62540de905')

class Test17(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='b40d9ac76ae85b90edfb675fdd98a3d7ad42f6f39ae541f57834885a9f4da5ab'
    )

    def test_dotnet_info_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['dotnetInfo']['moduleVersionId'], 'a8666090-5620-4a96-b2cb-40798f794f6e')

class Test18(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='d1fae1542fb78276046b318692c9315a1ac3dc01b4b6f483762d638b99844878'
    )

    def test_dotnet_info_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['dotnetInfo']['moduleVersionId'], 'a3192f3c-ac2d-40d6-86c7-098d55af994f')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeLibId'], '6ef6f991-d2b6-416d-9905-dac375ab51af')

class TestDotnetTypes(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='regression_test_sample.ex'
    )

    def field_is_correct(self, obj, index, visibility, data_type, name, static=False):
        self.assertEqual(obj['fields'][index]['visibility'], visibility)
        self.assertEqual(obj['fields'][index]['type'], data_type)
        self.assertEqual(obj['fields'][index]['name'], name)
        self.assertEqual(obj['fields'][index]['static'], static)

    def property_is_correct(self, obj, index, visibility, data_type, name, static=False):
        self.assertEqual(obj['properties'][index]['visibility'], visibility)
        self.assertEqual(obj['properties'][index]['type'], data_type)
        self.assertEqual(obj['properties'][index]['name'], name)
        self.assertEqual(obj['properties'][index]['static'], static)

    def method_is_correct(self, obj, index, visibility, name, return_type=None, static=False, virtual=False, abstract=False, final=False, params=[], generic_params=None):
        self.assertEqual(obj['methods'][index]['visibility'], visibility)
        self.assertEqual(obj['methods'][index]['name'], name)
        if return_type is not None:
            self.assertEqual(obj['methods'][index]['returnType'], return_type)
        self.assertEqual(obj['methods'][index]['static'], static)
        self.assertEqual(obj['methods'][index]['virtual'], virtual)
        self.assertEqual(obj['methods'][index]['abstract'], abstract)
        self.assertEqual(obj['methods'][index]['final'], final)
        if generic_params is not None:
            self.assertEqual(obj['methods'][index]['genericParameters'], generic_params)
        if len(params) > 0:
            counter = 0
            for (param_type,param_name) in params:
                self.assertEqual(obj['methods'][index]['parameters'][counter]['type'], param_type)
                self.assertEqual(obj['methods'][index]['parameters'][counter]['name'], param_name)
                counter += 1
        else:
            self.assertEqual(obj['methods'][index]['parameters'], [])

    def test_dotnet_types_presented(self):
        assert self.fileinfo.succeeded

        enumClass = self.fileinfo.output['dotnetInfo']['classes'][0]
        self.assertEqual(enumClass['baseTypes'][0], 'System.Enum')
        self.assertEqual(enumClass['name'], 'MyEnum')
        self.assertEqual(enumClass['sealed'], True)
        self.assertEqual(enumClass['visibility'], 'public')
        self.field_is_correct(enumClass, 1, 'public', 'regression_test_sample.MyEnum', 'Value1', static=True)
        self.field_is_correct(enumClass, 2, 'public', 'regression_test_sample.MyEnum', 'Value2', static=True)
        self.field_is_correct(enumClass, 3, 'public', 'regression_test_sample.MyEnum', 'Value3', static=True)

        basicClass = self.fileinfo.output['dotnetInfo']['classes'][1]
        self.assertEqual(basicClass['baseTypes'], ['System.Object','regression_test_sample.BasicInterface<int>'])
        self.assertEqual(basicClass['name'], 'BasicClass')
        self.assertEqual(basicClass['genericParameters'], ['T'])
        self.assertEqual(basicClass['abstract'], False)
        self.field_is_correct(basicClass, 3, 'public', 'bool', 'boolField')
        self.field_is_correct(basicClass, 4, 'public', 'char', 'charField')
        self.field_is_correct(basicClass, 5, 'public', 'sbyte', 'sbyteField')
        self.field_is_correct(basicClass, 6, 'public', 'byte', 'byteField')
        self.field_is_correct(basicClass, 7, 'public', 'short', 'shortField')
        self.field_is_correct(basicClass, 8, 'public', 'ushort', 'ushortField')
        self.field_is_correct(basicClass, 9, 'public', 'int', 'intField')
        self.field_is_correct(basicClass, 10, 'public', 'uint', 'uintField')
        self.field_is_correct(basicClass, 11, 'public', 'long', 'longField')
        self.field_is_correct(basicClass, 12, 'public', 'ulong', 'ulongField')
        self.field_is_correct(basicClass, 13, 'public', 'float', 'floatField')
        self.field_is_correct(basicClass, 14, 'public', 'double', 'doubleField')
        self.field_is_correct(basicClass, 15, 'public', 'string', 'stringField')
        self.field_is_correct(basicClass, 16, 'public', 'regression_test_sample.BasicClass<T>', 'classField')
        self.field_is_correct(basicClass, 17, 'public', 'int[,]', 'arrayField')
        self.field_is_correct(basicClass, 18, 'public', 'System.Collections.Generic.List<int>', 'genericInstField')
        self.field_is_correct(basicClass, 19, 'public', 'IntPtr', 'intPtrField')
        self.field_is_correct(basicClass, 20, 'public', 'UIntPtr', 'uintPtrField')
        self.field_is_correct(basicClass, 21, 'public', 'object', 'objectField')
        self.field_is_correct(basicClass, 22, 'public', 'int[]', 'szArrayField')
        self.field_is_correct(basicClass, 23, 'public', 'volatile int', 'volatileIntField')
        self.field_is_correct(basicClass, 24, 'public', 'System.Type', 'typeField')
        self.field_is_correct(basicClass, 25, 'public', 'regression_test_sample.MyEnum', 'myEnumField')
        self.property_is_correct(basicClass, 0, 'public', 'string', 'StringProperty')
        self.property_is_correct(basicClass, 1, 'public', 'System.Collections.Generic.List<int>', 'ListIntProperty')
        self.property_is_correct(basicClass, 2, 'public', 'int', 'StaticIntProperty', static=True)
        self.method_is_correct(basicClass, 0, 'public', '.ctor')
        self.method_is_correct(basicClass, 1, 'private', '.cctor', static=True)
        self.method_is_correct(basicClass, 2, 'public', 'PublicMethod', return_type='void')
        self.method_is_correct(basicClass, 3, 'protected', 'ProtectedMethod', return_type='void')
        self.method_is_correct(basicClass, 4, 'private', 'PrivateMethod', return_type='void')
        self.method_is_correct(basicClass, 5, 'public', 'StaticMethod', return_type='void', static=True)
        self.method_is_correct(basicClass, 6, 'public', 'VirtualMethod', return_type='void', virtual=True)
        self.method_is_correct(basicClass, 7, 'public', 'MethodWithIntReturnType', return_type='int')
        self.method_is_correct(basicClass, 8, 'public', 'MethodWithIntReturnTypeAndParams', return_type='int',
                                params=[('int', 'x'), ('int', 'y'), ('int', 'z')])
        self.method_is_correct(basicClass, 9, 'public', 'MethodWithIntReturnTypeAndDiverseParams', return_type='int',
                                params=[('object', 'x'), ('float', 'y'), ('bool', 'z')])
        self.method_is_correct(basicClass, 10, 'public', 'MethodWithListIntReturnType', return_type='System.Collections.Generic.List<int>')
        self.method_is_correct(basicClass, 11, 'public', 'MethodWithListIntReturnTypeAndParam', return_type='System.Collections.Generic.List<int>',
                                params=[('System.Collections.Generic.List<int>', 'list')])
        self.method_is_correct(basicClass, 12, 'public', 'MethodWithGenericReturnType', return_type='U', generic_params=['U'])
        self.method_is_correct(basicClass, 13, 'public', 'MethodWithGenericParam', return_type='void', generic_params=['U'],
                                params=[('U', 'x')])
        self.method_is_correct(basicClass, 14, 'public', 'MethodWithMultipleGenericParams', return_type='void', generic_params=['T1','T2','T3'],
                                params=[('T3', 't3'), ('T2', 't2'), ('T1', 't1')])
        self.method_is_correct(basicClass, 15, 'public', 'MethodWithOutParameter', return_type='void',
                                params=[('int', 'inParam'), ('ref int', 'outParam')])
        self.method_is_correct(basicClass, 16, 'public', 'InterfaceMethod', return_type='int', final=True, virtual=True)

        interface = self.fileinfo.output['dotnetInfo']['classes'][2]
        self.assertEqual(interface['name'], 'BasicInterface')
        self.assertEqual(interface['genericParameters'], ['T'])
        self.assertEqual(interface['abstract'], True)
        self.assertEqual(interface['type'], 'interface')
        self.method_is_correct(interface, 0, 'public', 'InterfaceMethod', return_type='T', virtual=True, abstract=True)

        subClass = self.fileinfo.output['dotnetInfo']['classes'][4]
        self.assertEqual(subClass['baseTypes'], ['System.Object'])
        self.assertEqual(subClass['name'], 'Subclass')
        self.assertEqual(subClass['namespace'], 'regression_test_sample.BasicClass')
        self.assertEqual(subClass['genericParameters'], ['T'])
        self.field_is_correct(subClass, 0, 'public', 'int', 'randomSubclassField')
        self.method_is_correct(subClass, 0, 'public', '.ctor')

class TestEncTables(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='55385de7764267d00d4395b98eec8cf5'
    )

    def test_name_is_made_of_printable_characters(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['dotnetInfo']['classes'][1]['name'], 'CompressShell')
