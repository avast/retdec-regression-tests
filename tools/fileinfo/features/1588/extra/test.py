from regression_tests import *

class TestNoSegfault(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=files_in_dir('no-segfault-inputs')
    )

    def test_has_dotnet_info(self):
        assert self.fileinfo.succeeded
        assert 'dotnetInfo' in self.fileinfo.output

class TestNoTypeLibId(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=files_in_dir('no-typelib-id-inputs')
    )

    def test_no_typelib_id(self):
        assert self.fileinfo.succeeded
        assert 'dotnetInfo' in self.fileinfo.output
        assert 'typeLibId' not in self.fileinfo.output['dotnetInfo']

class TestTypeLibId(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=files_in_dir('typelib-id-inputs')
    )

    def test_has_typelib_id(self):
        assert self.fileinfo.succeeded
        assert 'dotnetInfo' in self.fileinfo.output
        self.assertEqual(self.fileinfo.output['dotnetInfo']['typeLibId'], '6d932415-c126-4832-8b79-3698b5231e00')

class TestHasSomeClasses(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=files_in_dir('some-classes')
    )

    def test_has_some_classes(self):
        assert self.fileinfo.succeeded
        assert 'dotnetInfo' in self.fileinfo.output
        assert 'classes' in self.fileinfo.output['dotnetInfo']

class TestHasInvalidClasses(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=files_in_dir('invalid-classes')
    )

    def test_has_invalid_classes(self):
        assert self.fileinfo.succeeded
        assert 'dotnetInfo' in self.fileinfo.output
        assert 'classes' not in self.fileinfo.output['dotnetInfo']

class TestFnPtrType(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='fnptr-type/35009ea91d696863f3c1f686a6ff7264'
    )

    def check_field(self, obj, index, name, data_type):
        self.assertEqual(obj['fields'][index]['name'], name)
        self.assertEqual(obj['fields'][index]['type'], data_type)

    def test_has_fnptr_types(self):
        assert self.fileinfo.succeeded
        c = self.fileinfo.output['dotnetInfo']['classes'][0]
        self.assertEqual(c['name'], 'SNINativeMethodWrapper')
        self.check_field(c, 1, 'SNICheckConnectionPtr', 'FnPtr<uint(Ptr<SNI_Conn>)>')
        self.check_field(c, 2, 'SNIWriteAsyncWrapperPtr', 'FnPtr<uint(Ptr<SNI_ConnWrapper>, Ptr<SNI_Packet>)>')
        self.check_field(c, 3, 'SNIReadAsyncWrapperPtr', 'FnPtr<uint(Ptr<SNI_ConnWrapper>, Ptr<Ptr<SNI_Packet>>)>')
        self.check_field(c, 4, 'SNIPacketAllocatePtr', 'FnPtr<Ptr<SNI_Packet>(Ptr<SNI_Conn>, SNI_Packet_IOType)>')
        self.check_field(c, 5, 'SNIPacketReleasePtr', 'FnPtr<void(Ptr<SNI_Packet>)>')
        self.check_field(c, 6, 'SNIPacketResetPtr', 'FnPtr<void(Ptr<SNI_Conn>, SNI_Packet_IOType, Ptr<SNI_Packet>, ConsumerNum)>')
        self.check_field(c, 7, 'SNIPacketGetDataWrapperPtr', 'FnPtr<uint(Ptr<SNI_Packet>, Ptr<byte>, uint, Ptr<uint>)>')
        self.check_field(c, 8, 'SNIPacketSetDataPtr', 'FnPtr<void(Ptr<SNI_Packet>, Ptr<byte>, uint)>')
