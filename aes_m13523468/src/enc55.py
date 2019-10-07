import os
import sys
from Crypto.Cipher import AES


def enc55(msg, key, iv):
    """This function accepts plaintext, 32bytes key and 16bytes IV"""
    #converting key to bytes from hex
    key = bytes.fromhex(key)
    
    #CBC
    obj = AES.new(key, AES.MODE_CBC, iv)
    ciphertxt = obj.encrypt(msg)#ciphertxt will be in 'bytes'
    ciphertxt = ciphertxt.hex()
    print("Ciper in CBC mode is: ",ciphertxt)
    
    #ECB
    obj2 = AES.new(key, AES.MODE_ECB, iv)
    ciphertxt = obj2.encrypt(msg)#ciphertxt will be in 'bytes'
    ciphertxt = ciphertxt.hex()
    print("Ciper in ECB mode is: ",ciphertxt)
    return
    
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

#function call and writing output to a ciphertext.txt

enc55(msg, key, iv)

