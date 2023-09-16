from Crypto.PublicKey import RSA
import hashlib
from Crypto.Cipher import PKCS1_v1_5

mykey = RSA.generate(1024)

public_key = mykey.publickey().exportKey("PEM")
private_key = mykey.exportKey("PEM")

#print(mykey.publickey().exportKey('PEM'))# to see public key of private key below
#print(mykey.exportKey(format='PEM')) #privatekey

print(public_key)
print(private_key)

print(hashlib.sha256(public_key).hexdigest()) #public key in hexadevimal özeti

example_text = "a"
cipher = PKCS1_v1_5.new(mykey)
myencdata = mykey.encrypt(example_text, cipher)
mydecdata = mykey.decrypt(myencdata)
print(myencdata)
print(mydecdata)