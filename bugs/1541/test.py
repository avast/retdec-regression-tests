from regression_tests import *

CommonSettings = TestSettings(
    args='--backend-no-opts'
)

class CommonTest(Test):
    def test(self):
        assert self.decomp.succeeded

class AlarmManagerTest(CommonTest):
    settings=TestSettings.from_settings(CommonSettings,
        input='AlarmManager.exe',
        pdb='AlarmManager.pdb'
    )

class B2bTest(CommonTest):
    settings=TestSettings.from_settings(CommonSettings,
        input='b2b.exe',
        pdb='b2b.pdb'
    )

class PMSTransferUtilityTest(CommonTest):
    settings=TestSettings.from_settings(CommonSettings,
        input='PMSTransferUtility.exe',
        pdb='PMSTransferUtility.pdb'
    )

class DwarfTest(CommonTest):
    settings=TestSettings.from_settings(CommonSettings,
        input=['client', 'letsencrypt.live.bin'],
        args='--select-functions=syscall.init --select-decode-only'
    )
