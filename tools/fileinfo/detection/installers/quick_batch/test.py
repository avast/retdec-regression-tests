from regression_tests import *
import os

class Test_Version_105(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=files_in_dir('inputs'),
        args='--json'
    )
        
    version_map = {
        'sample-batch-file-1.0.3.2.exe_'       : '1.0.0.0 - 1.0.5.5',
        'sample-batch-file-1.0.5.5.exe_'       : '1.0.0.0 - 1.0.5.5',
        'sample-batch-file-1.0.6.3.exe_'       : '1.0.6.0+',
        'sample-batch-file-2.0.5.1.exe_'       : '2.0.0.0 - 2.1.7.0',
        'sample-batch-file-2.0.7.1.exe_'       : '2.0.0.0 - 2.1.7.0',
        'sample-batch-file-2.1.5.0.exe_'       : '2.0.0.0 - 2.1.7.0',
        'sample-batch-file-2.1.6.0-2.exe_'     : '2.0.0.0 - 2.1.7.0',
        'sample-batch-file-2.1.6.0.exe_'       : '2.0.0.0 - 2.1.7.0',
        'sample-batch-file-2.1.7.0.exe_'       : '2.0.0.0 - 2.1.7.0',
        'sample-batch-file-3.0.0.4.exe_'       : '3.0.0.0 - 3.1.6.0',
        'sample-batch-file-3.0.1.0.exe_'       : '3.0.0.0 - 3.1.6.0',
        'sample-batch-file-3.1.5.0.exe_'       : '3.0.0.0 - 3.1.6.0',
        'sample-batch-file-3.1.6.0.exe_'       : '3.0.0.0 - 3.1.6.0',
        'sample-batch-file-3.2.0.0-2.exe_'     : '3.2.0.0',
        'sample-batch-file-3.2.0.0.exe_'       : '3.2.0.0',
        'sample-batch-file-3.2.1.0.exe_'       : '3.2.1.0+',
        'sample-batch-file-3.2.9.0.exe_'       : '3.2.1.0+',
        'sample-batch-file-3.6.1.0.exe_'       : '3.2.1.0+',
        'sample-batch-file-3.7.1.0.exe_'       : '3.2.1.0+',
        'sample-batch-file-4.0.0.0-32bit.exe_' : '4.0.0.0+',
        'sample-batch-file-4.0.0.0-64bit.exe_' : '4.0.0.0+',
        'sample-batch-file-4.0.1.0-32bit.exe_' : '4.0.0.0+',
        'sample-batch-file-4.0.1.0-64bit.exe_' : '4.0.0.0+',
        'sample-batch-file-4.1.0.0-32bit.exe_' : '4.0.0.0+',
        'sample-batch-file-4.1.0.0-64bit.exe_' : '4.0.0.0+',
        'sample-batch-file-4.1.5.0-32bit.exe_' : '4.0.0.0+',
        'sample-batch-file-4.1.5.0-64bit.exe_' : '4.0.0.0+',
        'sample-batch-file-4.2.0.0-32bit.exe_' : '4.0.0.0+',
        'sample-batch-file-4.2.0.0-64bit.exe_' : '4.0.0.0+',
        'sample-batch-file-4.3.0.0-32bit.exe_' : '4.0.0.0+',
        'sample-batch-file-4.3.0.0-64bit.exe_' : '4.0.0.0+',
        'sample-batch-file-5.0.6.6-32bit.exe_' : '5.0.0.0+',
        'sample-batch-file-5.0.6.6-64bit.exe_' : '5.0.0.0+',
        'sample-batch-file-5.1.0.0-32bit.exe_' : '5.0.0.0+',
        'sample-batch-file-5.1.0.0-64bit.exe_' : '5.0.0.0+',
        'sample-batch-file-5.2.0.0-32bit.exe_' : '5.0.0.0+',
        'sample-batch-file-5.2.0.0-64bit.exe_' : '5.0.0.0+',
        'sample-batch-file-5.3.0.0-32bit.exe_' : '5.0.0.0+',
        'sample-batch-file-5.3.0.0-64bit.exe_' : '5.0.0.0+',
        'sample-batch-file-5.3.1.0-32bit.exe_' : '5.0.0.0+',
        'sample-batch-file-5.3.1.0-64bit.exe_' : '5.0.0.0+',
        'sample-batch-file-5.3.1.1-32bit.exe_' : '5.0.0.0+',
        'sample-batch-file-5.3.1.1-64bit.exe_' : '5.0.0.0+'
    }

    def test_correctly_analyzes_input_file(self):

        source_file_name = self.fileinfo.output['inputFile']
        source_base_name = os.path.split(source_file_name)[1]
        if source_base_name in self.version_map:
            self.assertTrue(self.fileinfo.succeeded)
            desired_tool_recognized = False
            quickbatch_version = self.version_map[source_base_name]
            for tool in self.fileinfo.output['tools']:
                if tool['type'] == 'installer' and tool['name'] == 'Quick Batch File Compiler' and tool['version'] == quickbatch_version:
                    desired_tool_recognized = True
                    break
            self.assertTrue(desired_tool_recognized)
