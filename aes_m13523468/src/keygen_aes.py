import os

def key_gen():
    """This function generates 32bytes random = 256bits"""
    rndkey = os.urandom(32)
    return rndkey

#opening file for writing AES key
key_file = open("../data/key.txt", "w")

#function call and convert to hex
rndkey = key_gen().hex()
print("Generated key is:\n",rndkey)
print("Size of key: ",len(bytes.fromhex(rndkey)), "bytes", sep = ' ')
#print("Len in hex :",len(rndkey))
#writing hexadecimal key to file.
key_file.write(rndkey)

#closing cipher file
key_file.close()

