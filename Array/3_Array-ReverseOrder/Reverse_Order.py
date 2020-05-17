'''
3. Write a Python program to reverse the order of the items in the array.
'''

def RevOrder(x):
    x.reverse()

from array import *
array_num = array('i',[1,2,3,4,5])
RevOrder(array_num)
for i in array_num:
    print(i)