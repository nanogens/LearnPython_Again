'''
Write a Python program to append items from an array to the end of another array.
'''

def App(x_arr):
    index = 0
    x_arr.extend(x_arr)

    # either one of the two ways of printing out the Array below works
    '''    
    for i in x_arr:
        print(i)
    '''
    for i in x_arr:
        #print(i)
        print(x_arr[index])
        index += 1

from array import *
array_num = array('i',[1,2,3,4,5])
App(array_num)