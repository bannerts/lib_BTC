#
#	Elliptic Curve Digital Signature Algorithm
#	Bitcoin uses ECDSA to sign transactions: secp256k1 curve
#	References:		
#		https://en.bitcoin.it/wiki/Secp256k1
#		** https://github.com/warner/python-ecdsa
#		** https://en.bitcoin.it/wiki/Technical_background_of_Bitcoin_addresses


#	ADDED THIS FUNCTION TO ecdsa/keys.py in class VerifyKey 
#    ##  -- MODIFIED BELOW 
#    def to_xy(self):
#        return (self.pubkey.point.x(), self.pubkey.point.y())
#    ##  -- MODIFIED ABOVE

from class_BTC import private_key, digest


PK1 = private_key.PrivateKey("18E14A7B6A307F426A94F8114701E7C8E774E7F9A47E2C2035DB29A206321725", in_hex=True)

print(PK1.hex)
print(PK1.public.hex)
print(PK1.address)


XX = digest.clean("E9 87 3D 79 C6 D8 7D C0 FB 6A 57 78 63 33 89 F4 45 32 13 30 3D A6 1F 20 BD 67 FC 23 3A A3 32 62")
PK2= private_key.PrivateKey(XX, in_hex=True)
print(PK2.wif)
print(PK2.address)






# signature = sk.sign(b"message",  hashfunc=hashlib.sha256)
# assert vk.verify(signature, b"message",  hashfunc=hashlib.sha256)



