# 1 - Read the data files
# Download the image and label files. Have Python decompress and read them byte by byte into appropriate data structures in memory.

# Read gzip file adapted from https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python

import gzip
limit = 50 # Limiting output for now
index = 9

f = gzip.open('data/t10k-labels-idx1-ubyte.gz', 'rb')

magic = f.read(4)
print("Magic: " + str(int.from_bytes(magic, 'big')))

numLabels = f.read(4)
print("Num of labels: " + str(int.from_bytes(numLabels, 'big')))
    
# \x00\x00\x08\x03 (first item) -> 00000000 00000000 00001000 00000011 in binary


