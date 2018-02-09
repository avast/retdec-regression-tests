from regression_tests import *

class ImportDirectoryWithNoSizeTest(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='imports.ex'
	)

	def test_import_directory_with_no_size(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '2')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['index'], '0')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['name'], 'ExitProcess')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['libraryName'], 'kernel32.dll')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['address'], '0x4010c0')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['index'], '1')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['name'], 'printf')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['libraryName'], 'msvcrt.dll')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['address'], '0x4010c8')

class ImportDirectoryWithMinimalTerminatorTest(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='imports_badterm.ex'
	)

	def test_import_directory_with_minimal_terminator_size(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '2')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['index'], '0')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['name'], 'ExitProcess')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['libraryName'], 'kernel32.dll')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['address'], '0x4010e0')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['index'], '1')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['name'], 'printf')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['libraryName'], 'msvcrt.dll')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['address'], '0x4010e8')

class LowSectionOffsetAutoalignTest(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='duphead.ex'
	)

	def test_low_section_offset_autoalign(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['offset'], '0x1ff')
		self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '2')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['index'], '0')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['name'], 'ExitProcess')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['libraryName'], 'kernel32.dll')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['address'], '0x4014a0')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['index'], '1')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['name'], 'printf')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['libraryName'], 'msvcrt.dll')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['address'], '0x4014a8')

class ExportDirectoryWithNoSizeTest(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='dll.dll'
	)

	def test_export_directory_with_no_size(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output['exportTable']['numberOfExports'], '1')
		self.assertEqual(self.fileinfo.output['exportTable']['exports'][0]['index'], '0')
		self.assertEqual(self.fileinfo.output['exportTable']['exports'][0]['name'], 'export')
		self.assertEqual(self.fileinfo.output['exportTable']['exports'][0]['ordinalNumber'], '0')
		self.assertEqual(self.fileinfo.output['exportTable']['exports'][0]['address'], '0x1001024')

class ResourceDirectoryWithNoSizeTest(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='resource_icon.ex'
	)

	def test_resource_directory_with_no_size(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output['resourceTable']['numberOfResources'], '2')
		self.assertEqual(self.fileinfo.output['resourceTable']['resources'][0]['index'], '0')
		self.assertEqual(self.fileinfo.output['resourceTable']['resources'][0]['nameId'], '1576')
		self.assertEqual(self.fileinfo.output['resourceTable']['resources'][0]['type'], 'Icon')
		self.assertEqual(self.fileinfo.output['resourceTable']['resources'][0]['typeId'], '3')
		self.assertEqual(self.fileinfo.output['resourceTable']['resources'][0]['language'], 'Neutral')
		self.assertEqual(self.fileinfo.output['resourceTable']['resources'][0]['languageId'], '0')
		self.assertEqual(self.fileinfo.output['resourceTable']['resources'][0]['sublanguageId'], '0')
		self.assertEqual(self.fileinfo.output['resourceTable']['resources'][0]['offset'], '0x400')
		self.assertEqual(self.fileinfo.output['resourceTable']['resources'][0]['size'], '0x1628')
		self.assertEqual(self.fileinfo.output['resourceTable']['resources'][1]['index'], '1')
		self.assertEqual(self.fileinfo.output['resourceTable']['resources'][1]['nameId'], '788')
		self.assertEqual(self.fileinfo.output['resourceTable']['resources'][1]['type'], 'Icon Group')
		self.assertEqual(self.fileinfo.output['resourceTable']['resources'][1]['typeId'], '14')
		self.assertEqual(self.fileinfo.output['resourceTable']['resources'][1]['language'], 'Neutral')
		self.assertEqual(self.fileinfo.output['resourceTable']['resources'][1]['languageId'], '0')
		self.assertEqual(self.fileinfo.output['resourceTable']['resources'][1]['sublanguageId'], '0')
		self.assertEqual(self.fileinfo.output['resourceTable']['resources'][1]['offset'], '0x1a28')
		self.assertEqual(self.fileinfo.output['resourceTable']['resources'][1]['size'], '0x14')

class ImportsAtUnexpectedEndOfFileTest(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='imports_vterm.ex'
	)

	def test_imports_at_unexpected_end_of_file(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '2')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['index'], '0')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['name'], 'ExitProcess')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['libraryName'], 'kernel32.dll')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][0]['address'], '0x401080')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['index'], '1')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['name'], 'printf')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['libraryName'], 'msvcrt.dll')
		self.assertEqual(self.fileinfo.output['importTable']['imports'][1]['address'], '0x401088')

class MaximumValuesInHeaderTest(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='dllmaxvals.dll'
	)

	def test_maximum_values_in_header(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output['declaredNumberOfSections'], '1')
		self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '2')
		self.assertEqual(self.fileinfo.output['exportTable']['numberOfExports'], '1')
		self.assertEqual(self.fileinfo.output['relocationTables'][0]['numberOfRelocations'], '0')

class LessSectionsThanDeclaredTest(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='d_resource.dll'
	)

	def test_less_sections_than_declared(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output['declaredNumberOfSections'], '65535')
		self.assertEqual(self.fileinfo.output['sectionTable']['numberOfSections'], '8')
