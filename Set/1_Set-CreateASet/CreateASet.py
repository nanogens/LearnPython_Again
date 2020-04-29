'''
1. Write a Python program to create a set.
'''

'''
Note:
Lists and tuples are standard Python data types that store values in a sequence. 
Sets are another standard Python data type that also store values. 
The major difference is that sets, unlike lists or tuples, cannot have multiple 
occurrences of the same element and store unordered values.
'''

#Create a new empty set
x = set()
print(x)
#Create a non empty set
n = set([0, 6, 2, 3, 4]) #sets are automatically ordered even if they are created unordered
m = set([1,3,9,5,5,2,3]) #also duplicates are eliminated
o = set([3,4,-5,-10,-3]) #also negative numbers show up on the right, going frm most negative midlist to least negative
print(n)
print(m)
print(o)