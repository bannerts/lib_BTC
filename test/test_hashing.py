#
#  Testing file for hashing functions
#  Reference: https://en.bitcoin.it/wiki/Protocol_specification

if __name__ == "__main__":
	from lib_BTC import convert
	import hashes
	
	message = "hello"
	print(message)
	M = message.encode('utf-8')
	
	
	Answer_1 = b'2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
	Answer_2 = b'9595c9df90075148eb06860365df33584b75bff782a510c6cd4883a419833d50'
	Answer_3 = b'b6a9c8c230722b7c748331a8b450f05566dc7d0f'
	
	Q1a = set(convert.bin2hex(hashes.Hash(M, 1, 'sha256')) for i in range(5))	
	if len(Q1a) == 1 and Answer_1 in Q1a:
		print('Passed: sha256 in single hash test')
	else:
		print('### Failed: sha256 in single hash test')
		print(Q1a)
		print(Answer_1)
	Q1b = set(convert.bin2hex(hashes.Hash(M, 1, 'SHA256')) for i in range(6))	
	if len(Q1b) == 1 and Answer_1 in Q1b:
		print('Passed: SHA256 in single hash test')
	else:
		print('### Failed: SHA256 in single hash test')
		print(Q1a)
		print(Answer_1)		
		
		
	Q2a = set(convert.bin2hex(hashes.Hash(M, 2, 'sha256')) for i in range(6))
	if len(Q2a) == 1 and Answer_2 in Q2a:
		print('Passed: sha256 in double hash test')
	else:
		print('### Failed: sha256 in double hash test')
		print(Q2a)
		print(Answer_2)
	Q2b = set(convert.bin2hex(hashes.Hash(M, 2, 'SHA256')) for i in range(5))	
	if len(Q2b) == 1 and Answer_2 in Q2b:
		print('Passed: SHA256 in double hash test')	
	else:
		print('### Failed: SHA256 in double hash test')
		print(Q2b)
		print(Answer_2)
		
	
	Q3 = set(convert.bin2hex(hashes.Hash( hashes.Hash(M, 1, 'sha256'), 1, 'ripemd160')) for i in range(7))
	if len(Q3) == 1 and Answer_3 in Q3:
		print('Passed: RIPEMD in hash test')
	else:
		print('### Failed: RIPEMD in hash test')
		print(Q3)
		print(Answer_3)	

