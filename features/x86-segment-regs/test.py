from regression_tests import *

class TestBasic(Test):
    """Related to:
    #41:  https://github.com/avast-tl/retdec/issues/41
    #169: https://github.com/avast-tl/retdec/issues/169
    #391: https://github.com/avast-tl/retdec/pull/391
    """
    settings=TestSettings(
        input='Test.exe'
    )

    def test(self):
        main = self.out_c.funcs['main']
        assert main.calls('__readfsdword')
        assert self.out_c.contains('__readfsdword\(24\)')

class TestIssue376(Test):
    """Related to:
    #376: https://github.com/avast-tl/retdec/issues/376
    """
    settings=TestSettings(
        input='96BA2AE23FB2267D993BD018A5BDEEF062BED7C56DD6C37BDDC00EFA65085363',
        args='--select-functions=function_4169830c,TModuleEntry'
    )

    def test(self):
        f1 = self.out_c.funcs['function_4169830c']
        assert f1.calls('__readfsdword')
        assert f1.calls('__writefsdword')
        assert f1.calls('_40_FinalizeArray')
        assert f1.calls('_40_LStrClr')
        assert not f1.calls('abort')

        f2 = self.out_c.funcs['TModuleEntry']
        assert f2.calls('__readfsdword')
        assert f2.calls('__writefsdword')
        assert f2.calls('FileSearch')
        assert f2.calls('_40_LStrAsg')
        assert f2.calls('function_41697aa4')
        assert not f2.calls('abort')
