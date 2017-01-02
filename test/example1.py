#
#

from class_BTC import digest as D
import hashes


message = D.Digest("hello")

Answer_1 = '0x2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
Answer_2 = '0x9595c9df90075148eb06860365df33584b75bff782a510c6cd4883a419833d50'
Answer_3 = '0xb6a9c8c230722b7c748331a8b450f05566dc7d0f'

print(message.bin)
print(message.hex)

A1 = hashes.Hash(message, 1, 'sha256')
A2 = hashes.Hash(message, 2, 'sha256')
A3 = hashes.Hash(A1, 1, 'RIPEMD')

print(A1.hex)
print(A2.hex)
print(A3.hex)
