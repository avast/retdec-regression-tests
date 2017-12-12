from regression_tests import *

class TestDecompileElfX86NotRebased(Test):
    settings = CriticalTestSettings(
        tool='idaplugin',
        input='hello-x86.o',
        args='--select 0x8000000'
    )

    def setUp(self):
        # Prevent the base class from checking that the decompilation
        # succeeded (we expect it to fail).
        pass

    def test_idaplugin_succeeded(self):
        self.assertEqual(self.idaplugin.succeeded, False)


class TestDecompileElfX86RebasedTo0x0(Test):
    settings = CriticalTestSettings(
        tool='idaplugin',
        input='hello-x86-rebase.o',
        idb='hello-x86-rebase.idb',
        args='--select 0x0'
    )

    # This is tested by setUp(), but we want to make it explicit here.
    def test_idaplugin_succeeded(self):
        self.assertEqual(self.idaplugin.succeeded, True)

class TestDecompileElfArm(Test):
    settings = CriticalTestSettings(
        tool='idaplugin',
        input='hello-arm.o',
        args='--select 0x0'
    )

    # This is tested by setUp(), but we want to make it explicit here.
    def test_idaplugin_succeeded(self):
        self.assertEqual(self.idaplugin.succeeded, True)

class TestDecompileElfMips(Test):
    settings = CriticalTestSettings(
        tool='idaplugin',
        input='hello-mips.o',
        args='--select 0x0'
    )

    # This is tested by setUp(), but we want to make it explicit here.
    def test_idaplugin_succeeded(self):
        self.assertEqual(self.idaplugin.succeeded, True)

class TestDecompileElfPpc(Test):
    settings = CriticalTestSettings(
        tool='idaplugin',
        input='hello-ppc.o',
        args='--select 0x0'
    )

    # This is tested by setUp(), but we want to make it explicit here.
    def test_idaplugin_succeeded(self):
        self.assertEqual(self.idaplugin.succeeded, True)

class TestDecompileCoffX86(Test):
    settings = CriticalTestSettings(
        tool='idaplugin',
        input='debug.obj',
        args='--select 0x0'
    )

    # This is tested by setUp(), but we want to make it explicit here.
    def test_idaplugin_succeeded(self):
        self.assertEqual(self.idaplugin.succeeded, True)

class TestDecompileCoffX86RebasedTo0x1000(Test):
    settings = CriticalTestSettings(
        tool='idaplugin',
        input='debug-rebase.obj',
        idb='debug-rebase.idb',
        args='--select 0x1000'
    )

    def setUp(self):
        # Prevent the base class from checking that the decompilation
        # succeeded (we expect it to fail).
        pass

    def test_idaplugin_succeeded(self):
        self.assertEqual(self.idaplugin.succeeded, False)
