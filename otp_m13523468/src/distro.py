import sys
import random

#there will be 8 possible key values for three bits

#intiliaze list with zeroes
freq = [0,0,0,0,0,0,0,0]
print("Claculating frequency of each 3 bit key in 6000 generated keys")


#create random sequence of 0's and 1's for 6000 times
for j in range(6000):
    key=""

    for i in range(3):
        key = key + str(random.randint(0,1))

    #convert binary string to decimal
    n = int(key,2)
    # since n is value of key (n-1)th index is increment by 1
    freq[n-1] = freq[n-1]+1

#print frequency of each key
print('Frequency of Key:000 = ', freq[0])
print('Frequency of Key:001 = ', freq[1])
print('Frequency of Key:010 = ', freq[2])
print('Frequency of Key:011 = ', freq[3])
print('Frequency of Key:100 = ', freq[4])
print('Frequency of Key:101 = ', freq[5])
print('Frequency of Key:110 = ', freq[6])
print('Frequency of Key:111 = ', freq[7])

