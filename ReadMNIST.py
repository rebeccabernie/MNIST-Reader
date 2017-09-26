# 1 - Read the data files
# Download the image and label files. Have Python decompress and read them byte by byte into appropriate data structures in memory.

# Read gzip file adapted from https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python

import gzip
from PIL import Image
import numpy

# -----------------------------------------------------------------
# Problem 1 - Read the Data Files

def readLabelsFromFile(filename):
    # Using "with" for files limits the scope of variables within the block
    with gzip.open(filename, 'rb') as f:
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
    return labels

print("Label Files")
trainLabels = readLabelsFromFile('data/train-labels-idx1-ubyte.gz')
testLabels = readLabelsFromFile('data/t10k-labels-idx1-ubyte.gz')

def readImagesFromFile(filename):
    with gzip.open(filename, 'rb') as f:
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("Magic: ", magic)

        numImgs = f.read(4)
        numImgs = int.from_bytes(numImgs, 'big')
        print("Num of Images: ", numImgs)

        numRows = f.read(4)
        numRows = int.from_bytes(numRows, 'big')
        print("Num of Rows: ", numRows)

        numCols = f.read(4)
        numCols = int.from_bytes(numCols, 'big')
        print("Num of Cols: ", numCols)

        # Inefficient / Messy Way
        images = []
        for i in range(numImgs):
            rows = []
            for r in range(numRows):
                cols = []
                for c in range(numCols):
                    cols.append(int.from_bytes(f.read(1), 'big'))
                rows.append(cols)
            images.append(rows)
    return images

print()
print("Image Files")
trainImages = readImagesFromFile('data/train-images-idx3-ubyte.gz')
testImages = readImagesFromFile('data/t10k-images-idx3-ubyte.gz')

# -----------------------------------------------------------------------------------
# Problem 2 - Output Image to the Console using .'s and #'s depending on pixel value.
print("Output image to console? Y/N: ")
ans = input()
if ans.lower() == 'y':
    for row in trainImages[4999]:
        for col in row:
            print('.' if col<= 127 else '#', end='')
        print()
else:
    pass


# -----------------------------------------------------------------------------------
# Problem 3 - Output image files as PNGs.
print("Output images as PNG files? Y/N: ")
ans = input()
if ans.lower == 'y':
    img = Image.fromarray(numpy.array(trainImages[4999]))
    img = img.convert('RGB')
    img.show()
    img.save('2.png')