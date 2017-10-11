# Problem Sheet 2 - MNIST Reader

> Module: Emerging Technologies / 4th Year  
> Lecturer: Dr Ian McLoughlin  
> [Original Problem Sheet](https://github.com/emerging-technologies/emerging-technologies.github.io/blob/master/problems/digits.md)

## Overview

This problem sheet relates to the [MNIST Database](http://yann.lecun.com/exdb/mnist/) of handwritten digits. This repository **does not** include copies of the .gz files contained in the database, but these can be downloaded from the MNIST [website](http://yann.lecun.com/exdb/mnist/). The compressed image files contain images not in a standard format (like PNG or JPEG), meaning they cannot be viewed without first being converted to a one of these formats.  
The training set and test set contain 60,000 and 10,000 examples, respectively. This program uses both sets.  

## Exercises

*Note that the high number of items in each file means this program can be very slow, in particular when reading the test images file.*

**1. Read the Files**  
The program first decompresses and reads in the .gz files. The first 4 bytes contain the magic number, which relates to the number of dimensions in the file - label files are only one-dimensional (just a list of labels), whereas image files are three-dimensional (each image contains rows & columns of pixels - *number of images x rows in each x columns in each*).  
When finished, the program displays *(for each file)* the file's magic number and either the number of labels, or the number of images, rows, and columns.

**2. Output an Image to the Console**  
After reading the files into memory, the program will output an interpretation of the third image in the training set to the console. The program looks at this image in the file and outputs `.` if the pixel value is less than 128, or `#` if it's greater - the digit in the image will be marked in `#`'s.  
The output won't be exactly like the original image since this method only deals with *either* black or white / `.` or `#`, but it should be clear enough to see what the digit is. See below.  

<img src="https://user-images.githubusercontent.com/14957616/30874278-bf308f1c-a2e7-11e7-98f4-3ec92e0cfe26.PNG " width="200" height="200">

**3. Output the Images as PNGs**  
*Note: I have limited this part of the program to only save 2000 of each image
The program asks the user if they want to output the images in PNG format, if the user enters 'y' the program will continue. The program works by saving test images first, then training images. Test images get saved to the TestImages folder and training images to the TrainImages folder, which are created by the program if they don't already exist. For both sets of images, the program loops through each image in the set and saves the image with a name. The name consists of image type, image number, and the number displayed in the image. - e.g. `test-01234-7.png`.  See example of folder layout and saved images below.  

<img src="https://user-images.githubusercontent.com/14957616/31395086-d4e8b0f0-add7-11e7-8c88-d608340d62d8.png">

