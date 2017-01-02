#
#
#	References: https://en.bitcoin.it/wiki/Private_key

if __name__ == "__main__":
	from lib_BTC import convert	
	Qs = ["001", "a", "b", "aa", "ff", "10a", "0x10a"]
	As = [1, 10, 11, 170, 255, 266, 266]
	
	for i in range(len(Qs)):
		if convert.hex2int(Qs[i]) == As[i]:
			print("Passed %s: hex %s = %s" % (i, Qs[i], As[i]))
		else:
			print("### Failed %s: hex %s = %s" % (i, Qs[i], As[i]))	

	print("----------------")
	
	PK_hex = """E9 87 3D 79 C6 D8 7D C0 FB 6A 
		57 78 63 33 89 F4 45 32 13 30 3D 
		A6 1F 20 BD 67 FC 23 3A A3 32 62"""
	PK_hex = convert.clean(PK_hex)
	PK_int = convert.hex2int(PK_hex)
	print(PK_hex)
	print(PK_int) 
