'''
Write a Python program to append items from a specified list.
'''

'''
#MT Solution
def AppendItem(arr,itm):
    index = 0
    for i in itm:
        arr.append(itm[index])
        index += 1
    for j in arr:
        print(j)

from array import *
array_num = array('i',[1,2,3,4,5])
items_num = array('i',[6,7,8])
AppendItem(array_num,items_num)
'''


#Actual solution
#Note : A list is created
#       and using .fromlist() it is attached to an array
from array import *
num_list = [1, 2, 6, -8]
array_num = array('i', [])
print("Items in the list: " + str(num_list))
print("Append items from the list: ")
array_num.fromlist(num_list)  # array.fromlist(list)
print("Items in the array: " + str(array_num))
