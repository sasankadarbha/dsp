import sys

#decrypt function
def decrypt_otp(cipher,key):
    msg = ""
    #compare length of key and cipher
    if len(cipher) != len(key):
        print ("Error!! Cipher and Key are of different lengths.")
        return msg
    
    else:
        msg_str = ""
        msg_bin = ""
        #ord returns ASCII code of a character
        #chr return character for an ASCII code
        #zip returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the arguments

        msg_bin = [ord(a) ^ ord(b) for a,b in zip(cipher,key)]
    
        #convert msg_bin to string    
        for i in msg_bin:
            msg_str = msg_str + str(i)

        #taking 8bits in binary and converting into character
        for i in range(0, 32, 8):
            n = int(msg_str[i:i+8],2)
            #convert ASCII to character and append to msg string
            msg = msg + chr(n)

        print ("Plain Text is: ",msg)
        return msg
      
#argv[0] is program name
#argv[1] is path of cipher file
#argv[2] is path of key file

cipherpath = sys.argv[1]
keypath = sys.argv[2]

#opening ciphertext.txt
cipher_file = open(cipherpath,'r')
cipher = cipher_file.read()
print ("Cipher is: ",cipher)

#opening key.txt
key_file = open(keypath,'r')
key = key_file.read()
print ("Key is: ",key)

#opening result.txt
msg_file = open("../data/result.txt", "w")

#function calling and writing output to a file
msg_file.write(decrypt_otp(cipher,key))

#closing result file    
msg_file.close()
