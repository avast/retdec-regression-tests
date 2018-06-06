from regression_tests import *

class TestMachoUniversalDecomp(Test):
    settings = TestSettings(
        input= [ 'macho_fact_uni', 'macho_fact_uni_rev' ]
    )

    def test_has_main_function(self):
        assert self.out_c.has_func( 'main' )

    def test_decompilation_has_funcs(self):
        assert self.out_c.has_func( '_factorial' )

    def test_decompilation_calls(self):
        assert self.out_c.funcs['_factorial'].calls( '_factorial' )
        assert self.out_c.funcs['main'].calls( '_scanf', '_factorial', '_printf' )
