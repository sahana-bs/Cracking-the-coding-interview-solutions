'''
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

1 2 3
4 5 6
7 8 9
after 90 rotation (clockwise)
7 4 1
8 5 2
9 6 3

The most elegant solution for rotating the matrix is to firstly reverse the matrix around the main diagonal,
and then reverse it from left to right. These operations are called transpose and reflect in linear algebra.

This needs some understanding of how matricies are formed and works...Not my particular interest
1 2 3
4 5 6
7 8 9   transpose

1 4 7
2 5 8
3 6 9   reverse (flip along an axis)

7 4 1
8 5 2
9 6 3
*****************Always use Numpy for matrix operations****************

TC:the temporal complexity is O (1) because to transpose an array, numpy just swaps the shape and
stride information for each axis. No data needs to be copied for this to happen!!!That's why use NUMPY

SC:We are not doing this in place so addional space required. O(N^2)
'''

import numpy as np
a = np.arange(9).reshape((3,3))
print(a)
a=a.T
print(a)
print(np.flip(a,axis=0))
print(a)
