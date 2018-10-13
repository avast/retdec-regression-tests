from regression_tests import *

class Test(Test):

    settings = TestSettings(
        input='adoughbee.ex',
        pdb='adoughbee.pdb',
        args='--select-functions RegisterSoftware --select-decode-only'
    )

    def test_for_selected_function(self):
        assert self.out_c.has_just_funcs('RegisterSoftware')
