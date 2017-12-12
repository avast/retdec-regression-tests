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
        assert self.out_c.has_comment_matching(r'.*VOID KeStallExecutionProcessor\(.*MicroSeconds\);')
        assert self.out_c.has_comment_matching(r'.*ULONG NDIS_BUFFER_TO_SPAN_PAGES\(.*PNDIS_BUFFER Buffer\);')
        assert self.out_c.has_comment_matching(r'.*VOID NdisAcquireSpinLock\(.*PNDIS_SPIN_LOCK SpinLock\);')
        assert self.out_c.has_comment_matching(r'.*NDIS_STATUS NdisMAllocateMapRegisters\(.*MiniportAdapterHandle, .*DmaChannel, .*DmaSize, .*BaseMapRegistersNeeded, .*MaximumPhysicalMapping\);')
        assert self.out_c.has_comment_matching(r'.*NDIS_STATUS NdisMRegisterIoPortRange\(.*PortOffset, .*MiniportAdapterHandle, .*InitialPort, .*NumberOfPorts\);')
        assert self.out_c.has_comment_matching(r'.*ULONG NdisWritePciSlotInformation\(.*NdisAdapterHandle, .*SlotNumber, .*Offset, .*Buffer, .*Length\);')
        assert self.out_c.has_comment_matching(r'.*UCHAR READ_PORT_UCHAR\(_In_ PUCHAR Port\);')
        assert self.out_c.has_comment_matching(r'.*BOOLEAN RtlEqualUnicodeString\(.*String1, .*String2, .*CaseInSensitive\);')
        assert self.out_c.has_comment_matching(r'.*VOID WRITE_PORT_USHORT\(.*PUSHORT Port, .*Value\);')
