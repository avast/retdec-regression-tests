from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='40ecc99e2128ddbfe332e85c62bee3bb'
    )

    def test_c(self):
        f = self.out_c.funcs['vgFlush']
        assert f.calls('NCGSYS_DeviceIOControl')

        f = self.out_c.funcs['vgFinish']
        assert f.calls('NCGSYS_DeviceIOControl')

        f = self.out_c.funcs['vgTranslate']
        assert f.calls('NCGSYS_DeviceIOControl')

        f = self.out_c.funcs['vgAppendPath']
        assert f.calls('NCGSYS_DeviceIOControl')

        f = self.out_c.funcs['vgCopyImage']
        assert f.calls('NCGSYS_DeviceIOControl')

        f = self.out_c.funcs['vgQueryResourceRE']
        assert f.calls('NCGSYS_DeviceIOControl')

        f = self.out_c.funcs['vgGetProcAddress']
        assert f.calls('strcmp')
