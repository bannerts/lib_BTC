#
#
# REFERENCES:
#	https://en.bitcoin.it/wiki/Wallet_import_format


from lib_BTC import WIF
from class_BTC import private_key as pk
from class_BTC import digest as D

# Test private Key Conversion to WIF
PK_HEX = "0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D"
Answer = "5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ"

X = pk.PrivateKey(PK_HEX)
print(Answer)
print(X.wif)

print()

Y = pk.PrivateKey(Answer, in_B58=True)
print(Y.hex)
print(PK_HEX.lower())


PK2_HEX = "0C28FCA38637A227600B2F750B7CAE11EC8613BF1FBE4719E89827E19D72AA1D"
print(PK2_HEX.lower())
X2 = pk.PrivateKey(PK2_HEX)
PK2_B58 = X2.wif
print(PK2_B58)
X3 = pk.PrivateKey(PK2_B58, in_B58=True)
PK3_HEX = X3.hex
print(PK3_HEX)
X4 = pk.PrivateKey(PK3_HEX, in_hex = True, in_B58=False)
PK4_B58 = X4.wif


PK = 'E9 87 3D 79 C6 D8 7D C0 FB 6A 57 78 63 33 89 F4 45 32 13 30 3D A6 1F 20 BD 67 FC 23 3A A3 32 62'
PK = D.clean(PK)
PK = pk.PrivateKey(PK)
print(PK.wif)
