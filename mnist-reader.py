# Read gzip file adapted from https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python

import gzip

f = gzip.open('data/t10k-images-idx3-ubyte.gz', 'rb')

hexdata = f.read(4) 
# Currently reads \x00\x00\x08\x03 -> 00000000 00000000 00001000 00000011 in binary

# Use iPython to run through some options on hexdata, nothing of interest but - check if any options on int. int.from_bytes takes two arguments, try inputting hexdata and 'big' - big/little depends on which way binary is read by your machine (left to right or right to left)

print(int.from_bytes(hexdata, 'big'))
