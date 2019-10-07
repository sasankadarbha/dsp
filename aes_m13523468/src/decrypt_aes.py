import os
import sys
from Crypto.Cipher import AES


def unpad(s):
    """removes padding"""
    return "".join([i for i in s if ord(i)>31])

def decrypt_aes(cipher,key,iv):
    """This function accepts cipher, key, iv in bytes and decrypts"""
    iv = bytes.fromhex(iv)
    key = bytes.fromhex(key)
    cipher_dec = bytes.fromhex(cipher)
    
    obj2 = AES.new(key, AES.MODE_CBC, iv)
    plaintext = obj2.decrypt(cipher_dec)

    #formatting bytes to string
    plaintext = plaintext.decode('utf-8')
    
    #function call
    plaintext = unpad(plaintext)
    print("Plaintext is: ",plaintext)
    return plaintext

#argv[0] is program name
#argv[1] is path of cipher file
#argv[2] is path of key file
#argv[3] is path to iv file

cipherpath = sys.argv[1]
keypath = sys.argv[2]
ivpath = sys.argv[3]

#-----------------------
#opening cipher file
cipher_file = open(cipherpath,'r')
cipher_txt = cipher_file.read()
print("Cipher is: ",cipher_txt)
cipher_file.close()
#------------------------
#opening key.txt
key_file = open(keypath,'r')
key = key_file.read()
print ("Key is: ",key)
key_file.close()
#---------------------
#opening file for writing iv
iv_file = open("../data/iv.txt", "r")
iv = iv_file.read()
print("IV is: ",iv)
#closing iv file
iv_file.close()
#--------------------
#opening file for writing result text
result_file = open("../data/result.txt", "w")

#function call and writing output to a result.txt
result = decrypt_aes(cipher_txt, key, iv)
result_file.write(result)

#closing cipher file
result_file.close()
