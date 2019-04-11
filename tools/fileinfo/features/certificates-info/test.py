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
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "8fb47562286677514075bc38d1cfd2b73481d93cb3f9c23f9ac3e6414ef34a6f")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "582dc1d97a790ef04fe2567b1ec88c26b03bf6e99937cae6a0b50397ad20bbf8")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "8420dfbe376f414bf4c0a81e6936d24ccc03f304835b86c7a39142fca723a689")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][3]["sha256"], "0374881c9b74d31f28dc580b0f2b9d2b14a97ce31cbec2a05aeb377dcddcc2b0")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][4]["sha256"], "0625fee1a80d7b897a9712249c2f55ff391d6661dbd8b87f9be6f252d88ced95")

class Test2(Test):
	settings=TestSettings(
		tool='fileinfo',
		input='avgcfgex.ex',
		args='--json --verbose'
	)

	def test_certificates(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output["certificateTable"]["numberOfCertificates"], "5")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "3b0abe047d7e84f3bbd12b5e399bed55e4d7e9fcc3f629b8953a8c060ef6d746")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "0cfc19db681b014bfe3f23cb3a78b67208b4e3d8d7b6a7b1807f7cd6ecb2a54e")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "8420dfbe376f414bf4c0a81e6936d24ccc03f304835b86c7a39142fca723a689")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][3]["sha256"], "0374881c9b74d31f28dc580b0f2b9d2b14a97ce31cbec2a05aeb377dcddcc2b0")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][4]["sha256"], "0625fee1a80d7b897a9712249c2f55ff391d6661dbd8b87f9be6f252d88ced95")

class Test3(Test):
	settings=TestSettings(
		tool='fileinfo',
		input='c339b87d932b3f86c298b1745db1a28b1214fb7635ba3805851ef8699290f9b8',
		args='--json --verbose'
	)

	def test_certificates(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output["certificateTable"]["numberOfCertificates"], "5")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "fcb433d6d1afbec9e8f5447c2c0fa4ae7553986d5c2703be82524be608f35f61")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "53793cfc1b2b5096cc4edbec527abc5cbc20470c788162d9e54c370d51625f4a")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "c766a9bef2d4071c863a31aa4920e813b2d198608cb7b7cfe21143b836df09ea")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][3]["sha256"], "0374881c9b74d31f28dc580b0f2b9d2b14a97ce31cbec2a05aeb377dcddcc2b0")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][4]["sha256"], "0625fee1a80d7b897a9712249c2f55ff391d6661dbd8b87f9be6f252d88ced95")

class Test4(Test):
	settings=TestSettings(
		tool='fileinfo',
		input='c58e6118bbe12d2c56b2db014c4eb0d3fd32cde7bca1f32a2da8169be1301e23',
		args='--json --verbose'
	)

	def test_certificates(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output["certificateTable"]["numberOfCertificates"], "5")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "e2dba399be32992b74df8a86cfd9886c2304ccc19da8a9be2b87809da006379e")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "973a41276ffd01e027a2aad49e34c37846d3e976ff6a620b6712e33832041aa6")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "3a2fbe92891e57fe05d57087f48e730f17e5a5f53ef403d618e5b74d7a7e6ecb")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][3]["sha256"], "0374881c9b74d31f28dc580b0f2b9d2b14a97ce31cbec2a05aeb377dcddcc2b0")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][4]["sha256"], "0625fee1a80d7b897a9712249c2f55ff391d6661dbd8b87f9be6f252d88ced95")

class Test5(Test):
	settings=TestSettings(
		tool='fileinfo',
		input='crashreporter.ex',
		args='--json --verbose'
	)

	def test_certificates(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output["certificateTable"]["numberOfCertificates"], "5")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "1a73bf16814d061cf5930634fbbd8a55e53df2a556469c48fdf2623dfeeee8a8")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "51044706bd237b91b89b781337e6d62656c69f0fcffbe8e43741367948127862")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "3e9099b5015e8f486c00bcea9d111ee721faba355a89bcf1df69561e3dc6325c")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][3]["sha256"], "0374881c9b74d31f28dc580b0f2b9d2b14a97ce31cbec2a05aeb377dcddcc2b0")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][4]["sha256"], "0625fee1a80d7b897a9712249c2f55ff391d6661dbd8b87f9be6f252d88ced95")

class Test6(Test):
	settings=TestSettings(
		tool='fileinfo',
		input='f77acb4e1523b882f5307864345e5f7d20a657a7f40863bd7ae41d2521703fec',
		args='--json --verbose'
	)

	def test_certificates(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output["certificateTable"]["numberOfCertificates"], "5")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "fcb433d6d1afbec9e8f5447c2c0fa4ae7553986d5c2703be82524be608f35f61")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "53793cfc1b2b5096cc4edbec527abc5cbc20470c788162d9e54c370d51625f4a")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "c766a9bef2d4071c863a31aa4920e813b2d198608cb7b7cfe21143b836df09ea")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][3]["sha256"], "0374881c9b74d31f28dc580b0f2b9d2b14a97ce31cbec2a05aeb377dcddcc2b0")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][4]["sha256"], "0625fee1a80d7b897a9712249c2f55ff391d6661dbd8b87f9be6f252d88ced95")

class Test7(Test):
	settings=TestSettings(
		tool='fileinfo',
		input='msenvmnu.dll',
		args='--json --verbose'
	)

	def test_certificates(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output["certificateTable"]["numberOfCertificates"], "4")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "67c529ad57b2aedd4d248993324270c7064d4f6bdaaf70044d772d05c56001a4")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "9cbf22fae0dd53a7395556ce6154aa14a0d03360aa8c51cfea05d1fd8819e043")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "6413cbcf5c6ab255868033d4e701b579b2509a47c3c18b3199c140d20209c19d")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][3]["sha256"], "4f987bbe4e0d1dcf48fcefc9239ac6e62ee9df38cac2d32993b8533cd95c2e49")

class Test8(Test):
	settings=TestSettings(
		tool='fileinfo',
		input='PdfConv_32.dll',
		args='--json --verbose'
	)

	def test_certificates(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output["certificateTable"]["numberOfCertificates"], "4")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "bb70f99803db3f20919852d5af93bcad68f4f9109c8014676ee2cdd6ffdd1a8e")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "5e6d2f88f617dc8b809aee712445a41b3cde26af874a221a9dc98ea1dc68e3d5")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "4f32d5dc00f715250abcc486511e37f501a899deb3bf7ea8adbbd3aef1c412da")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][3]["sha256"], "12f0a1ddf83d265b205b4f3bca43b3fa89a748e9834ec24004774fd2fde34073")

class Test9(Test):
	settings=TestSettings(
		tool='fileinfo',
		input='thunderbird.ex',
		args='--json --verbose'
	)

	def test_certificates(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output["certificateTable"]["numberOfCertificates"], "5")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "1a73bf16814d061cf5930634fbbd8a55e53df2a556469c48fdf2623dfeeee8a8")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "51044706bd237b91b89b781337e6d62656c69f0fcffbe8e43741367948127862")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "3e9099b5015e8f486c00bcea9d111ee721faba355a89bcf1df69561e3dc6325c")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][3]["sha256"], "0374881c9b74d31f28dc580b0f2b9d2b14a97ce31cbec2a05aeb377dcddcc2b0")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][4]["sha256"], "0625fee1a80d7b897a9712249c2f55ff391d6661dbd8b87f9be6f252d88ced95")

class Test10(Test):
	settings=TestSettings(
		tool='fileinfo',
		input='VSTST-FileConverter.ex',
		args='--json --verbose'
	)

	def test_certificates(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output["certificateTable"]["numberOfCertificates"], "4")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "67c529ad57b2aedd4d248993324270c7064d4f6bdaaf70044d772d05c56001a4")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "9cbf22fae0dd53a7395556ce6154aa14a0d03360aa8c51cfea05d1fd8819e043")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "e43f82bc40029f17dbb516613d1e1a96ec2940ce76e0a9cd5f53ba50175a8766")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][3]["sha256"], "4f987bbe4e0d1dcf48fcefc9239ac6e62ee9df38cac2d32993b8533cd95c2e49")

class TestEscaping(Test):
	settings=TestSettings(
		tool='fileinfo',
		input='3708882e564ba289416f65cb4cb2b4de',
		args='--json --verbose'
	)

	def test_certificates(self):
		assert self.fileinfo.succeeded
		self.assertEqual(self.fileinfo.output["certificateTable"]["numberOfCertificates"], "4")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "9d5dc543a16e3b97aa12abb6a09c9393c1f6778e475d95c81607335d5d19af8b")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "0d34394100e961ce4318dba9b8dd38ebc25bb07aef78fda3fff632685549ba0f")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "0374881c9b74d31f28dc580b0f2b9d2b14a97ce31cbec2a05aeb377dcddcc2b0")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][3]["sha256"], "0625fee1a80d7b897a9712249c2f55ff391d6661dbd8b87f9be6f252d88ced95")
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
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "d271598adb52545b0094e806af9c4702d857b29d43d6896c523eef7758519153")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "09ed6e991fc3273d8fea317d339c02041861973549cfa6e1558f411f11211aa3")
		self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "c3846bf24b9e93ca64274c0ec67c1ecc5e024ffcacd2d74019350e81fe546ae4")
