# Text must be utf-8 binary encoded before it can be hashed
#   "message".encode('utf-8')
#	b"message"
# Unicode Reference: http://docs.python.org/3.2/tutorial/introduction.html#about-unicode
from class_BTC import digest as D

# Dictionary of all hashes
hash_dict ={'default': lambda x: x}
Include_PyCrypto = True
Include_hashlib = True


### Logic to include specific hash libraries ###
if Include_PyCrypto:
	from lib_BTC.lib_hash import Crypto_lib
	hash_dict.update(Crypto_lib.hashes)	
	
if Include_hashlib:
	from lib_BTC.lib_hash import hashlib_lib
	hash_dict.update(hashlib_lib.hashes)	
### ---------------------------------------- ###
	
	
def Hash(digest, n=1, hash_fn='SHA256'):
	"Computes SHA256 digest (binary) of a binary encoded utf-8 string"
	if not isinstance(digest, D.Digest):
		digest = D.Digest(digest) 
	
	# Get hash function
	if hash_fn in hash_dict:
		hasher = hash_dict[hash_fn] # Selects hash function from hash dictionary
	else:
		hasher = hash_dict['default']
	
	# Calculate n hashes
	binary = digest.bin
	for i in range(n):
		binary = hasher(binary)
	return D.Digest(binary)
