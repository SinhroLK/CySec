from Crypto.Util.number import *
enc_base10= 11515195063862318899931685488813747395775516287289682636499965282714637259206269
flag = enc_base10.to_bytes(33, 'big')
print(flag.decode())