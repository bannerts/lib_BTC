# 
# hashlib 
# Reference: http://docs.python.org/3/library/hashlib.html

import hashlib

hashlib_dict = {'sha1': hashlib.sha1, 'sha224': hashlib.sha224, 
	'sha256': hashlib.sha256, 'sha384': hashlib.sha384, 
	'ripemd160': lambda: hashlib.new('ripemd160'),
	'md5': hashlib.md5
	}

def fn_get( hashlib_hash ):
	def fn_temp(binary):
		hash = hashlib_hash()
		hash.update(binary)
		return hash.digest()
	return fn_temp

# Pack all hashes into 'hashes' dictionary	
hashes = {}	
for key, val in hashlib_dict.items():
	hashes[key] = fn_get(val)
