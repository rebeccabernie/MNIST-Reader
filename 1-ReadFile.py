# 1 - Read the data files
# Download the image and label files. Have Python decompress and read them byte by byte into appropriate data structures in memory.

# Read gzip file adapted from https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python

import gzip
limit = 50 # Limiting output for now
index = 9

f = gzip.open('data/t10k-images-idx3-ubyte.gz', 'rb')


for index, byte in enumerate(f):
    hexdata = f.read(4) 
    print("Hex: " + str(hexdata))
    print("Int: " + str((int.from_bytes(hexdata, 'big')))) # Use iPython to run through some options on hexdata, nothing of interest but - check if any options on int. int.from_bytes takes two arguments, try inputting hexdata and 'big' - big/little depends on which way binary is read by your machine (left to right or right to left)
    print()
    
    if index == limit:
        break
        # Limit & enumerate function adapted from https://stackoverflow.com/questions/36106712/how-can-i-limit-iterations-of-a-loop-in-python
    
# \x00\x00\x08\x03 (first item) -> 00000000 00000000 00001000 00000011 in binary


