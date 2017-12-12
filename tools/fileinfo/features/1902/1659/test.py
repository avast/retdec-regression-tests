from regression_tests import *


class TestMachODelphi16(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json',
        input=files_in_dir('macho-delphi-16')
    )

    def test_delphi_was_detected(self):
        assert self.fileinfo.succeeded
        # Compiler detection.
        self.assertEqual(
            self.fileinfo.output['tools'][0]['name'], 'Embarcadero Delphi'
        )
        self.assertEqual(self.fileinfo.output['tools'][0]['type'], 'compiler')
        self.assertEqual(
            self.fileinfo.output['tools'][1]['name'], 'Embarcadero Delphi'
        )
        self.assertEqual(self.fileinfo.output['tools'][1]['type'], 'compiler')
        self.assertEqual(self.fileinfo.output['tools'][1]['version'], '29.0')
        self.assertEqual(
            self.fileinfo.output['tools'][1]['additional'], 'XE8'
        )
        # Language detection.
        self.assertEqual(self.fileinfo.output['languages'][0]['name'], 'Delphi')


class TestMachODelphi18(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json',
        input=files_in_dir('macho-delphi-18')
    )

    def test_delphi_was_detected(self):
        assert self.fileinfo.succeeded
        # Compiler detection.
        self.assertEqual(
            self.fileinfo.output['tools'][0]['name'], 'Embarcadero Delphi'
        )
        self.assertEqual(self.fileinfo.output['tools'][0]['type'], 'compiler')
        self.assertEqual(
            self.fileinfo.output['tools'][1]['name'], 'Embarcadero Delphi'
        )
        self.assertEqual(self.fileinfo.output['tools'][1]['type'], 'compiler')
        self.assertEqual(self.fileinfo.output['tools'][1]['version'], '31.0')
        self.assertEqual(
            self.fileinfo.output['tools'][1]['additional'], '10.1 Berlin'
        )
        # Language detection.
        self.assertEqual(self.fileinfo.output['languages'][0]['name'], 'Delphi')


class TestDelphi19(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json',
        input=files_in_dir('delphi-19')
    )

    def test_delphi_was_detected(self):
        assert self.fileinfo.succeeded
        # Compiler detection.
        self.assertEqual(
            self.fileinfo.output['tools'][0]['name'], 'Embarcadero Delphi'
        )
        self.assertEqual(self.fileinfo.output['tools'][0]['type'], 'compiler')
        self.assertEqual(self.fileinfo.output['tools'][0]['version'], '32.0')
        self.assertEqual(
            self.fileinfo.output['tools'][0]['additional'], '10.2 Tokyo'
        )
        # Language detection.
        self.assertEqual(self.fileinfo.output['languages'][0]['name'], 'Delphi')


class TestDelphiNoComment(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json',
        input='no-comment.exe'
    )

    def test_delphi_was_detected(self):
        assert self.fileinfo.succeeded
        # Compiler detection.
        self.assertEqual(
            self.fileinfo.output['tools'][0]['name'], 'Embarcadero Delphi'
        )
        self.assertEqual(self.fileinfo.output['tools'][0]['type'], 'compiler')
        self.assertEqual(self.fileinfo.output['tools'][0]['version'], '26.0+')
        self.assertEqual(
            self.fileinfo.output['tools'][0]['additional'], 'XE5 or higher'
        )
         # Language detection.
        self.assertEqual(self.fileinfo.output['languages'][0]['name'], 'Delphi')