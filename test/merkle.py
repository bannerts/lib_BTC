# 
# Compute merkle hash
# Refernce: https://en.bitcoin.it/wiki/Protocol_specification#Merkle_Trees

import hashes

# Set hash function for merkle
dhash = lambda X: hashes.Hash(X, 2, 'sha256')

def merkle_reduce( elements, hf=dhash):
	"Computes the merkle root of a list or tuple of elements"
	X = list(elements)
	if len(X) % 2 == 1:
		X.append(X[-1])
	return [ hf(X[2*i] + X[2*i+1]) for i in range(len(X)//2)]
	
def root( elements, hf=dhash):
	X = [hf(item) for item in elements]
	if len(X) % 2 == 1:
		X.append(X[-1])
	while (len(X) > 1):
		X = merkle_reduce(X, hf)
	return X
