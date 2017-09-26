# 1 - Read the data files
# Download the image and label files. Have Python decompress and read them byte by byte into appropriate data structures in memory.

# Read gzip file adapted from https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python

import gzip
from PIL import Image
#import numpy as np

# Numpy not giving errors here but not running correctly - see
# https://github.com/numpy/numpy/issues/9272 and 
# https://github.com/ContinuumIO/anaconda-issues/issues/1508
# Have tried uninstalling & reinstalling, updating python & other packages, will keep trying / maybe try a numpy alternative


# -----------------------------------------------------------------
# Problem 1 - Read the Data Files

def readLabelsFromFile(filename): # For reading a label file
    # Using "with" for files limits the scope of variables to within the block. No file closing means no forgetting to close = good.
    with gzip.open(filename, 'rb') as f:
        # Pointer at 0, read the magic number - 801 means 1 dimention, 802 means 2 dim. etc etc
        magic = f.read(4) # First 4 bytes = magic number
        magic = int.from_bytes(magic, 'big') # Convert bytes to int format, 'big' = big-endian / most significant byte first
        print("Magic: ", magic)

        # Pointer now at 3 (4th pos)
        numLabels = f.read(4) # Next 4 bytes = number of items in the file
        numLabels = int.from_bytes(numLabels, 'big')
        print("Num of labels: ", numLabels)

        # Inefficient Way
        # labels = []

        # for i in range(numLabels):
        #     labels.append(f.read(1))

        # Proper Way
        # labels = [int.from_bytes(f.read(1)) for i in range(numLabels)]
        # --------- OR, tidier inline for loop ---------
        labels = [f.read(1) for i in range(numLabels)] # Read file byte by byte and store items in array
        labels = [int.from_bytes(label, 'big') for label in labels] # Overwrite the labels array with ints instead of bytes (same data different format)
    return labels

print("Label Files -------------")
# Pass filenames into the read labels function
trainLabels = readLabelsFromFile('data/train-labels-idx1-ubyte.gz')
testLabels = readLabelsFromFile('data/t10k-labels-idx1-ubyte.gz')

def readImagesFromFile(filename): # For reading an image file (not the same structure as a label file)
    with gzip.open(filename, 'rb') as f:
        # Same as label function, read magic number
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("Magic: ", magic)

        # Next 4 bytes = number of items (images)
        numImgs = f.read(4)
        numImgs = int.from_bytes(numImgs, 'big')
        print("Num of Images: ", numImgs)

        # Next 4 = number of rows
        numRows = f.read(4)
        numRows = int.from_bytes(numRows, 'big')
        print("Num of Rows: ", numRows)

        # Next 4 = number of columns
        numCols = f.read(4)
        numCols = int.from_bytes(numCols, 'big')
        print("Num of Cols: ", numCols)

        # Inefficient / Messy Way (but simplest)
        images = []
        for i in range(numImgs):
            rows = []
            for r in range(numRows):
                cols = []
                for c in range(numCols):
                    cols.append(int.from_bytes(f.read(1), 'big')) # For every column add the current byte (pixel) to the column array
                rows.append(cols) # For every row, add the column array
            images.append(rows) # For every image, add the rows array - rows + columns of pixels = full image.
    return images # Return the image array

print()
print("Image Files -------------")
# Pass filenames to read images function
trainImages = readImagesFromFile('data/train-images-idx3-ubyte.gz')
testImages = readImagesFromFile('data/t10k-images-idx3-ubyte.gz')

# -----------------------------------------------------------------------------------
# Problem 2 - Output Image to the Console using .'s and #'s depending on pixel value.

for row in trainImages[2]: # For each row in 3rd image (looks like a 4?)
    for col in row: # For each column in each row
        print('. ' if col<= 127 else '# ', end='') # Output either . or #, end result should look somewhat like a 4
        # Spacing after . and # make output more accurate
    print() # New line for a new row


# -----------------------------------------------------------------------------------
# Problem 3 - Output image files as PNGs.
# print("Output images as PNG files? Y/N: ")
# ans = input()
# if ans.lower == 'y':
#     img = Image.fromarray(np.array(trainImages[4999]))
#     img = img.convert('RGB')
#     img.show()
#     img.save('2.png')
# else:
#     # do nothing