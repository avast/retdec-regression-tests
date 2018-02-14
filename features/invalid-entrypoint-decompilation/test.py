from regression_tests import *

class TestKernel(Test):
    settings=TestSettings(
        input='kernel',
        args='-k'
    )

    def test_contains_functions(self):
        assert self.decompiler.succeeded
        assert self.out_c.has_funcs('binit', 'balloc', 'dirlookup', 'kalloc',
            'kfree', 'scheduler', 'sys_fork')
        
class TestApplication(Test):
    settings=TestSettings(
        input='application.axf'
    )

    def test_contains_functions(self):
        assert self.decompiler.succeeded

        assert self.out_c.has_funcs('console_init', 'uxListRemove', 'RtlConsolInitRam', 'rtw_spinlock_init', 'vListInitialise', 'vPortExitCritical', 'vTaskSuspendAll', 'xTaskGenericCreate')
