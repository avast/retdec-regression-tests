from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=[
            'PrimediusFirewallLite.exe_',
            'SETUP.EXE_',
            'yahoo_messenger_install.exe_'
        ],
        args='--json'
    )

    def test_correctly_analyzes_input_file(self):
        installer_recognized = False

        self.assertTrue(self.fileinfo.succeeded)
        for tool in self.fileinfo.output['tools']:
            if tool['type'] == 'installer' and tool['name'] == 'Wise Installer':
                installer_recognized = True
        self.assertTrue(installer_recognized)
