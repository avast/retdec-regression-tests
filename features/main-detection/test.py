from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input=[
            'ack_msvc17-O1_ack_0x401024.exe',
            'ackerman_msvs2005_O1_0x4010a4.exe',
            'ackerman_msvs2005_debug_ZI_0x411620.exe',
            'ackerman_msvs2008_debug_0x411630.exe',
            'ackerman_msvs2010_O1_0x4010a9.exe',
            'ackermann_msvc16-O2_0x4010e0.exe',
            'dijkstra_msvs2005_debug_Zi_Ox_0x4012f0.exe',
            'dijkstra_msvs2008_0x4012c0.exe',
            'dijkstra_msvs2008_dx_0x4012c0.exe',
            'dijkstra_msvs2010_debug_Zi-Ox_0x4012f0.exe',
            'fib_msvc16-Od_0x401040.exe',
            'fibo_msvc16-Od-debug_0x401020.exe',
            'fibo_msvc17-O2_0x401030.exe',
            'gcd_msvc17-O1-debug_0x4010a5.exe',
            'izp_proj1_msvc17-Ox_0x4013d0.exe',
            'izu_a_star_msvs2010_debug_ZI_0x412380.exe',
            'switch_msvs2012-ox-debug_0x4012e0.exe'
        ]
    )

    def test_check_for_main(self):
        assert self.out_c.has_func( 'main' )
