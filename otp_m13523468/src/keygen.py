import sys
import random

def keygen(key_length):
    """returns a sequence of 0's and 1's for specified key_length value"""
    key=""
    for i in range(key_length):
        key = key + str(random.randint(0,1))
    print(key)
    return key

#calling from here
key_len = int(sys.argv[1])

if (key_len < 1 or key_len >128):
    print ("Security Parameter must be between 1 and 128")
    sys.exit(-1)

#opening a file
new_file = open("../data/newkey.txt", "w")

#function call to generate a key and write it to file
new_file.write(keygen(key_len))

#closing the file
new_file.close()
