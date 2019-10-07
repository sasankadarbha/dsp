import os
import sys
from Crypto.Cipher import AES

pad = lambda s: s + (16 - len(s) % 16)*chr(16 - len(s)% 16)    

def encrypt_aes(msg, key, iv):
    """This function accepts plaintext, 16bytes key and 16bytes IV"""
    #converting key to bytes from hex
    key = bytes.fromhex(key)
    msg = pad(msg)
    obj = AES.new(key, AES.MODE_CBC, iv)
    ciphertxt = obj.encrypt(msg)#ciphertxt will be in 'bytes'

    #converting ciphertxt into hexadecimal
    ciphertxt = ciphertxt.hex()
    print("Ciper is: ",ciphertxt)
    return ciphertxt
    
def iv_gen():
    """This function generates IV of random 16 bytes"""
    rndiv = os.urandom(16)
    return rndiv


#argv[0] is program name
#argv[1] is path of plaintext file
#argv[2] is path of key file

msgpath = sys.argv[1]
keypath = sys.argv[2]

#opening plaintext.txt
msg_file = open(msgpath,'r')
msg = msg_file.read()
print ("Plain Text is: ",msg)

#opening key.txt
key_file = open(keypath,'r')
key = key_file.read()
print ("Key is: ",key)

#--------------------
#generating random IV of 16bytes
iv = iv_gen()
print ("IV is: ",iv.hex())

#opening file for writing iv
iv_file = open("../data/iv.txt", "w")

#function call and writing output to a iv.txt in hex format
iv_file.write(iv.hex())

#closing iv file
iv_file.close()

#--------------------
#opening file for writing cipher text
cipher_file = open("../data/ciphertext.txt", "w")

#function call and writing output to a ciphertext.txt

cipher = encrypt_aes(msg, key, iv)
cipher_file.write(cipher)

#closing cipher file
cipher_file.close()
