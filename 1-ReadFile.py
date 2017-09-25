# 1 - Read the data files
# Download the image and label files. Have Python decompress and read them byte by byte into appropriate data structures in memory.

# Read gzip file adapted from https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python

import gzip
limit = 50 # Limiting output for now
index = 9

# Using "with" for files limits the scope of variables within the block
with gzip.open('data/t10k-labels-idx1-ubyte.gz', 'rb') as f:
    # Pointer at 0
    magic = f.read(4)
    magic = int.from_bytes(magic, 'big')
    print("Magic: ", magic)

    # Pointer now at 3 (4th pos)
    numLabels = f.read(4)
    numLabels = int.from_bytes(numLabels, 'big')
    print("Num of labels: ", numLabels)

    # Inefficient Way
    # labels = []

    # for i in range(numLabels):
    #     labels.append(f.read(1))

    # Proper Way
    # labels = [int.from_bytes(f.read(1)) for i in range(numLabels)]
    # --------- OR, tidier ---------
    labels = [f.read(1) for i in range(numLabels)]
    labels = [int.from_bytes(label, 'big') for label in labels]

