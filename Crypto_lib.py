# 
# PyCrypto 2.4.1 and later work on Python 3.x
# Reference: https://www.dlitz.net/software/pycrypto/

from Crypto.Hash import SHA256, RIPEMD, MD2, MD4, MD5	
Crypto_dict = {'SHA256': SHA256, 
	'RIPEMD': RIPEMD,
	'MD2': MD2, 'MD4': MD4, 'MD5': MD5
	}

def fn_get(Crypto_hash):
	def fn_temp(binary):
		hash = Crypto_hash.new()
		hash.update(binary)
		return hash.digest()
	return fn_temp

# Pack all hashes into 'hashes' dictionary	
hashes = {}	
for key, val in Crypto_dict.items():
	hashes[key] = fn_get(val)
