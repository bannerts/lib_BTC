#
#
#	References:
#		https://en.bitcoin.it/wiki/Private_key

def clean( text ):
	var = "".join(text.lower().split())
	if var[0:2] == "0x":
		return var[2:]
	else:
		return var	

def hex2int( hex_unicode ):
	X = clean(hex_unicode)
	if X[0:2] != '0x':
		X = '0x' + X
	return int(X, 16)

PKmin = '0x1'
PKmax = clean("""0x
	FFFF FFFF FFFF FFFF FFFF FFFF
	FFFF FFFE BAAE DCE6 AF48 A03B 
	BFD2 5E8C D036 4141""")

PKmin_int = hex2int(PKmin)
PKmax_int = hex2int(PKmax)

B58_alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
version_application_byte = "80"  # given in hex
