'''
5. Write a Python program to get the current memory address and the length in elements of the buffer used to hold an
array?s contents and also find the size of the memory buffer in bytes.
'''

def MultipleOps(x):
    print(str(array_num))
    print(x.buffer_info())
    print(str(x.buffer_info()[1] * x.itemsize))

from array import *
array_num = array('i',[1,2,3,4,5])
MultipleOps(array_num)