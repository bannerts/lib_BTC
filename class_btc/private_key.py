#
#  PrivateKey Class Definition
#	
#	Wallet Import Format
#	References:
#		https://en.bitcoin.it/wiki/Wallet_import_format

from lib_BTC import CONSTANTS
from class_BTC import digest as D

import hashlib, hashes


class PrivateKey:
	def __init__(self, value, in_hex=True, in_B58=False):
	# value = hex | num | WIF
		self.value = value
		self.in_hex = in_hex
		self.in_B58 = in_B58
			
		if not isinstance(value, D.Digest):
			value = D.Digest(value, in_hex, in_B58)			
				
		if in_B58:
			if self.valid_WIF(value):
				self.wif = value.B58
				var = D.Digest(value.hex[2:-8], True)			
				(self.hex, self.num) = (var.hex, var.num)
			else:
				print("INVALID WALLET")
		else: 
			(self.hex, self.num, self.wif) = (value.hex, value.num, self.WIF(value))
		self.ECDSA_keys()
			
	
	def ECDSA_keys(self):
		# Secret Key Object
		self.sk = SigningKey.from_secret_exponent(self.num, curve=SECP256k1, hashfunc=hashlib.sha256)
		# Verification Key Object
		self.vk = self.sk.get_verifying_key()
		(self.x, self.y) = self.vk.to_xy()
		self.public = D.Digest("04" + D.Digest(self.x).hex + D.Digest(self.y).hex, in_hex=True)
		addr = self.BTC_Address(self.public)
		if self.valid_WIF(addr):
			self.address = addr.B58
		else:
			print("Invalid Bitcoin Address")
		return
	
	def BTC_Address(self, pk_digest):
		# Step 2-3: Calc SHA256 then RIPEMD 
		VAR3 = hashes.Hash(hashes.Hash(self.public, 1, 'SHA256'), 1, 'RIPEMD')
		# Step 4: Add version byte in front "00" (for main network) 
		VAR4 = D.Digest("00" + VAR3.hex, in_hex=True)
		# Step 5-6: Calc double SHA256 on VAR4
		VAR6 = hashes.Hash(VAR4, 2, 'SHA256')
		# Step 7-8: Append first four bytes of VAR6 at end of VAR 4, B58 encode
		return D.Digest(VAR4.hex + VAR6.hex[0:8], in_hex=True)
		
		
	# Private Key to WIF
	def WIF(self, value, vbyte = CONSTANTS.version_application_byte):
		"Transform private key in hexidecimal, integer, or binary form to WIF"
		# Verify value is in valid range
		if not (CONSTANTS.PKmin_int < value.num < CONSTANTS.PKmax_int):
			print("ERROR: in private_key, PrivateKey class, WIF function input out of range")
			return (None, None)
		# Step 1-2: Append Version/Application Byte in front
		var2 = D.Digest(vbyte + value.hex, True)
		# Step 3-6: Append the first 4 bytes of the double SHA256 of 'var2' to the end 'var2' -> convert to B58
		return D.Digest(var2.hex + hashes.Hash(var2, 2, 'SHA256').hex[0:8], True).B58

	def valid_WIF(self, value):
		var = D.Digest(value.hex[:-8], True)
		return hashes.Hash(var, 2, 'SHA256').hex[:8] == value.hex[-8:]
