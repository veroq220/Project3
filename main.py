import sys
import base64
from Crypto.Util.number import long_to_bytes
from Crypto.Util.number import bytes_to_long
from pwn import xor

ords = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

print("Here is your flag:")
ords_16 = bytes.fromhex(ords)
print(bytes.fromhex(ords))
print(base64.b64encode(ords_16))

ords_64 = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
print(long_to_bytes(ords_64))

data = 'label'

print('Here is your flag:')
flag = ("".join(chr(ord(c) ^ 13) for c in data))
print('crypto{{{}}}'.format(flag))


def xor_two_str(s1, s2):
    return "".join(format(int(a, 16) ^ int(b, 16), "x") for a, b in zip(s1, s2))


key_1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"

key_1_b = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key_2_1_b = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
key_2_3_b = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
key_2 = xor(key_1_b, key_2_1_b)
key_3 = xor(key_2_3_b, key_2)
flag = xor(bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"), key_3, bytes.fromhex(key_1), key_2)
print(flag)

data4 = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
data4b = bytes.fromhex(data4)

print(data4b)
