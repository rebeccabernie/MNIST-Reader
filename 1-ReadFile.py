# 1 - Read the data files
# Download the image and label files. Have Python decompress and read them byte by byte into appropriate data structures in memory.

# Read gzip file adapted from https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python

import gzip

def readLabelsFromFile(filename):
    # Using "with" for files limits the scope of variables within the block
    print("Label Files")
    with gzip.open(filename, 'rb') as f:
        # Pointer at 0
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("(Magic: ", magic)

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

trainLabels = readLabelsFromFile('data/train-labels-idx1-ubyte.gz')
testLabels = readLabelsFromFile('data/t10k-labels-idx1-ubyte.gz')

def readImagesFromFile(filename):
    # Using "with" for files limits the scope of variables within the block
    print()
    print("Image Files")
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

trainImages = readImagesFromFile('data/train-images-idx3-ubyte.gz')
testImages = readImagesFromFile('data/t10k-images-idx3-ubyte.gz')