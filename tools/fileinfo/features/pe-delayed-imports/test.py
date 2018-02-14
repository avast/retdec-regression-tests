from regression_tests import *

class Test(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--verbose --json',
		input='dropped.ex'
	)

	def test_delayled_imports_detection(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '80')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][72]['index'], '72')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][73]['index'], '73')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][74]['index'], '74')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][75]['index'], '75')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][76]['index'], '76')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][77]['index'], '77')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][78]['index'], '78')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][79]['index'], '79')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][72]['name'], 'GetInputState')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][73]['name'], 'wsprintfA')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][74]['name'], 'PostThreadMessageA')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][75]['name'], 'GetMessageA')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][76]['name'], 'GetDesktopWindow')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][77]['name'], 'RegOpenKeyExA')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][78]['name'], 'RegCloseKey')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][79]['name'], 'RegQueryValueExA')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][72]['libraryName'], 'USER32.dll')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][73]['libraryName'], 'USER32.dll')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][74]['libraryName'], 'USER32.dll')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][75]['libraryName'], 'USER32.dll')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][76]['libraryName'], 'USER32.dll')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][77]['libraryName'], 'ADVAPI32.dll')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][78]['libraryName'], 'ADVAPI32.dll')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][79]['libraryName'], 'ADVAPI32.dll')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][72]['address'], '0x4020ae')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][73]['address'], '0x402078')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][74]['address'], '0x40209c')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][75]['address'], '0x40208a')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][76]['address'], '0x402058')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][77]['address'], '0x4020f2')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][78]['address'], '0x4020c0')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][79]['address'], '0x4020e0')
