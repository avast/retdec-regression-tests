from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=[
            'dhsetup.exe_',
            'multires.exe_'
        ],
        args='--json'
    )

    def test_correctly_analyzes_input_file(self):
        create_install_recognized = False

        self.assertTrue(self.fileinfo.succeeded)
        for tool in self.fileinfo.output['tools']:
            if tool['type'] == 'installer' and tool['name'] == 'GenteeInstaller':
                create_install_recognized = True
        self.assertTrue(create_install_recognized)
