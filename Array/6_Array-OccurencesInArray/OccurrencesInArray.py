'''
6. Write a Python program to get the number of occurrences of a specified element in an array.
'''

def Occur(arr,elem):
    num_four = 0
    for i in arr:
        if i is elem:
            num_four = num_four + 1
    print(num_four)


from array import *
array_num = array('i',[1,4,3,4,5])
element = 4
Occur(array_num,element)