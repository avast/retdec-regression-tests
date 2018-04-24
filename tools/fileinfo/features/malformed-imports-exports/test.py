from regression_tests import *

# Not included because of the sample size (14.1 MB)
#class Test001(Test):
#	settings=TestSettings(
#		tool='fileinfo',
#		timeout=30,					# ~15.6 seconds on Intel Xeon E5-1620 v3 @3.50 GHz with 16 GB RAM (Windows 10 x64, Release, x64 build)
#		input=[
#			'4A2A008CF1AEE9BA49D8D1DAA22D8E868365ACE633823D464478239F27ED4F18.dat',
#		],
#		args='--json --verbose'
#	)

	def test_imports_exports(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output['declaredNumberOfDataDirectories'], '620')
		self.assertEqual(len(self.fileinfo.output['importTable']['imports']), 527798)


class Test002(Test):
	settings=TestSettings(
		tool='fileinfo',
		timeout=20,					# ~3.4 seconds on Intel Xeon E5-1620 v3 @3.50 GHz with 16 GB RAM (Windows 10 x64, Release, x64 build)
		input=[
			'7CE5BB5CA99B3570514AF03782545D41213A77A0F93D4AAC8269823A8D3A58EF.dat',
		],
		args='--json --verbose'
	)

	def test_imports_exports(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output['declaredNumberOfDataDirectories'], '16')
		self.assertEqual(len(self.fileinfo.output['importTable']['imports']), 28672)

# Not included because of the sample size (17.1 MB)
#class Test003(Test):
#	settings=TestSettings(
#		tool='fileinfo',
#		timeout=50,					# ~25.4 seconds on Intel Xeon E5-1620 v3 @3.50 GHz with 16 GB RAM (Windows 10 x64, Release, x64 build)
#		input=[
#			'CCE461B6EB23728BA3B8A97B9BE84C0FB9175DB31B9949E64144198AB3F702CE.dat',
#		],
#		args='--json --verbose'
#	)
#
#	def test_imports_exports(self):
#		assert self.fileinfo.succeeded
#		self.assertEqual(self.fileinfo.output['declaredNumberOfDataDirectories'], '16')
#		self.assertEqual(len(self.fileinfo.output['importTable']['imports']), 715060)
