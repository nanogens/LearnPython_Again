from array import *  # for Array
from math import pi  # for Basic

# Array_Print5Ints ------------------------------------------------------------------
'''
1. Write a Python program to create an array of 5 integers and display the array items.
Access individual element through indexes.
'''
def Array_Print5Ints():
    array_num = array('i', [1, 2, 3, 5, 7, 9])
    for i in array_num:
        print(i)
    print("Access first three items individually:")
    print(array_num[0])
    print(array_num[1])
    print(array_num[2])

# Array_Append ------------------------------------------------------------------
'''
2. Write a Python program to append a new item to the end of the array.
'''
def appd(x,numtoappend):
    x.append(numtoappend)

def Array_Append():
    array_num = array('i',[1,2,3,4])
    appd(array_num,5) # append the number 5
    for i in array_num:
        print(i)

# Array_ReverseOrder ------------------------------------------------------------------
'''
3. Write a Python program to reverse the order of the items in the array.
'''
def RevOrder(x):
    x.reverse()

def Array_RevOrder():
    array_num = array('i',[1,2,3,4])
    RevOrder(array_num)
    for i in array_num:
        print(i)

# Array_MultipleOps ------------------------------------------------------------------
'''
5. Write a Python program to get the current memory address and the length in elements of 
the buffer used to hold an array?s contents and also find the size of the memory buffer 
in bytes.
'''
def MultipleOps(x):
    print(str(array_num))
    print(x.buffer_info())
    print(str(x.buffer_info()[1] * x.itemsize))

def Array_MultipleOps():
    array_num = array('i',[1,2,3,4,5])
    MultipleOps(array_num)

# Array_OccurenceInArray -------------------------------------------------------
'''
6. Write a Python program to get the number of occurrences of a specified element in an array.
'''
def Occur(arr,ele):
    num = 0
    for i in arr:
        if ele is i:
            num = num + 1
    print(num)

def Array_OccurenceInArray():
    array_num = array('i',[1,4,4,4,5]) # 3 occurences of the number 4 should be detected
    element = 4
    Occur(array_num,4)

# Array_AppendArray -------------------------------------------------------
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

def Array_AppendArray():
    array_num = array('i',[1,2,3,4,5])
    App(array_num)

# Basic_RadiusCircleArea -------------------------------------------------------
'''
Write a Python program to append items from an array to the end of another array.
'''
def Basic_RadiusCircleArea():
    radius = float(input("\nEnter radius of a circle:"))
    area = pi * radius * radius
    print("\nArea:" + str(area))


# # Basic_RadiusCircleArea ------------------------------------------------------- -------------------------------------------------------
'''
6. Write a Python program which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers
'''

'''
Note :
Python list:

A list is a container which holds comma separated values (items or elements) between square brackets where 
items or elements need not all have the same type. In general, we can define a list as an object that contains 
multiple data items (elements). The contents of a list can be changed during program execution. The size of a list 
can also change during execution, as elements are added or removed from it.

Python tuple:

A tuple is container which holds a series of comma separated values (items or elements) between parentheses such 
as an (x, y) co-ordinate. Tuples are like lists, except they are immutable (i.e. you cannot change its content 
once created) and can hold mix data types. 
'''

def Basic_CSVListTuple():
    values = input("\nEnter a few numbers separated by commas: ")
    listx = values.split(",")
    tuplex = tuple(listx)
    print('List: ', listx)
    print('Tuple: ', tuplex)


# # Class_GeneralLearning ------------------------------------------------------- -----------------------------------------------
def Class_GeneralLearning():

    class Things:
        pass

    class Person:
        def __init__(self,name,age):
            self.name = name
            self.age = age
        def myfunc(self):
            print("My name is {0} and my age is {1}".format(self.name,self.age))

    p1 = Person("Amit",43)
    p1.age = 33
    p1.myfunc()

def Tester():
    print("hello")

# Main ------------------------------------------------------------------
#print('\n--- Array-Print5Ints ---\n')
# Array_Print5Ints()
print('\n --- Array-Append ---\n')
# Array_Append()
#print('\n --- Array-Reverse Order ---\n')
# Array_RevOrder()
#print('\n --- Array-MultipleOps ---\n')
# Array_MultipleOps()
#print('\n --- Array_OccurenceInArray ---\n')
# Array_OccurenceInArray()
#print('\n --- Array_AppendArray ---\n')
# Array_AppendArray()
#print('\n --- Basic_RadiusCircleArea ---\n')
# Basic_RadiusCircleArea()
#print('\n --- CSVListTuple ---\n')
# Basic_CSVListTuple()
#Class_GeneralLearning()
Tester()