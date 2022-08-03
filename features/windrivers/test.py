from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='413837291628d5d7288f885e4892af5c',
        args='-k'
    )

    def test_NdisMAllocateMapRegisters_call(self):
        assert self.out_c.funcs['function_10400'].calls('NdisMAllocateMapRegisters')
        assert self.out_c.contains('NdisMAllocateMapRegisters\(.*, .*, .*, 64, 1536\)')

    def test_some_driver_related_imports(self):
        assert self.out_c.contains(r'void KeStallExecutionProcessor\(int32_t a1\);')
        assert self.out_c.contains(r'int32_t NDIS_BUFFER_TO_SPAN_PAGES\(struct _MDL \* a1\);')
        assert self.out_c.contains(r'void NdisAcquireSpinLock\(struct _NDIS_SPIN_LOCK \* a1\);')
        assert self.out_c.contains(r'int32_t NdisMAllocateMapRegisters\(int32_t \* a1, int32_t a2, char a3, int32_t a4, int32_t a5\);')
        assert self.out_c.contains(r'int32_t NdisMRegisterIoPortRange\(int32_t \*\* a1, int32_t \* a2, int32_t a3, int32_t a4\);')
        assert self.out_c.contains(r'int32_t NdisWritePciSlotInformation\(int32_t \* a1, int32_t a2, int32_t a3, int32_t \* a4, int32_t a5\);')
        assert self.out_c.contains(r'int16_t READ_PORT_USHORT\(int16_t \* a1\);')
        assert self.out_c.contains(r'char RtlEqualUnicodeString\(struct _UNICODE_STRING \* a1, struct _UNICODE_STRING \* a2, char a3\);')
        assert self.out_c.contains(r'void WRITE_PORT_USHORT\(int16_t \* a1, int16_t a2\);')
