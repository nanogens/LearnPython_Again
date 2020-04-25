'''
25. Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
'''

def CheckValue(specifiedval, allvalues):
    if ((specifiedval in allvalues) == True):
        print("\nSpecified Value Found in All Values")
    else:
        print("\nSpecified Value Not Found")

CheckValue('x',"Mandrake") # not found
CheckValue('a',"Mandrake") # found

TestData = [1, 5, 8, 3]
CheckValue(3,TestData) # found
CheckValue(9,TestData) # not found