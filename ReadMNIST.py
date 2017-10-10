# 1 - Read the data files
# Download the image and label files. Have Python decompress and read them byte by byte into appropriate data structures in memory.

# Read gzip file adapted from https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python

import gzip
from PIL import Image
import numpy as np
import os

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

def saveImages(imgType, imNum):

    limit = 1999 # Limiting image saving because would just take too long to save 70,000 images. Comment out "if index == limit: break" statements in Training/Test sections to save all 70,000 images.

    # if imNum is 0, use test image details
    if imNum == 0:
        imName = 'test'
        labels = testLabels
        images = testImages
        # Create directory for images if not already exists
        filepath = "PNGs/TestImages/"
        directory = os.path.dirname(filepath)

        if not os.path.exists(directory):
            os.makedirs(directory)

    # If imNum is 1, use training image details
    if imNum == 1:
        imName = 'train'
        labels = trainLabels
        images = trainImages
        filepath = "PNGs/TrainImages/"
        directory = os.path.dirname(filepath)

        if not os.path.exists(directory):
            os.makedirs(directory)

    print('Saving ' + str(imName) + ' images...')

    # Index loop adapted from https://stackoverflow.com/questions/522563/accessing-the-index-in-python-for-loops
    for index, item in enumerate(imgType):
        label = labels[index]

        # Leading 0s for names (0001, 0002 etc) adapted from https://stackoverflow.com/questions/134934/display-number-with-leading-zeros
        imfile = filepath + imName + '-' + str(index).zfill(5) + '-' + str(label) + '.png'
        name = imName + '-' + str(index).zfill(5) + '-' + str(label) + '.png'
        print ('saving ' + name + '...')

        img = Image.fromarray(np.array(images[index])*255)  # Image was saving all black, multiply by 255 to solve - adapted from https://stackoverflow.com/questions/28176005/pil-images-converted-to-rgb-getting-saved-as-plain-black-images-python
        img.convert('RGB')
        img.save(imfile, 'PNG')

        print (name + ' saved')

        if index == limit:
            break

    print(str(imName + ' images saved.'))

run = input('Save files as PNGs? y/n ')

if run.lower() == 'y':
    # Make directory if not exists adapted from https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist
    filepath = "PNGs/"
    directory = os.path.dirname(filepath)

    if not os.path.exists(directory):
        os.makedirs(directory)

    saveImages(testImages, 0)
    saveImages(trainImages, 1)