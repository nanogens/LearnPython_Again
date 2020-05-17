'''
2. Write a Python program to append a new item to the end of the array.
'''

def appd(x):
    x.append(5)

from array import *
array_num = array('i',[1,2,3,4])
appd(array_num)
for i in array_num:
    print(i)