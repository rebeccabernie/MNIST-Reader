# Read gzip file adapted from https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python

import gzip

f = gzip.open('data/t10k-images-idx3-ubyte.gz', 'rb')

file_content = f.read()
print(file_content)