from regression_tests import *

class Test_ClickteamFusion(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '78da5a285061f19391758b66f6f82838cb7fbed0d758706335b6535d27dc81b7',
            '972b1ad01a914a7c70cbfa8b80ed1e4081d6460b98d388d2005598872bda49dc',
        ],
        args='--json'
    )

    def test_pe_packer(self):
        assert self.fileinfo.succeeded
        self.assertTrue(self.fileinfo.output['tools'][0]['name'] == 'Clickteam Fusion')

