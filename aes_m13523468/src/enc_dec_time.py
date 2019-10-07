import os
import sys
from Crypto.Cipher import AES
import timeit

pad = lambda s: s + (16 - len(s) % 16)*chr(16 - len(s)% 16)

def removeNonAscii(s):
    """removes non printable ascii characters from a string"""
    return "".join([i for i in s if ord(i)>31])

def encrypt_aes(msg, key, iv):
    """This function accepts plaintext, 16bytes key and 16bytes IV"""
    #start timer
    start = timeit.default_timer()

    #converting key to bytes from hex
    key = bytes.fromhex(key)
    msg = pad(msg)
    obj = AES.new(key, AES.MODE_CBC, iv)
    ciphertxt = obj.encrypt(msg)#ciphertxt will be in 'bytes'

    #converting ciphertxt into hexadecimal
    ciphertxt = ciphertxt.hex()

    print("Ciper is: ",ciphertxt)

    #stop timer
    stop = timeit.default_timer()
    print('Encryption Running Time: ', stop-start)
    
    return ciphertxt

def decrypt_aes(cipher,key,iv):
    """This function accepts cipher, key, iv in bytes and decrypts"""
    #start timer
    start = timeit.default_timer()
    
    #iv = bytes.fromhex(iv)
    key = bytes.fromhex(key)
    cipher = bytes.fromhex(cipher)
    obj2 = AES.new(key, AES.MODE_CBC, iv)
    plaintext = obj2.decrypt(cipher)

    #formatting bytes to string
    plaintext = plaintext.decode('utf-8')
    #function call
    plaintext = removeNonAscii(plaintext)
    print("\nPlaintext is: ",plaintext)

    
    #stop timer
    stop = timeit.default_timer()
    print('Decryption Running Time: ', stop-start)

    return plaintext

    
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
print ("\nPlain Text is: ",msg)

#opening key.txt
key_file = open(keypath,'r')
key = key_file.read()
print ("Key is: ",key)

#--------------------
#generating random IV of 16bytes
iv = iv_gen()
print ("IV is: ",iv.hex())
print("\n")

cipher = encrypt_aes(msg, key, iv)
plaintxt = decrypt_aes(cipher, key, iv)
