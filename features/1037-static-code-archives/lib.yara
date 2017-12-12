private rule architecture {
	meta:
		bitWidth = 32
		endianness = "little"
		architecture = "x86"
	condition:
		true
}

rule file_0_0_0 {
	meta:
		name = "ackermann"
		size = 92
		refs = "0027 ackermann"
	strings:
		$1 = { 55 89 E5 83 EC 08 83 7D 08 00 75 08 8B 45 0C 83 C0 01 EB 46 83 7D 0C 00 75 16 8B 45 08 83 E8 01 83 EC 08 6A 01 50 E8 ?? ?? ?? ?? 83 C4 10 EB 2A 8B 45 0C 83 E8 01 83 EC 08 50 FF 75 08 E8 ?? ?? ?? ?? 83 C4 10 89 C2 8B 45 08 83 E8 01 83 EC 08 52 50 E8 ?? ?? ?? ?? 83 C4 10 C9 C3 }
	condition:
		$1
}

rule file_0_1_0 {
	meta:
		name = "factorial"
		size = 43
		refs = "001e factorial"
	strings:
		$1 = { 55 89 E5 83 EC 08 83 7D 08 00 75 07 B8 01 00 00 00 EB 16 8B 45 08 83 E8 01 83 EC 0C 50 E8 ?? ?? ?? ?? 83 C4 10 0F AF 45 08 C9 C3 }
	condition:
		$1
}

rule file_0_2_0 {
	meta:
		name = "my_strlen"
		size = 40
	strings:
		$1 = { 55 89 E5 83 EC 10 8B 45 08 89 45 FC EB 04 83 45 FC 01 8B 45 FC 0F B6 00 84 C0 75 F2 8B 55 FC 8B 45 08 29 C2 89 D0 C9 C3 }
	condition:
		$1
}