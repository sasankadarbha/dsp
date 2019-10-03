import sys

def encrypt_otp( msg, key):
    """This function accepts two strings and performs xor on their binary values """
    #convert plain text to binary
    msg_bin = '0'
    msg_bin = msg_bin + '0'.join(format(ord(x), 'b')for x in msg)
    cipher_bin = ""
    
    #compare length of key and text
    if len(msg_bin) != len(key):
        print ("Error!! Plain Text and Key are of different lengths.")
        return cipher_bin
    
    else:
        #ord returns ASCII code of a character
        cipher = [ord(a) ^ ord(b) for a,b in zip(msg_bin,key)]
    
        #convert cipher tuple to string   
        for i in cipher:
            cipher_bin = cipher_bin + str(i)

        print ("The Cipher is: ",cipher_bin)
        return cipher_bin


    
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


#opening file for writing cipher text
cipher_file = open("../data/ciphertext.txt", "w")

#function call and writing output to a ciphertext.txt
cipher_file.write(encrypt_otp(msg,key))

#closing cipher file
cipher_file.close()
