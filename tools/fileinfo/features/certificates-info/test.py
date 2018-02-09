from regression_tests import *

class Test1(Test):
	settings=TestSettings(
		tool='fileinfo',
		input='8b280f2b7788520de214fa8d6ea32a30ebb2a51038381448939530fd0f7dfc16',
		args='--json --verbose'
	)

	def test_certificates(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output["certificateTable"]["numberOfCertificates"], "5")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "8FB47562286677514075BC38D1CFD2B73481D93CB3F9C23F9AC3E6414EF34A6F")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "582DC1D97A790EF04FE2567B1EC88C26B03BF6E99937CAE6A0B50397AD20BBF8")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "8420DFBE376F414BF4C0A81E6936D24CCC03F304835B86C7A39142FCA723A689")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][3]["sha256"], "0374881C9B74D31F28DC580B0F2B9D2B14A97CE31CBEC2A05AEB377DCDDCC2B0")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][4]["sha256"], "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95")

class Test2(Test):
	settings=TestSettings(
		tool='fileinfo',
		input='avgcfgex.ex',
		args='--json --verbose'
	)

	def test_certificates(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output["certificateTable"]["numberOfCertificates"], "5")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "3B0ABE047D7E84F3BBD12B5E399BED55E4D7E9FCC3F629B8953A8C060EF6D746")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "0CFC19DB681B014BFE3F23CB3A78B67208B4E3D8D7B6A7B1807F7CD6ECB2A54E")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "8420DFBE376F414BF4C0A81E6936D24CCC03F304835B86C7A39142FCA723A689")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][3]["sha256"], "0374881C9B74D31F28DC580B0F2B9D2B14A97CE31CBEC2A05AEB377DCDDCC2B0")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][4]["sha256"], "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95")

class Test3(Test):
	settings=TestSettings(
		tool='fileinfo',
		input='c339b87d932b3f86c298b1745db1a28b1214fb7635ba3805851ef8699290f9b8',
		args='--json --verbose'
	)

	def test_certificates(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output["certificateTable"]["numberOfCertificates"], "5")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "FCB433D6D1AFBEC9E8F5447C2C0FA4AE7553986D5C2703BE82524BE608F35F61")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "53793CFC1B2B5096CC4EDBEC527ABC5CBC20470C788162D9E54C370D51625F4A")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "C766A9BEF2D4071C863A31AA4920E813B2D198608CB7B7CFE21143B836DF09EA")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][3]["sha256"], "0374881C9B74D31F28DC580B0F2B9D2B14A97CE31CBEC2A05AEB377DCDDCC2B0")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][4]["sha256"], "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95")

class Test4(Test):
	settings=TestSettings(
		tool='fileinfo',
		input='c58e6118bbe12d2c56b2db014c4eb0d3fd32cde7bca1f32a2da8169be1301e23',
		args='--json --verbose'
	)

	def test_certificates(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output["certificateTable"]["numberOfCertificates"], "5")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "E2DBA399BE32992B74DF8A86CFD9886C2304CCC19DA8A9BE2B87809DA006379E")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "973A41276FFD01E027A2AAD49E34C37846D3E976FF6A620B6712E33832041AA6")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "3A2FBE92891E57FE05D57087F48E730F17E5A5F53EF403D618E5B74D7A7E6ECB")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][3]["sha256"], "0374881C9B74D31F28DC580B0F2B9D2B14A97CE31CBEC2A05AEB377DCDDCC2B0")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][4]["sha256"], "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95")

class Test5(Test):
	settings=TestSettings(
		tool='fileinfo',
		input='crashreporter.ex',
		args='--json --verbose'
	)

	def test_certificates(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output["certificateTable"]["numberOfCertificates"], "5")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "1A73BF16814D061CF5930634FBBD8A55E53DF2A556469C48FDF2623DFEEEE8A8")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "51044706BD237B91B89B781337E6D62656C69F0FCFFBE8E43741367948127862")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "3E9099B5015E8F486C00BCEA9D111EE721FABA355A89BCF1DF69561E3DC6325C")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][3]["sha256"], "0374881C9B74D31F28DC580B0F2B9D2B14A97CE31CBEC2A05AEB377DCDDCC2B0")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][4]["sha256"], "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95")

class Test6(Test):
	settings=TestSettings(
		tool='fileinfo',
		input='f77acb4e1523b882f5307864345e5f7d20a657a7f40863bd7ae41d2521703fec',
		args='--json --verbose'
	)

	def test_certificates(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output["certificateTable"]["numberOfCertificates"], "5")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "FCB433D6D1AFBEC9E8F5447C2C0FA4AE7553986D5C2703BE82524BE608F35F61")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "53793CFC1B2B5096CC4EDBEC527ABC5CBC20470C788162D9E54C370D51625F4A")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "C766A9BEF2D4071C863A31AA4920E813B2D198608CB7B7CFE21143B836DF09EA")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][3]["sha256"], "0374881C9B74D31F28DC580B0F2B9D2B14A97CE31CBEC2A05AEB377DCDDCC2B0")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][4]["sha256"], "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95")

class Test7(Test):
	settings=TestSettings(
		tool='fileinfo',
		input='msenvmnu.dll',
		args='--json --verbose'
	)

	def test_certificates(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output["certificateTable"]["numberOfCertificates"], "4")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "67C529AD57B2AEDD4D248993324270C7064D4F6BDAAF70044D772D05C56001A4")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "9CBF22FAE0DD53A7395556CE6154AA14A0D03360AA8C51CFEA05D1FD8819E043")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "6413CBCF5C6AB255868033D4E701B579B2509A47C3C18B3199C140D20209C19D")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][3]["sha256"], "4F987BBE4E0D1DCF48FCEFC9239AC6E62EE9DF38CAC2D32993B8533CD95C2E49")

class Test8(Test):
	settings=TestSettings(
		tool='fileinfo',
		input='PdfConv_32.dll',
		args='--json --verbose'
	)

	def test_certificates(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output["certificateTable"]["numberOfCertificates"], "4")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "BB70F99803DB3F20919852D5AF93BCAD68F4F9109C8014676EE2CDD6FFDD1A8E")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "5E6D2F88F617DC8B809AEE712445A41B3CDE26AF874A221A9DC98EA1DC68E3D5")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "4F32D5DC00F715250ABCC486511E37F501A899DEB3BF7EA8ADBBD3AEF1C412DA")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][3]["sha256"], "12F0A1DDF83D265B205B4F3BCA43B3FA89A748E9834EC24004774FD2FDE34073")

class Test9(Test):
	settings=TestSettings(
		tool='fileinfo',
		input='thunderbird.ex',
		args='--json --verbose'
	)

	def test_certificates(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output["certificateTable"]["numberOfCertificates"], "5")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "1A73BF16814D061CF5930634FBBD8A55E53DF2A556469C48FDF2623DFEEEE8A8")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "51044706BD237B91B89B781337E6D62656C69F0FCFFBE8E43741367948127862")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "3E9099B5015E8F486C00BCEA9D111EE721FABA355A89BCF1DF69561E3DC6325C")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][3]["sha256"], "0374881C9B74D31F28DC580B0F2B9D2B14A97CE31CBEC2A05AEB377DCDDCC2B0")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][4]["sha256"], "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95")

class Test10(Test):
	settings=TestSettings(
		tool='fileinfo',
		input='VSTST-FileConverter.ex',
		args='--json --verbose'
	)

	def test_certificates(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output["certificateTable"]["numberOfCertificates"], "4")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "67C529AD57B2AEDD4D248993324270C7064D4F6BDAAF70044D772D05C56001A4")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "9CBF22FAE0DD53A7395556CE6154AA14A0D03360AA8C51CFEA05D1FD8819E043")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "E43F82BC40029F17DBB516613D1E1A96EC2940CE76E0A9CD5F53BA50175A8766")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][3]["sha256"], "4F987BBE4E0D1DCF48FCEFC9239AC6E62EE9DF38CAC2D32993B8533CD95C2E49")

class TestEscaping(Test):
	settings=TestSettings(
		tool='fileinfo',
		input='3708882e564ba289416f65cb4cb2b4de',
		args='--json --verbose'
	)

	def test_certificates(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output["certificateTable"]["numberOfCertificates"], "4")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "9D5DC543A16E3B97AA12ABB6A09C9393C1F6778E475D95C81607335D5D19AF8B")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "0D34394100E961CE4318DBA9B8DD38EBC25BB07AEF78FDA3FFF632685549BA0F")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "0374881C9B74D31F28DC580B0F2B9D2B14A97CE31CBEC2A05AEB377DCDDCC2B0")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][3]["sha256"], "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["attributes"]["subject"]["locality"], R"M\xfcnchen")
		
class Test11(Test):
	settings=TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='x86-pe-ff6717faf307cdc5ba2d07e320cb8e33'
	)

	def test_certificates(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output["certificateTable"]["numberOfCertificates"], "3")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "D271598ADB52545B0094E806AF9C4702D857B29D43D6896C523EEF7758519153")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "09ED6E991FC3273D8FEA317D339C02041861973549CFA6E1558F411F11211AA3")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "C3846BF24B9E93CA64274C0EC67C1ECC5E024FFCACD2D74019350E81FE546AE4")
