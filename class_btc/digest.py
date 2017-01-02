#
#  Digest Class Relations
#	string -> utf-8 -> binary <-> hex <-> hex_bin  
#	B58 <-> int <-> hex
#   Binaries formed from hex cannot usually be decoded into unicode with utf-8
#	Canonical Form: binary  

from lib_BTC import CONSTANTS 
import binascii

class Digest:
	def __init__(self, value, in_hex = False, in_B58 = False):
	# value = text | hex | binary | integer | B58 
		self.value = value
		self.in_hex = in_hex
		self.in_B58 = in_B58
		if not in_B58:
			(self.bin, self.hex) = self.calc_digest()
			self.size = (len(self.hex) + 1) // 2 
			self.num = int(self.hex, 16)
			self.B58 = self.B58_encode()
		else:
			self.B58 = value
			self.num = self.B58_decode()
			(self.bin, self.hex) = self.calc_digest(self.num)
			self.size = (len(self.hex) + 1) // 2 
			
	def calc_digest(self, value = None, hex_bin = False):
		# default to self values
		if value == None:
			value = self.value
			in_hex = self.in_hex	
		if isinstance(value, type(b'ab')):
			if in_hex:
				val = value.lower()
				if val[0:2] == b'0x':
					val = val[2:]
				return (binascii.unhexlify(val), val.decode('utf-8'))
			else:
				return (value, binascii.hexlify(value).decode('utf-8'))
		elif isinstance(value, type('abc')):
			if in_hex:
				val = value.lower()
				if val[0:2] == '0x':
					val = val[2:]
				return (bytes.fromhex(val), val)
			else:
				val = value.encode('utf-8')
				return (val, binascii.hexlify(val).decode('utf-8'))		
		elif isinstance(value, type(12)):
			val = hex(value)[2:]
			return (bytes.fromhex(val), val)
		else:
			print("ERROR: Invalid input to Digest Class binary function")
			return (None, None)

	def B58_encode(self):
		"Encodes in B58 from integer format"
		(B58, arr, val, i) = (CONSTANTS.B58_alphabet, [], self.num, 0)
		while(val > 0):
			(val, rem) = divmod(val, 58) # combined division remainder
			arr.append(B58[rem])
		# Append 1 for each "00" starting byte
		while (i < self.size) and (self.hex[2*i:2*i+2] == '00'):
				i += 1
				arr.append(B58[0])
		arr.reverse()
		return ''.join(arr)			
			
	def B58_decode(self):	
		"Decode base58 encoded string into integer"
		(B58, sum, wif) = (CONSTANTS.B58_alphabet, 0, self.B58)
		for val in [B58.index(char) for char in list(wif)]:
			sum *= 58
			sum += val
		return sum		
			
def clean( text ):
	var = "".join(text.lower().split())
	return var
			
			
			
